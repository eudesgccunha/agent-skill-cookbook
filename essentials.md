# Essential skills

You do not need every skill. This is the short list worth installing, and what to skip.

## Pocock: keep 7

| Skill | Why keep it |
|---|---|
| `grill-with-docs` | Best design starter: interview plus ADRs and glossary. |
| `grilling` | Primitive used by `grill-with-docs` and `grill-me`. Install it with them. |
| `domain-modeling` | Keeps the glossary and ADRs current. |
| `setup-matt-pocock-skills` | Run once per repo. The other engineering skills expect its config. |
| `diagnosing-bugs` | Strong loop for hard or flaky bugs. |
| `code-review` | Standards plus spec review before a PR. |
| `pr` | PR body in one step. |

Add later if the need shows up: `tdd`, `to-spec`, `implement`, `prototype`, `research`, `codebase-design`, `wizard`, `writing-for-agents`.

`tdd` is optional here only because Superpowers already ships `test-driven-development`. Keep one.

## Superpowers: keep 5

| Skill | Why keep it |
|---|---|
| `writing-plans` | Turns a spec into steps before code. |
| `test-driven-development` | Test-first discipline for features and fixes. |
| `systematic-debugging` | Cause before fix. |
| `verification-before-completion` | Blocks "done" claims without proof. |
| `requesting-code-review` | Review gate before merge. |

Skip `brainstorming` (grill covers design). The rest (`subagent-driven-development`, `dispatching-parallel-agents`, `using-git-worktrees`, `finishing-a-development-branch`) help on larger plans. Add them when you run multi-task plans.

Superpowers installs as a whole plugin on Claude Code, so every skill loads. Selective install is not confirmed. Disable what you skip through the "Superpowers" line in your `CLAUDE.md`.

## Caveman: keep 3

| Skill | Why keep it |
|---|---|
| `caveman` | Shorter replies in execution phases. |
| `caveman-commit` | Compact Conventional Commits. |
| `caveman-compress` | Shrinks large memory files such as `CLAUDE.md`. |

Optional: `caveman-review` (one-line findings), `caveman-stats` (usage), `cavecrew` (Claude Code only, needs subagents).

Skip: `caveman-setup`, `caveman-discover`, `caveman-evidence-review`, `caveman-learn`, `caveman-manage`, `caveman-optimize`. They belong to Caveman Cloud (spend observability), not day-to-day coding.

## RTK

No skill to pick. Install the hook for your harness (see [harnesses.md](harnesses.md)).

## Ponytail

Optional. Install only if the agent over-builds.
