# agent-skill-cookbook

Recipes for choosing the right agent skill for each workflow. Covers RTK, Superpowers, Matt Pocock's skills and Caveman, used with Claude Code.

## Tools at a glance

| Tool | What it does | How it runs |
|---|---|---|
| RTK | CLI proxy that compresses command output | Automatic (Bash hook) |
| Superpowers | Plan, TDD, debugging, subagents, review | Automatic (session-start hook picks skills) |
| Pocock skills | Grilling, domain modeling, TDD, review, PR | You invoke them |
| Caveman | Short replies, fewer output tokens | Mode you toggle |

Recommended base: RTK + Pocock (design) + Superpowers (execution). Caveman is optional.

## Rule of thumb

Design with Pocock. Execute with Superpowers. Compress with RTK and Caveman.

Pocock and Superpowers overlap on TDD, debugging and review. Pick one per stage and say so in `CLAUDE.md` (see [setup](setup.md)).

## Workflows

- [New feature](workflows/new-feature.md)
- [Bug fix](workflows/bug-fix.md)
- [Refactor](workflows/refactor.md)
- [Review and PR](workflows/review-and-pr.md)
- [Research and prototyping](workflows/research-and-prototype.md)
- [Cutting token cost](workflows/token-cost.md)

## Skill index

| Skill | Use when | Workflow |
|---|---|---|
| `grilling` / `grill-me` | A plan or idea is vague | New feature |
| `domain-modeling` | Terms are confusing, or a decision needs an ADR | New feature |
| `tdd` | You want test-first work | New feature, bug fix |
| `diagnosing-bugs` | Something is broken, flaky or slow | Bug fix |
| `codebase-design` | You are shaping a module interface or seam | Refactor |
| `code-review` | Before opening a PR | Review and PR |
| `pr` | You need a PR body | Review and PR |
| `prototype` | You need a throwaway answer to a design question | Research and prototyping |
| `research` | You need facts from primary sources | Research and prototyping |
| `writing-for-agents` | You edit `AGENTS.md`, `CLAUDE.md` or a skill | Any |
| `wizard` | Steps only a human can do (credentials, cutover) | Any |
| `caveman`, `caveman-commit`, `caveman-review` | Execution phases, commits, reviews | Token cost |
| `caveman-compress` | A memory file is too large | Token cost |
| `cavecrew` | Delegate search or small edits to cheap subagents | Token cost |

Skill names follow the plugin versions listed in [setup](setup.md). Verify them with `/skills` in your install.
