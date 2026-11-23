# Diagram

> Last verified: 2026-11-23 · Level: read · Basis: written from the skill texts and docs; the scenario was not run end to end

[All scenarios](README.md)

Goal: a diagram that matches the code, as a single HTML file you open in a browser.

No skill in this toolset draws diagrams. The agent writes the HTML itself, so the prompt carries the rules. The method works the same on Claude Code, OpenCode and Pi.

1. **Read first.** Run [Architecture exploration](architecture-exploration.md) on the part you draw. Never draw from memory.
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

Reference example: [examples/diagrams/harness-bench-run-flow.html](../examples/diagrams/harness-bench-run-flow.html). Open it in a browser. It follows these rules: one idea, real function names, `path:line` in tooltips, light and dark mode, no external assets.
