# New feature

[All scenarios](README.md)

Goal: agree on the design first, then build it test-first.

1. **Align.** `grill-with-docs` with a repo (`grill-me` without). Output: decisions in `docs/adr/` and `CONTEXT.md`.
2. **Name things.** `domain-modeling` if terms are unclear.
3. **Plan.** `writing-plans`. Skip Superpowers `brainstorming`.
4. **Isolate** (optional, bigger work): `using-git-worktrees`.
5. **Build.** `test-driven-development`, one small step at a time.
6. **Verify.** `verification-before-completion`.
7. **Ship:** [Review and PR](review-and-pr.md).

Turn Caveman on from step 3. Keep it off for steps 1 and 2.

Prompt:
> Use grill-with-docs. Feature: <what>. Constraints: <list>. Ask me one question at a time.

Harness notes: CC can run independent plan tasks through `subagent-driven-development`. OC can too. Pi can too once the subagent extension is installed. Without it, Pi runs the plan task by task in one thread (`executing-plans`). Done when plan tasks are checked off, tests pass and ADRs are written.
