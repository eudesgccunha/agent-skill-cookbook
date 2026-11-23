# agent-skill-cookbook

Recipes for choosing the right agent skill for each workflow. Covers RTK, Superpowers, Matt Pocock's skills, Caveman and Ponytail, across Claude Code, OpenCode and Pi (plus Codex and Cursor notes).

## Tools at a glance

| Tool | What it does | How it runs |
|---|---|---|
| RTK | CLI proxy that compresses command output | Automatic (Bash hook) |
| Superpowers | Plan, TDD, debugging, subagents, review | Automatic (session-start hook picks skills) |
| Pocock skills | Grilling, domain modeling, TDD, review, PR | You invoke them |
| Caveman | Short replies, fewer output tokens | Mode you toggle |
| Ponytail (optional) | Makes the agent write less code | Mode you toggle |

Recommended base: RTK + Pocock (design) + Superpowers (execution). On Pi, also install a subagent extension, and optionally the Cursor and LiteLLM provider extensions ([harnesses/README.md](harnesses/pi.md#pi-install-a-subagent-extension)). Caveman and Ponytail are optional.

## Rule of thumb

Design with Pocock. Execute with Superpowers. Compress with RTK and Caveman.

Pocock and Superpowers overlap on TDD, debugging and review. Pick one per stage and say so in `AGENTS.md`. Trade-offs and the author's picks: [skills/tradeoffs.md](skills/tradeoffs.md).

**Before you install anything, read [security](getting-started/security.md).** Then follow [setup](getting-started/setup.md) and pick a [scenario](scenarios/README.md).

## Contents

| Folder | What is inside |
|---|---|
| [getting-started/](getting-started/) | [Setup](getting-started/setup.md) and [security](getting-started/security.md). Read both first |
| [scenarios/](scenarios/README.md) | Step-by-step recipes: bug fix, new feature, Kubernetes manifest, architecture exploration, diagram, refactor, review and PR, migration, large work, research, incident |
| [skills/](skills/README.md) | [Catalog](skills/README.md) of when to use each skill, the [essentials](skills/essentials.md) worth installing, and Pocock vs Superpowers [trade-offs](skills/tradeoffs.md) |
| [harnesses/](harnesses/README.md) | Claude Code, OpenCode, Pi, Codex and Cursor: install, paths, differences. [Pi extensions](harnesses/pi.md) |
| [practices/](practices/README.md) | Cross-cutting good practice, starting with [cutting token cost](practices/token-cost.md) |
| [examples/](examples/diagrams/harness-bench-run-flow.html) | Reference artifacts, such as an HTML diagram |

## License

MIT. See [LICENSE](LICENSE).
