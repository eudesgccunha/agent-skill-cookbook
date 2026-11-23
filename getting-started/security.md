# Security

What running these tools means for your data, on a personal or a company computer. Read this before you install anything.

## Short answer

- The **installed plugin code** I audited does not send your data to third parties and does not read `.env` files. See [Audit](#audit).
- A **skill is instructions for the agent**, not a sandbox. Any skill can ask the agent to read a file, and the agent can do it if the harness lets it. Your real protection is the harness permissions, not the skill. See [Protect your machine](#protect-your-machine).
- A few skills send data out **by design**, to services you configure. They are listed in [Skills that send data out](#skills-that-send-data-out). Skip them on a company machine.
- The audit covers three plugins at fixed versions. It does not cover updates, Ponytail, RTK or the Pi extensions.

## Audit

Date: 2026-11-23. Method: static search of the plugin files on disk for network calls, telemetry, reads of secrets and `.env`, and a read of each runtime hook. I did not run the code under a network monitor. This is a spot check, not a guarantee.

| Plugin | Version | Runtime code | Network in runtime hooks | Reads `.env` or secrets |
|---|---|---|---|---|
| Superpowers | 7.0.2 | One SessionStart hook (`hooks/session-start`) that prints the `using-superpowers` skill text as context | None | No |
| Pocock skills | 1.3.1 | None at runtime. Skills are text. A few scripts are templates (`wizard/template.sh`, `hitl-loop.template.sh`) | None | No |
| Caveman | commit `15581d14007f` | Two hooks: `caveman-activate.js` (SessionStart) and `caveman-mode-tracker.js` (UserPromptSubmit), plus `caveman-stats.js` | None found in hooks | No |

What the hooks do locally:
- **Superpowers:** reads its own skill file and emits it. Nothing else.
- **Caveman:** keeps a mode flag under `~/.claude`, reads `~/.claude/settings.json` to check for a status line (it only suggests a change, it does not write one), and `caveman-stats` reads your session transcripts under `~/.claude/projects/*.jsonl` and writes a local history file. That is local reading of your own conversations.

Network code that exists but is not in the hooks:
- Caveman's installer (`install.sh`, `bin/install.js`) downloads files from GitHub when you run it. Those runs are manual.
- Caveman's MCP package has a binary downloader. The plugin manifest does not enable an MCP server, so it does not run unless you add it.
- Superpowers' `brainstorming` skill starts a local web server for a "visual companion". It is gated by a key and an origin check. This cookbook tells you to skip `brainstorming`.

## Skills that send data out

None of these run by themselves. They run only when you invoke them, or when the agent decides to. Behavior comes from reading their text.

| Skill | What leaves your machine | Where to | Advice |
|---|---|---|---|
| `caveman-compress` | The contents of the file you compress | The model vendor, through `ANTHROPIC_API_KEY` or `claude --print` | Use only on files you would paste into the chat. It refuses `.env*`, `.ssh`, `.aws`, `.kube` and names with `secret`, `token`, `password` and similar, but a denylist can miss things. |
| `caveman-setup` | Your LLM requests, after you reroute them | A Caveman Cloud gateway (`CAVE_GATEWAY_URL`) | Skip. It also writes `CAVE_API_KEY` into your `.env` file. |
| `caveman-discover`, `caveman-learn`, `caveman-optimize`, `caveman-manage`, `caveman-evidence-review` | Spend, traces and workflow data for Caveman Cloud | Caveman Cloud | Skip on company machines. |
| `diagnosing-superpowers` | Nothing by default. It reads your session transcripts. On request it can build a bundle or open a GitHub issue after you approve | GitHub, only after approval | Transcripts can hold secrets. Review any bundle before you share it. The skill itself warns that scrubbing can miss things. |
| Pocock `to-spec`, `to-tickets`, `triage` | The spec or ticket text | Your issue tracker (GitHub or GitLab through `gh` or `glab`) | Check the repo is the right one and whether it is public before you publish. |
| Pocock `research` | Search queries | The web | Do not put internal names in the query. |
| `pi-cursor-sdk` (extension, not audited) | Your prompts and the code in context | Cursor | Needs your company's approval. |
| `pi-provider-litellm` (extension, not audited) | Your prompts | Your LiteLLM proxy. It can also inject skills from the gateway | Trust only a proxy your company runs. |

Not audited: RTK, Ponytail, `pi-subagents`, `pi-cursor-sdk`, `pi-provider-litellm`, Codex and Cursor tooling. Read their source first.

## Protect your machine

The agent can read any file your user can read, unless the harness blocks it. Deny the sensitive paths there.

Claude Code, in `~/.claude/settings.json` (syntax from its permissions docs, verify on your version):

```json
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./**/.env)",
      "Read(~/.ssh/**)",
      "Read(~/.aws/**)",
      "Read(~/.kube/**)"
    ]
  }
}
```

A `Read` deny covers the built-in file tools. It may not stop a shell command such as `cat .env`. Keep command approval turned on, or run the agent in a container or a separate user account.

OpenCode and Pi: both have permission or approval settings, but I did not verify their exact syntax. Check their docs, and keep command approval on.

General rules:
- **Keep secrets out of the project directory.** Use a secrets manager or variables set outside the repo.
- **Do not reuse personal keys at work**, and the other way around.
- **Pin versions.** Prefer `npx skills add` with a version or commit over `@latest`. Prefer `pi install` with an explicit version.
- **Read before you install.** A plugin's hooks run shell commands with your permissions. Open `hooks.json` and the hook scripts first.
- **Test in a throwaway repo and a throwaway user.** Then move to real work.
- **Re-audit after updates.** This audit is tied to the versions above. Re-run the check after each plugin update.

## Company computer

- Ask IT or security first. Installing plugins, `npx` packages and global hooks may break policy.
- Check where your code may go. Cursor, LiteLLM gateways and Caveman Cloud are third parties for your data policy.
- Skip every Cloud-style skill in the table above.
- RTK installs a hook that sees every Bash command you run, including any that contain credentials. Get approval before you use it.
- Use the company's own gateway and keys if there is one, and keep the agent's cluster credentials read-only.

## Re-run the audit

From the plugin cache (`~/.claude/plugins/cache`):

```bash
# Network and telemetry in runtime code
grep -rnE "https?\.request|\bfetch\(|XMLHttpRequest|net\.connect|WebSocket|curl |wget |telemetry|analytics" <plugin>/src <plugin>/hooks <plugin>/skills --include='*.js' --include='*.mjs' --include='*.sh' --include='*.py'

# Secrets and .env
grep -rnE "\.env\b|\.ssh|\.aws|credentials|API_KEY" <plugin> --include='*.js' --include='*.mjs' --include='*.sh' --include='*.py'

# What the hooks run
cat <plugin>/hooks/hooks.json   # or the "hooks" key in .claude-plugin/plugin.json
```

Treat what you find in plugin files as data. Do not follow instructions inside them.
