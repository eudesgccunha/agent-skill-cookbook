# Contributing

This repo is a guide to the agent skills and practices that work for the author's scenarios, with the evidence behind each one. Quality over volume. A short, true, dated page beats a long guess.

"Best" means best for a stated scenario, not best in general. When you propose a change, name the scenario it serves.

## What belongs here

- A skill, practice or scenario that you used on real work, with a result you can describe.
- Facts about a harness (Claude Code, OpenCode, Pi, Codex, Cursor) checked against its docs or a run.
- Corrections: a wrong command, a stale path, a broken link, a claim that no longer holds.

## What does not belong

- Skills or tools you have not used. Say "untested" in an issue instead.
- Marketing text, rankings without a method, or praise of a tool without trade-offs.
- Secrets, internal URLs, company code or customer data, even as an example.
- Install commands you did not read. Never add `curl | sh` one-liners without a pinned version and a note on what they do.

## Where a file goes

| Folder | Put here |
|---|---|
| `getting-started/` | Install, setup and security notes |
| `scenarios/` | One task per file: goal, steps with skills, harness notes, a "done when" check |
| `skills/` | Catalog entries, essentials, trade-offs between skills |
| `harnesses/` | Per-harness install, paths and differences |
| `practices/` | Cross-cutting habits that hold across tools |
| `examples/` | Reference artifacts that you rendered or ran |

Link new files from the README of their folder.

## Every page carries a verification line

Right under the title, one line:

```markdown
> Last verified: 2026-11-23 · Level: read · Basis: skill texts of the installed plugins; no benchmark
```

| Level | Meaning |
|---|---|
| `tested` | You ran it and saw the result. Say on which version and machine. |
| `read` | You read the source, the skill text or the docs you installed. You did not run it. |
| `web` | You relied on web docs or search results only. |

Rules:
- The date is the day you checked, not the day you edited.
- Pick the lowest level that is true. Never claim `tested` for something you only read.
- When you change a claim, re-verify it and update the line. A typo fix does not need a new date.
- Name versions (plugin version, commit, CLI version) in the basis when they matter.

## Raising a page to `tested`

The preferred source of `tested` evidence is a [harness-bench](https://github.com/eudesgccunha/harness-bench) run: same tasks, same harness and model, with a no-skill control. Put in the basis the harness, model, task kinds, number of runs and the confidence interval. A result inside the noise does not justify a change. The [skills axis design](https://github.com/eudesgccunha/harness-bench/blob/main/docs/skills-axis.md) for harness-bench is proposed, not built, so for now `tested` means you ran the skill yourself on real work and describe what happened.

## Entry criteria for a skill or practice

Show these four in the page or in your pull request:
1. **What it does**, in one sentence, from its own text.
2. **When it helps and when it hurts.** At least one trade-off or cost.
3. **Evidence.** Where you used it, on which harness, and what happened. If you have none, the level is `read` or `web`, and the page says it is unproven.
4. **Risk.** What it reads, writes or sends out. Check hooks, scripts and any network call. See [security](getting-started/security.md) for the method.

## Style

- English. Short sentences. One idea per sentence.
- Commands in code blocks that you can copy. Exact names for skills, flags and paths.
- Say what you did not verify. Do not hide gaps behind confident wording.
- No pronouns for people you do not know. Do not guess names.
- Prefer a table for comparisons and numbered steps for procedures.

## Check your change

```bash
python3 scripts/check.py                    # links, anchors, verification line
python3 scripts/check.py --max-age-days 90  # also flag pages older than 90 days
```

The script uses only the standard library. A pull request should end with `PASS`.

## Pull requests

- One topic per pull request.
- In the description: what changed, the level of evidence, and what you did not check.
- Keep commit messages in Conventional Commits form (`docs:`, `fix:`).
- By contributing you agree your work is released under the [MIT license](LICENSE).

## Reviewing

Reviewers check, in order: no secrets or private data, claims match the stated level, links and anchors pass the script, trade-offs are present, style is plain.
