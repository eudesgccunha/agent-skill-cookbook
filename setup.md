# Setup

Checked against Claude Code on Ubuntu, November 2026.

```bash
# RTK: install from https://github.com/rtk-ai/rtk, then
rtk init -g
rtk gain          # must print savings stats; "command not found" means wrong package

# Superpowers, Pocock skills
claude plugin install superpowers@claude-plugins-official
claude plugin install mattpocock-skills@claude-plugins-official

# Caveman (optional)
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
```

Do not install the same skill through a plugin and through `npx skills`. It duplicates it.

## Suggested `CLAUDE.md` block

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
