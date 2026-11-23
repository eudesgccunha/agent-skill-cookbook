# Scenarios

Pick your task, follow the steps. Each scenario names the skills, what changes on Claude Code (CC), OpenCode (OC) and Pi, and how to know you are done.

Skill names are in [essentials.md](essentials.md). Install and paths per harness are in [harnesses.md](harnesses.md).

## Quick pick

| I want to... | Go to |
|---|---|
| Fix a bug | [Bug fix](#bug-fix) |
| Build a new feature | [New feature](#new-feature) |
| Write or change a Kubernetes manifest | [Kubernetes manifest](#kubernetes-manifest) |
| Understand an unfamiliar codebase | [Architecture exploration](#architecture-exploration) |
| Draw a diagram | [Diagram](#diagram) |
| Restructure code without changing behavior | [Refactor](#refactor) |
| Review a branch or open a PR | [Review and PR](#review-and-pr) |
| Upgrade a dependency or migrate | [Migration](#migration-or-dependency-upgrade) |
| Plan work too big for one session | [Large work](#large-work) |
| Look up docs or API facts | [Research](#research) |
| Investigate a live failure | [Incident](#incident-or-live-failure) |

## How the harnesses differ

| | CC | OC | Pi |
|---|---|---|---|
| Skills load | Auto-picked by Superpowers hook, or `/name` | Invoke by name, or list them in `AGENTS.md` | Invoke by name, or list them in `AGENTS.md` |
| Subagents (`cavecrew`, `subagent-driven-development`) | Yes | Yes | Only after you install a subagent extension ([harnesses.md](harnesses.md#pi-install-a-subagent-extension)). Without it, one thread |
| Instructions file | `AGENTS.md` (v2.1.277+ without `CLAUDE.md`, else `@AGENTS.md` import) | `AGENTS.md` | `AGENTS.md` |
| RTK hook | `rtk init -g` | `rtk init -g --opencode` | `rtk init -g --agent pi` |

If a skill does not load by itself, name it in the prompt: "use systematic-debugging".

---

## Bug fix

Goal: fix the cause, not the symptom, with a test that proves it.

1. **Find the cause.** Unknown or intermittent: `diagnosing-bugs`. Plain failing test: `systematic-debugging`. Use one, not both.
2. **Confirm with evidence** (log, trace, minimal repro) before any edit.
3. **Write a failing test** that captures the bug (`test-driven-development`).
4. **Fix at the narrowest layer.** Do not clean up nearby code.
5. **Run the full test suite**, then `verification-before-completion`.
6. **Ship:** [Review and PR](#review-and-pr).

Prompt:
> Use diagnosing-bugs. Symptom: <what>. Repro: <how>. Do not edit until you show evidence for the cause.

Harness notes: on Pi without a subagent extension, keep the log reading in the main thread and let RTK trim output. With the extension, delegate log reading to a subagent. Done when the new test fails before the fix and passes after.

---

## New feature

Goal: agree on the design first, then build it test-first.

1. **Align.** `grill-with-docs` with a repo (`grill-me` without). Output: decisions in `docs/adr/` and `CONTEXT.md`.
2. **Name things.** `domain-modeling` if terms are unclear.
3. **Plan.** `writing-plans`. Skip Superpowers `brainstorming`.
4. **Isolate** (optional, bigger work): `using-git-worktrees`.
5. **Build.** `test-driven-development`, one small step at a time.
6. **Verify.** `verification-before-completion`.
7. **Ship:** [Review and PR](#review-and-pr).

Turn Caveman on from step 3. Keep it off for steps 1 and 2.

Prompt:
> Use grill-with-docs. Feature: <what>. Constraints: <list>. Ask me one question at a time.

Harness notes: CC can run independent plan tasks through `subagent-driven-development`. OC can too. Pi can too once the subagent extension is installed. Without it, Pi runs the plan task by task in one thread (`executing-plans`). Done when plan tasks are checked off, tests pass and ADRs are written.

---

## Kubernetes manifest

Goal: a manifest that validates, shows a clean diff and reaches the cluster only through a PR.

No skill in this toolset covers Kubernetes. The safety comes from rules in your instructions file plus validation commands. Put this block in `AGENTS.md` (see [setup.md](setup.md) for how Claude Code reads it):

```markdown
## Kubernetes / GitOps
- Never run `kubectl apply`, `helm upgrade` or `kubectl delete` against a cluster. Changes go through a PR.
- Validate every manifest before saying it is done:
  `kubeconform -strict -summary <file>`, `helm lint <chart>`, `kubectl diff --dry-run=server -f <file>`.
- Set resource requests and limits, probes and a non-root securityContext unless told otherwise.
- Pin image tags or digests. No `latest`.
```

Steps:
1. **Understand the target.** Read neighbors in the repo: naming, labels, namespace, kustomize or Helm layout. Copy the convention, do not invent one.
2. **Design the unusual part.** New service or risky change: `grill-with-docs` (ingress, secrets, storage, rollout).
3. **Write the manifest.**
4. **Validate** with the commands above. Treat failures like failing tests: fix, rerun.
5. **Review** with `code-review`. Check selectors match labels, ports match, secrets are not inline.
6. **Ship** by PR (`pr`). The pipeline applies it.

Prompt:
> Add a Deployment and Service for <app> following the layout in <path>. Do not touch the cluster. Run kubeconform and helm lint, show the output.

Harness notes: `kubectl diff --dry-run=server` needs cluster access. Without it, say so and stop at `kubeconform` rather than guessing. Done when validators exit 0 and you pasted their output.

---

## Architecture exploration

Goal: a correct mental model of unfamiliar code, with file references.

1. **Orient cheaply.** CC: `caveman-explore` (read-only, returns `path:line`, keeps reads out of main context) or the built-in Explore subagent. OC and Pi: ask the agent to map directories and entry points only, no edits.
2. **Trace one flow end to end** (request in, result out). Ask for `path:line` for every claim.
3. **Find weak spots.** `improve-codebase-architecture` scans for deepening opportunities and builds an HTML report, then grills you on the one you choose. `codebase-design` gives the vocabulary.
4. **Record what you learned.** `domain-modeling` writes terms and ADRs. Draw it with [Diagram](#diagram).

Prompt:
> Map this repo: entry points, main modules, data flow. Read only. Cite path:line for each claim. Say what you could not confirm.

Harness notes: on Pi, use the subagent extension for the exploration so reads stay out of the main context. Without it, run the exploration in a fresh session. Done when every claim has a file reference and unknowns are listed, not guessed.

---

## Diagram

Goal: a diagram that matches the code, as a single HTML file you open in a browser.

No skill in this toolset draws diagrams. The agent writes the HTML itself, so the prompt carries the rules. The method works the same on Claude Code, OpenCode and Pi.

1. **Read first.** Run [Architecture exploration](#architecture-exploration) on the part you draw. Never draw from memory.
2. **Pick the form.** Components and flow: boxes and arrows. Request sequence: lifelines with numbered steps. Data model: tables with relation lines. States: nodes with labeled transitions.
3. **Draw one idea per diagram.** About 10 nodes max. Split larger views into separate files or sections.
4. **Write one self-contained `.html` file.** Inline SVG (or HTML and CSS), inline styles, no build step, no external scripts or fonts. It must open from disk and work offline.
5. **Make it readable.** Short labels, arrows with direction, a legend if colors carry meaning, readable in light and dark mode, no horizontal page scroll on a laptop.
6. **Tie it to the code.** Put the real name (service, function, table) in each box. Add the source `path:line` as a tooltip (`<title>` inside the SVG element) or a small caption.
7. **Check it.** Open the file in a browser and confirm it renders. Where the harness has a browser tool, ask the agent to screenshot it. Check each label against the code.
8. **Keep it near the code:** `docs/diagrams/<name>.html`, linked from the ADR or README it explains.

Prompt:
> Draw a diagram of <flow> as one self-contained HTML file with inline SVG, no external scripts. Read the code first and use real names. Put the source path:line of each box in its tooltip. Save it as docs/diagrams/<name>.html and tell me how you checked it renders.

Harness notes: CC can also publish the page as an artifact when you want to share it, and has Excalidraw tools for freehand drawing. OC and Pi write the file and you open it yourself. Plain HTML diffs as text, so changes still show up in review. Done when the file opens, renders and a teammate can match every box to code.

Reference example: [docs/diagrams/harness-bench-run-flow.html](docs/diagrams/harness-bench-run-flow.html). Open it in a browser. It follows these rules: one idea, real function names, `path:line` in tooltips, light and dark mode, no external assets.

---

## Refactor

Goal: change structure, not behavior.

1. **Pin behavior** with tests. Missing coverage: add tests first (`test-driven-development`).
2. **Choose the shape** with `codebase-design`. Big redesign: `grill-with-docs` first.
3. **Move in small steps.** Run tests after each.
4. **Review** with `code-review`.

Done when tests pass unchanged and the diff shows no behavior edits.

---

## Review and PR

1. **Review.** `code-review` against the base branch. Superpowers `requesting-code-review` is the alternative. Pick one.
2. **Handle feedback** with `receiving-code-review`: verify each point before applying it.
3. **Verify.** `verification-before-completion`.
4. **PR body** with `pr`. Commit with `caveman-commit` if you use Caveman.

Write commits and PR text in normal prose. People read them.

---

## Migration or dependency upgrade

1. **Research the breaking changes** ([Research](#research)). Read the changelog, not memory.
2. **Pin current behavior** with tests.
3. **Plan in steps** (`writing-plans`) that keep the build green after each one.
4. **Upgrade one thing at a time.** Run tests after each.
5. **Keep a rollback.** One commit per step makes revert easy.

Done when tests pass on the new version and the old version still builds from the previous commit.

---

## Large work

Too big for one session: `wayfinder` splits it into a map of decision tickets on your issue tracker. Resolve one ticket per session. Use `handoff` to pass the state to a fresh agent. Run `setup-matt-pocock-skills` once so the tracker is configured.

---

## Research

Use `research` for facts from primary sources. It saves a Markdown file in the repo. Ask for source URLs and the date checked. Keep the file only if the team will reuse it.

---

## Incident or live failure

1. **Read-only first.** Logs, `kubectl get`, `kubectl describe`. No writes.
2. **Rank causes with evidence** (`diagnosing-bugs`).
3. **Propose the fix as a PR.** Do not patch the cluster by hand (see the Kubernetes rules above).
4. **Write it down.** `retro` after the session, ADR if a decision came out of it.

---

## Tips that apply everywhere

- Start a new session per task. Context from the last task misleads the next.
- Ask for evidence: file and line, command output, test result.
- RTK runs in the background. Check it with `rtk gain`.
- Caveman: on for execution, off for design and teaching.
- On Pi, check that a subagent extension is installed before you start a scenario that delegates.
- If a skill seems missing, run `/skills` (CC) or list the skills folder (OC, Pi), then name the skill in your prompt.
