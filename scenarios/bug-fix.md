# Bug fix

> Last verified: 2026-11-23 · Level: read · Basis: written from the skill texts and docs; the scenario was not run end to end

[All scenarios](README.md)

Goal: fix the cause, not the symptom, with a test that proves it.

1. **Find the cause.** Unknown or intermittent: `diagnosing-bugs`. Plain failing test: `systematic-debugging`. Use one, not both.
2. **Confirm with evidence** (log, trace, minimal repro) before any edit.
3. **Write a failing test** that captures the bug (`test-driven-development`).
4. **Fix at the narrowest layer.** Do not clean up nearby code.
5. **Run the full test suite**, then `verification-before-completion`.
6. **Ship:** [Review and PR](review-and-pr.md).

Prompt:
> Use diagnosing-bugs. Symptom: <what>. Repro: <how>. Do not edit until you show evidence for the cause.

Harness notes: on Pi without a subagent extension, keep the log reading in the main thread and let RTK trim output. With the extension, delegate log reading to a subagent. Done when the new test fails before the fix and passes after.
