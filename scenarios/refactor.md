# Refactor

> Last verified: 2026-11-23 · Level: read · Basis: written from the skill texts and docs; the scenario was not run end to end

[All scenarios](README.md)

Goal: change structure, not behavior.

1. **Pin behavior** with tests. Missing coverage: add tests first (`test-driven-development`).
2. **Choose the shape** with `codebase-design`. Big redesign: `grill-with-docs` first.
3. **Move in small steps.** Run tests after each.
4. **Review** with `code-review`.

Done when tests pass unchanged and the diff shows no behavior edits.
