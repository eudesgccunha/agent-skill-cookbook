# Scenarios

Pick your task, follow the steps. Each scenario names the skills, what changes on Claude Code (CC), OpenCode (OC) and Pi, and how to know you are done.

Skill names are in [skills/essentials.md](../skills/essentials.md). Install and paths per harness are in [harnesses/README.md](../harnesses/README.md).

## Quick pick

| I want to... | Go to |
|---|---|
| Fix a bug | [Bug fix](bug-fix.md) |
| Build a new feature | [New feature](new-feature.md) |
| Write or change a Kubernetes manifest | [Kubernetes manifest](kubernetes-manifest.md) |
| Understand an unfamiliar codebase | [Architecture exploration](architecture-exploration.md) |
| Draw a diagram | [Diagram](diagram.md) |
| Restructure code without changing behavior | [Refactor](refactor.md) |
| Review a branch or open a PR | [Review and PR](review-and-pr.md) |
| Upgrade a dependency or migrate | [Migration](migration.md) |
| Plan work too big for one session | [Large work](large-work.md) |
| Look up docs or API facts | [Research](research.md) |
| Investigate a live failure | [Incident](incident.md) |

## How the harnesses differ

| | CC | OC | Pi |
|---|---|---|---|
| Skills load | Auto-picked by Superpowers hook, or `/name` | Invoke by name, or list them in `AGENTS.md` | Invoke by name, or list them in `AGENTS.md` |
| Subagents (`cavecrew`, `subagent-driven-development`) | Yes | Yes | Only after you install a subagent extension ([harnesses/README.md](../harnesses/pi.md#pi-install-a-subagent-extension)). Without it, one thread |
| Instructions file | `AGENTS.md` (v2.1.277+ without `CLAUDE.md`, else `@AGENTS.md` import) | `AGENTS.md` | `AGENTS.md` |
| RTK hook | `rtk init -g` | `rtk init -g --opencode` | `rtk init -g --agent pi` |

If a skill does not load by itself, name it in the prompt: "use systematic-debugging".

## Tips that apply everywhere

- Start a new session per task. Context from the last task misleads the next.
- Ask for evidence: file and line, command output, test result.
- RTK runs in the background. Check it with `rtk gain`.
- Caveman: on for execution, off for design and teaching.
- On Pi, check that a subagent extension is installed before you start a scenario that delegates.
- If a skill seems missing, run `/skills` (CC) or list the skills folder (OC, Pi), then name the skill in your prompt.
