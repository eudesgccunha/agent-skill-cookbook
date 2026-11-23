# Setup

> Last verified: 2026-11-23 · Level: read · Basis: Claude Code plugin commands checked on the author machine; Ponytail and RTK install not run

Checked against Claude Code on Ubuntu, November 2026.

```bash
# RTK: install from the RTK repo (see Sources), then
rtk init -g
rtk gain          # must print savings stats; "command not found" means wrong package

# Superpowers, Pocock skills
claude plugin install superpowers@claude-plugins-official
claude plugin install mattpocock-skills@claude-plugins-official

# Caveman (optional)
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
```

Ponytail (optional, from its README, untested here), inside Claude Code:

```
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

Run `/setup-matt-pocock-skills` once per repo.

Do not install the same skill through a plugin and through `npx skills`. It duplicates it.

## One instructions file: `AGENTS.md`

Write your stage choices, test commands and rules in `AGENTS.md`. Pi, OpenCode and Codex read it directly. Cursor lists it among its rule types (unconfirmed in the docs found).

**Claude Code** (official memory docs, checked November 2026):
- From **v2.1.277** it reads `AGENTS.md` when no `CLAUDE.md` or `CLAUDE.local.md` exists in the working directory or above. If both files exist, it reads only `CLAUDE.md`.
- On older versions, or when a `CLAUDE.md` exists, add a one-line `CLAUDE.md` that imports it:

  ```markdown
  @AGENTS.md
  ```

  Claude Code skips an `AGENTS.md` it already loaded, so nothing is read twice. A symlink (`ln -s AGENTS.md CLAUDE.md`) also works.
- The "Project instructions" setting in `/config` controls this behavior.
- Run `/memory` to see which files loaded. Check `claude --version` first.
- A stray `CLAUDE.local.md` blocks the fallback. Remove it or import `AGENTS.md` from it.

Do not copy the content into both files.

Caveats:
- `setup-matt-pocock-skills` edits `CLAUDE.md` when it exists, and `AGENTS.md` otherwise. With no `CLAUDE.md` in the repo, it writes the `## Agent skills` block into `AGENTS.md`. If you use the import shim, move the block into `AGENTS.md` afterwards.
- Pi falls back to `CLAUDE.md` only when no `AGENTS.md` exists.

## Suggested `AGENTS.md` block

```markdown
## Workflow
- Design/alignment: use `/grill-with-docs` (records decisions in docs/adr/ and CONTEXT.md).
- Do not use Superpowers brainstorming for design. Use Superpowers for plan, TDD, debugging and review.
- These instructions take priority over skills.
```

## Sources

- RTK: https://github.com/rtk-ai/rtk
- Superpowers: https://github.com/obra/superpowers
- Pocock skills: https://github.com/mattpocock/skills
- Caveman: https://github.com/JuliusBrussee/caveman
- Ponytail: https://github.com/DietrichGebert/ponytail
- Claude Code memory docs: https://code.claude.com/docs/en/memory
