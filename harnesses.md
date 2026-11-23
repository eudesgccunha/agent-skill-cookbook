# Harnesses

How the same toolset applies to Claude Code, Codex, Cursor, OpenCode and Pi. Checked November 2026 against vendor docs and the `skills` CLI. Paths and flags change between versions, so verify before relying on them.

## What carries over

All five read the same skill format: a folder with a `SKILL.md`. So Pocock, Superpowers and Caveman skills are portable. What differs is how you install them, which hooks run, and where the instructions file lives.

| | Claude Code | Codex | Cursor | OpenCode | Pi |
|---|---|---|---|---|---|
| Instructions file | `CLAUDE.md` | `AGENTS.md` (`~/.codex/AGENTS.md` for user level) | rules and `AGENTS.md` | `AGENTS.md` | `AGENTS.md`, falls back to `CLAUDE.md` |
| Skills dir (project) | `.claude/skills` | `.agents/skills` | `.agents/skills`, `.cursor/skills` | `.opencode/skills` | `.pi/skills` |
| Skills dir (user) | `~/.claude/skills` | `~/.agents/skills` (older docs: `~/.codex/skills`) | `~/.agents/skills`, `~/.cursor/skills` | `~/.config/opencode/skills` | `~/.pi/agent/skills` |
| Plugins | Yes, `/plugin` | Skills only (as far as found) | Skills, rules | Skills, plugins | Packages (`pi install`) |
| Subagents | Yes | Limited | Yes | Yes | Only with a subagent extension (required, see below) |

The non-Claude rows come from web search of vendor docs and the `skills` CLI README, not from running those tools. Treat as unverified.

## Install per harness

Generic installer for skills (pick agent with `-a`, global with `-g`):

```bash
npx skills@latest add mattpocock/skills
npx skills add juliusbrussee/caveman --skill "caveman" -g -a <agent> -y
```

Run the Pocock one without `-a` and choose skills and agent in the menu. Select only the ones in [essentials.md](essentials.md).

| | Claude Code | Codex | Cursor | OpenCode | Pi |
|---|---|---|---|---|---|
| RTK | `rtk init -g` | Not in `rtk init --agent` list. Check the RTK README | `rtk init -g --agent cursor` | `rtk init -g --opencode` | `rtk init -g --agent pi` |
| Pocock | plugin or `npx skills` | `npx skills`, pick Codex | `npx skills`, pick Cursor | `npx skills`, pick OpenCode | `npx skills`, pick Pi |
| Superpowers | `/plugin install superpowers@claude-plugins-official` | Follow `obra/superpowers` docs | Follow `obra/superpowers` docs | Manual, see its `INSTALL.md` | Listed as supported, command unconfirmed |
| Caveman | plugin or `npx skills` | `npx skills` | `npx skills` | `npx skills` | `npx skills` |
| Ponytail | `/plugin install ponytail@ponytail` | `npx skills` | `npx skills` | `opencode-ponytail` package | `pi install npm:@dietrichgebert/ponytail` |

Do not install the same skill by plugin and by `npx skills`. It duplicates.

## Pi: install a subagent extension

Pi has no built-in subagents. Several skills and scenarios in this cookbook delegate work to subagents (`subagent-driven-development`, `dispatching-parallel-agents`, `cavecrew`, the exploration step in [scenarios.md](scenarios.md)). **On Pi, install a subagent extension before you rely on them.** Without it, run everything in one thread.

Community packages found on pi.dev (none is official, versions as listed in November 2026):

| Package | Install | Notes |
|---|---|---|
| `@tintinweb/pi-subagents` | `pi install npm:@tintinweb/pi-subagents` | Claude Code-style autonomous subagents. Closest to the Claude Code workflow. |
| `@narumitw/pi-subagents` | `pi install npm:@narumitw/pi-subagents` | Most downloaded in the listing. Try it first with `pi -e npm:@narumitw/pi-subagents`. |
| `@mjakl/pi-subagent` | `pi install npm:@mjakl/pi-subagent` | Agents are Markdown files. Needs Pi 0.80.5 or newer. |
| `@johnnywu/pi-subagents` | `pi install npm:@johnnywu/pi-subagents` | Agents in `.pi/agents/*.md`, delegated through a `subagent` tool. |

Choose one. Do not install two, the tools can clash.

Pi packages run code and shape agent behavior. Read the package source before you install it. Check the package page for the current version, because the listing changes.

Verify after install:
1. Restart Pi. The startup header lists loaded extensions and skills.
2. Ask: "Use a subagent to list the top-level folders of this repo." The agent should call the subagent tool.
3. Manage what loads with `pi config`.

## What changes in practice

- **Superpowers auto-loading.** On Claude Code its session-start hook loads `using-superpowers`. Elsewhere you may lose that, so invoke skills by name or reference them from `AGENTS.md`.
- **Caveman auto-activation.** Installed through `npx skills`, it does not get activation rules. Turn it on with `/caveman`.
- **`cavecrew` subagents.** Written for Claude Code agents. On Pi and OpenCode, behavior depends on the subagent support you have. Untested.
- **RTK.** The hook only rewrites shell commands. Built-in read and search tools bypass it on every harness. Hook support varies per harness.
- **Cursor.** Rules still exist beside skills. Cursor 2.4+ has `/migrate-to-skills` to convert old rules and commands.
- **Pi.** Minimal by design. Few built-ins, so skills carry more weight. Install a subagent extension (section above). `pi config` enables or disables individual skills and extensions.
- **Codex.** Reads `AGENTS.md` before work starts. Put the workflow block there.

## Instructions block for non-Claude harnesses

Put in `AGENTS.md` (same content as the `CLAUDE.md` block in [setup.md](setup.md)):

```markdown
## Workflow
- Design/alignment: use `grill-with-docs` (records decisions in docs/adr/ and CONTEXT.md).
- Do not use Superpowers brainstorming for design. Use Superpowers for plan, TDD, debugging and review.
- Before saying work is done, run the project's verification commands.
- These instructions take priority over skills.
```

## Sources

- https://github.com/vercel-labs/skills (`npx skills` CLI)
- https://developers.openai.com/codex/skills (Codex)
- https://cursor.com/docs/skills (Cursor)
- https://opencode.ai/docs/skills (OpenCode)
- https://pi.dev (Pi) and its package pages for the subagent extensions
- `rtk init --help` (local, RTK)
