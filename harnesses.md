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
| Subagents | Yes | Limited | Yes | Yes | Minimal by design |

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

## What changes in practice

- **Superpowers auto-loading.** On Claude Code its session-start hook loads `using-superpowers`. Elsewhere you may lose that, so invoke skills by name or reference them from `AGENTS.md`.
- **Caveman auto-activation.** Installed through `npx skills`, it does not get activation rules. Turn it on with `/caveman`.
- **`cavecrew` subagents.** Claude Code only.
- **RTK.** The hook only rewrites shell commands. Built-in read and search tools bypass it on every harness. Hook support varies per harness.
- **Cursor.** Rules still exist beside skills. Cursor 2.4+ has `/migrate-to-skills` to convert old rules and commands.
- **Pi.** Minimal by design. Few built-ins, so skills carry more weight. `pi config` enables or disables individual skills.
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
- https://pi.dev (Pi)
- `rtk init --help` (local, RTK)
