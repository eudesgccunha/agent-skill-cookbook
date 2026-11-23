# Architecture exploration

> Last verified: 2026-11-23 · Level: read · Basis: written from the skill texts and docs; the scenario was not run end to end

[All scenarios](README.md)

Goal: a correct mental model of unfamiliar code, with file references.

1. **Orient cheaply.** CC: `caveman-explore` (read-only, returns `path:line`, keeps reads out of main context) or the built-in Explore subagent. OC and Pi: ask the agent to map directories and entry points only, no edits.
2. **Trace one flow end to end** (request in, result out). Ask for `path:line` for every claim.
3. **Find weak spots.** `improve-codebase-architecture` scans for deepening opportunities and builds an HTML report, then grills you on the one you choose. `codebase-design` gives the vocabulary.
4. **Record what you learned.** `domain-modeling` writes terms and ADRs. Draw it with [Diagram](diagram.md).

Prompt:
> Map this repo: entry points, main modules, data flow. Read only. Cite path:line for each claim. Say what you could not confirm.

Harness notes: on Pi, use the subagent extension for the exploration so reads stay out of the main context. Without it, run the exploration in a fresh session. Done when every claim has a file reference and unknowns are listed, not guessed.
