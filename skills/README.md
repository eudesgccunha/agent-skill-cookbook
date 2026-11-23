# When to use each skill

Descriptions come from the installed plugins (November 2026). Verify against your install with `/skills`.

## RTK

No skill. A Bash hook rewrites commands (`git status` becomes `rtk git status`) and compresses output. Always on. It does not cover Read, Grep or Glob.

## Pocock (you invoke)

| Skill | Use when |
|---|---|
| `grill-me` / `grilling` | The plan is vague and there is no repo yet, or you want a stress test of a decision. |
| `grill-with-docs` | A repo exists. Same interview, but it writes ADRs and a glossary as it goes. Default for design. |
| `setup-matt-pocock-skills` | Once per repo, before the other engineering skills. Sets the issue tracker, label vocabulary and doc layout. |
| `domain-modeling` | Terms are ambiguous, or a decision needs an ADR or glossary entry. |
| `to-spec` | A conversation already settled the design. Turns it into a spec in the issue tracker, no new interview. |
| `implement` | A spec or set of tickets exists and you want it built. |
| `tdd` | You want test-first work. |
| `diagnosing-bugs` | Something is broken, flaky or slow. |
| `codebase-design` | You shape a module interface or seam. |
| `code-review` | Before a PR. Checks repo standards and the originating spec. |
| `pr` | You need a PR body. |
| `prototype` | You need a throwaway answer to a design question. |
| `research` | You need facts from primary sources saved in the repo. |
| `wizard` | Steps only a human can do: credentials, dashboards, cutovers. |
| `writing-for-agents` | You edit `AGENTS.md`, `CLAUDE.md` or a skill. |

## Superpowers (the session-start hook picks skills for you)

| Skill | Use when |
|---|---|
| `using-superpowers` | Loaded automatically at session start. Makes the agent check for a skill before answering. |
| `brainstorming` | Creative or design work. Skip it in this setup: `grill-with-docs` does that job. |
| `writing-plans` | A spec exists for a multi-step task, before touching code. |
| `using-git-worktrees` | Feature work needs isolation from the current workspace. |
| `executing-plans` | You run the plan yourself in the current session. |
| `subagent-driven-development` | The plan has independent tasks that subagents can take. |
| `dispatching-parallel-agents` | Two or more tasks share no state and do not depend on each other. |
| `test-driven-development` | Implementing any feature or bugfix, before writing implementation code. |
| `systematic-debugging` | Any bug, test failure or odd behavior, before proposing a fix. |
| `verification-before-completion` | About to say "done", commit or open a PR. Forces you to run checks first. |
| `requesting-code-review` | A major task or feature is done, before merge. |
| `receiving-code-review` | Review feedback arrived. Verify it before applying it. |
| `finishing-a-development-branch` | Work is complete and tests pass. Decide how to integrate. |
| `writing-skills` | You create or edit a skill. |

Overlap with Pocock: TDD, debugging, review. Pick one family per stage.

## Ponytail (optional)

Not installed in the author's setup. The notes below come from its README as summarized in a third-party install guide, so test in a throwaway repo first.

- **What:** makes the agent write less code (YAGNI).
- **Use when:** the agent over-builds, adds abstractions nobody asked for, or inflates diffs.
- **Skip when:** the agent already stays in scope. Superpowers plus a tight `AGENTS.md` is often enough.
- **Toggle:** `/ponytail` to enable, "stop ponytail" to disable.
- **Install (Claude Code):**
  ```
  /plugin marketplace add DietrichGebert/ponytail
  /plugin install ponytail@ponytail
  ```
- **Gotcha:** its hooks run in Node. With nvm, `node` must be on the PATH of non-interactive shells, or the hooks stay silent.

Source: https://github.com/DietrichGebert/ponytail

## Caveman (optional)

| Skill | Use when |
|---|---|
| `caveman` | Execution phases. Turn it off for design and teaching. |
| `caveman-commit` | You want a compact Conventional Commits message. |
| `caveman-review` | You want one-line review findings. |
| `caveman-compress` | A memory file such as `CLAUDE.md` is large. |
| `caveman-stats` | You want real token usage for the session. |
| `cavecrew` | Delegate code search, small edits or diff review to cheap subagents. |
| `caveman-help` | You forget the modes and commands. |
