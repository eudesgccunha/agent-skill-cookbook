# Migration or dependency upgrade

> Last verified: 2026-11-23 · Level: read · Basis: written from the skill texts and docs; the scenario was not run end to end

[All scenarios](README.md)

1. **Research the breaking changes** ([Research](research.md)). Read the changelog, not memory.
2. **Pin current behavior** with tests.
3. **Plan in steps** (`writing-plans`) that keep the build green after each one.
4. **Upgrade one thing at a time.** Run tests after each.
5. **Keep a rollback.** One commit per step makes revert easy.

Done when tests pass on the new version and the old version still builds from the previous commit.
