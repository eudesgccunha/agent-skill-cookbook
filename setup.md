# Setup

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

Write your stage choices, test commands and rules in `AGENTS.md`. Pi, OpenCode and Codex read it directly, and Cursor lists it among its rule types (unconfirmed in the docs found). **Claude Code reads `CLAUDE.md`, not `AGENTS.md`.** Bridge it with a one-line `CLAUDE.md`:

```markdown
@AGENTS.md
```

Claude Code expands the import, so `AGENTS.md` stays the single source. Do not copy the content into both files.

Caveats:
- `setup-matt-pocock-skills` edits `CLAUDE.md` when it exists, even if it only holds the import. Move the `## Agent skills` block it writes into `AGENTS.md` afterwards, or run it before you create the `CLAUDE.md` shim.
- If a tool still ignores `AGENTS.md`, check its docs. Pi falls back to `CLAUDE.md` only when no `AGENTS.md` exists.

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
