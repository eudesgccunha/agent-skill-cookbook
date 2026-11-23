# New feature

1. **Align the idea.** Run `grill-with-docs` (or `grill-me` without a repo). The agent interviews you until the plan has no gaps.
2. **Name things.** Run `domain-modeling` when terms are ambiguous. It updates the glossary and records ADRs for big decisions.
3. **Plan.** Let Superpowers write the plan (`writing-plans`). Skip its brainstorming step: grilling already did that job.
4. **Build test-first.** Use Superpowers `test-driven-development` (default) or Pocock `tdd`. Pick one. See [tradeoffs](../tradeoffs.md).
5. **Verify.** Superpowers `verification-before-completion` forces checks before you say done.
6. **Ship.** Continue in [Review and PR](review-and-pr.md).

Turn Caveman on from step 3 onward. Turn it off for steps 1 and 2: short answers hurt design talk.
