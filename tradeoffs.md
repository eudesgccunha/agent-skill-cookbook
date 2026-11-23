# Pocock vs Superpowers: trade-offs, setup and preferences

Both families ship TDD, debugging and review skills. This page compares them, lists what to configure before you use each one, and records the author's picks.

Based on reading the installed skill texts (November 2026), not on a benchmark. Re-read the skills after an update, they change.

## Trade-offs by stage

### TDD

| | Pocock `tdd` | Superpowers `test-driven-development` |
|---|---|---|
| Size | About 38 lines, plus `tests.md` and `mocking.md` | About 330 lines |
| Style | Light reference for good tests: behavior through public interfaces, agreed seams, anti-patterns | Strict. An "Iron Law", then red, verify red, green, verify green, refactor |
| Strength | Teaches what a good test is. Fewer tokens | Enforces the loop even when the agent wants to skip tests |
| Cost | Does not force the agent to follow it | Long. Costs more tokens on every use |
| Pick when | You trust the agent and want to save tokens | The agent skips tests or writes them after the code |

Pocock `tdd` asks you to confirm the seams (where tests go) before writing any test. Expect that question.

### Debugging

| | Pocock `diagnosing-bugs` | Superpowers `systematic-debugging` |
|---|---|---|
| Idea | Build a feedback loop first (failing test, curl script, replay, bisect, fuzz), then test hypotheses | Four phases: root cause, pattern analysis, hypothesis, implementation. No fix before the root cause |
| Strength | Handles flaky and performance bugs. Reads `GLOSSARY.md` and ADRs for context | Simple and fast for a clear error or failing test |
| Cost | Longer, more setup per bug | May stall on bugs you cannot reproduce on demand |
| Pick when | Hard, intermittent or slow bug | Test failure, stack trace or clear error |

### Review

| | Pocock `code-review` | Superpowers `requesting-code-review` |
|---|---|---|
| Idea | Two reviewers in parallel: Standards (repo rules plus a Fowler smell baseline) and Spec (what was asked) | Request a review of the finished work before merge |
| Strength | Catches scope creep and missing requirements, not only style | Short (about 95 lines), needs no spec |
| Cost | Needs subagents, a fixed starting point and a spec source | Less depth on spec compliance |
| Pick when | An issue or spec exists | No spec, small change |

Superpowers also has `receiving-code-review` (verify feedback before applying it) and `verification-before-completion` (run checks before saying done). Pocock has no direct equivalent. Keep both Superpowers ones regardless of your other picks.

### Rule

Never run both skills of one stage in the same session. State your choice in `AGENTS.md`.

## Setup before you use them

### Pocock

1. **Install** (see [harnesses.md](harnesses.md)).
2. **Run `setup-matt-pocock-skills` once per repo.** It is prompt-driven: it explores the repo, proposes answers, you confirm. It writes:
   - `docs/agents/issue-tracker.md`: where issues live. GitHub (needs the `gh` CLI), GitLab (needs `glab`), local markdown under `.scratch/`, or other.
   - `docs/agents/domain.md`: where `GLOSSARY.md` and ADRs live. Single context by default, multi-context for monorepos.
   - `docs/agents/triage-labels.md`: only if the `triage` skill is installed. Defaults: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`.
   - An `## Agent skills` block in your existing `CLAUDE.md` or `AGENTS.md`. It edits `CLAUDE.md` first when both exist, and asks before it creates one. If you use the `@AGENTS.md` shim, move the block into `AGENTS.md` ([setup.md](setup.md#one-instructions-file-agentsmd)).
3. **For `code-review`:**
   - Have a spec source: an issue reference in the commit messages, a path you pass, or a file under `docs/`, `specs/` or `.scratch/`. With none, the Spec review is skipped.
   - Document your standards in `CODING_STANDARDS.md`, `CONTRIBUTING.md` or similar. With none, only the smell baseline applies.
   - Subagent support. On Pi, install `pi-subagents` ([harnesses.md](harnesses.md#pi-install-a-subagent-extension)).
4. **For `tdd` and `diagnosing-bugs`:** create `GLOSSARY.md` and `docs/adr/` (through `grill-with-docs` or `domain-modeling`). Both skills read them when they exist. They work without them.
5. **For `to-spec`, `to-tickets`, `triage`:** the issue tracker from step 2 must work. Run `gh auth status` first.

### Superpowers

1. **Install** the plugin (Claude Code: `/plugin install superpowers@claude-plugins-official`).
2. **Restart the agent** so the session-start hook loads `using-superpowers`. Without the hook, skills do not auto-load. Name them in your prompt instead.
3. **Add the priority block to `AGENTS.md`:**
   ```markdown
   - Do not use Superpowers brainstorming for design. Use Superpowers for plan, TDD, debugging and review.
   - These instructions take priority over skills.
   ```
4. **Subagent skills** (`subagent-driven-development`, `dispatching-parallel-agents`) need subagent support. Pi: `pi-subagents`. Without it, use `executing-plans`.
5. **`using-git-worktrees`:** needs a git repo. Keep the working tree committed or stashed before you start.
6. **Test command:** put the project's test and lint commands in `AGENTS.md`. `verification-before-completion` runs what it finds there.

### Both

- One instructions file (`AGENTS.md`) with your stage choices, so the agent never picks two skills for one stage.
- A `docs/adr/` folder, so decisions have a place to land.
- Do not install the same skill through a plugin and through `npx skills`.

## Author preferences

These are the picks of the repo author. Adopt, adjust or ignore.

| Situation | Pick | Why |
|---|---|---|
| TDD | Superpowers `test-driven-development` | Long and strict: the agent must see the test fail before it implements. Fits agents that skip tests. |
| Hard or intermittent bug | Pocock `diagnosing-bugs` | Builds a feedback loop first, then tests hypotheses. Fits flaky and performance bugs. |
| Ordinary bug | Superpowers `systematic-debugging` | Four phases, no fix before the root cause. Fits a broken test or clear error. |
| Review with a spec or issue | Pocock `code-review` | Checks the diff against repo standards and against the spec, in parallel. Needs subagents, so Pi needs `pi-subagents`. |
| Review without a spec | Superpowers `requesting-code-review` | Shorter and needs no spec. |
| Design | Pocock `grill-with-docs` | Superpowers `brainstorming` stays off. |
| Plan and verify | Superpowers `writing-plans`, `verification-before-completion` | No Pocock equivalent in the same shape. |

Reach for Pocock `tdd` only when you trust the agent to follow the loop and want to save tokens.
