# Essential skills

> Last verified: 2026-11-23 · Level: read · Basis: skill texts of the installed plugins; picks are the author opinion

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

Superpowers installs as a whole plugin on Claude Code, so every skill loads. Selective install is not confirmed. Disable what you skip through the "Superpowers" line in your `AGENTS.md`.

## When Pocock and Superpowers overlap

Both families ship TDD, debugging and review skills. Use one per stage. Default picks, based on reading the skill texts (not on a benchmark):

| Stage | Pick | Why |
|---|---|---|
| TDD | Superpowers `test-driven-development` | Long and strict ("Iron Law", verify red, then green). Good when the agent skips tests. Pocock `tdd` is a 38-line loop: pick it to save tokens or when you trust the agent. |
| Debugging, hard or flaky bug | Pocock `diagnosing-bugs` | Starts by building a feedback loop (failing test, replay, bisect, fuzz), then tests hypotheses. Fits flaky and performance bugs. |
| Debugging, ordinary failure | Superpowers `systematic-debugging` | Four phases, no fix before root cause. Fits a failing test or clear error. |
| Review before a PR | Pocock `code-review` | Checks the diff against repo standards and the originating spec, in parallel. Needs subagents (Pi: install the extension) and a spec or issue to compare. |
| Review without a spec | Superpowers `requesting-code-review` | Shorter, no spec needed. |

Rule: never run both skills of one stage in the same session. Write your choice in `AGENTS.md`. Full comparison and setup: [skills/tradeoffs.md](tradeoffs.md).

## Caveman: keep 3

| Skill | Why keep it |
|---|---|
| `caveman` | Shorter replies in execution phases. |
| `caveman-commit` | Compact Conventional Commits. |
| `caveman-compress` | Shrinks large memory files such as `CLAUDE.md`. Sends the file to the model vendor, see [getting-started/security.md](../getting-started/security.md). |

Optional: `caveman-review` (one-line findings), `caveman-stats` (usage), `cavecrew` (needs subagents: native on Claude Code, an extension on Pi).

Skip: `caveman-setup`, `caveman-discover`, `caveman-evidence-review`, `caveman-learn`, `caveman-manage`, `caveman-optimize`. They belong to Caveman Cloud (spend observability), not day-to-day coding. They send data to a third party, see [getting-started/security.md](../getting-started/security.md).

## Security: Trail of Bits, keep 3

Source: [trailofbits/skills](https://github.com/trailofbits/skills) (about 8.4k stars on 2026-11-23, CC-BY-SA-4.0). Read the `SKILL.md` of each plugin. Not run on real work yet. Install only from the `trailofbits` org: forks and mirrors exist.

| Skill | Why keep it |
|---|---|
| `differential-review` | Security review of a PR or diff. Uses git blame, counts callers (blast radius), flags changed code with no test, writes a markdown report. Goes beyond `code-review`, which checks standards and spec. |
| `fp-check` | Verdict TRUE or FALSE POSITIVE for a suspected bug, with evidence. Verifies findings, does not hunt for new ones. Run it after any scanner or AI review. |
| `agentic-actions-auditor` | Static audit of GitHub Actions that run AI agents (Claude Code Action, Gemini CLI, Codex). Finds attacker input reaching the prompt, unsafe sandbox settings, wildcard allowlists. Reports only, does not edit. |

Install, inside Claude Code: `/plugin marketplace add trailofbits/skills`, then `/plugin install differential-review@trailofbits` (same for the other two).

Also built in: `/security-review` in Claude Code. The [Action version](https://github.com/anthropics/claude-code-security-review) is not hardened against prompt injection: use it on trusted PRs only.

Skip unless the scenario fits: `building-secure-contracts` (smart contracts), `c-review` (C/C++), `testing-handbook-skills` (fuzzers, sanitizers).

Security skills read your code and run `Bash`. Review a plugin before you install it, see [getting-started/security.md](../getting-started/security.md).

## Pi: required extension

On Pi, add a subagent extension to this list. Several Superpowers skills and `cavecrew` depend on subagents. See [Pi extensions](../harnesses/pi.md#pi-install-a-subagent-extension).

## RTK

No skill to pick. Install the hook for your harness (see [harnesses/README.md](../harnesses/README.md)).

## Ponytail

Optional. Install only if the agent over-builds.
