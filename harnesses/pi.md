# Pi

Pi is minimal by design. These extensions fill the gaps. Back to [harnesses](README.md).

## Pi: install a subagent extension

Pi has no built-in subagents. Several skills and scenarios in this cookbook delegate work to subagents (`subagent-driven-development`, `dispatching-parallel-agents`, `cavecrew`, the exploration step in [scenarios/README.md](../scenarios/README.md)). **On Pi, install a subagent extension before you rely on them.** Without it, run everything in one thread.

Use `pi-subagents` by nicopreme, from the pi.dev packages tab:

```bash
pi install npm:pi-subagents
```

- Needs Pi 1.2.0 or newer (listing: version 0.70.1, MIT, November 2026).
- Several forks with similar names exist on pi.dev (for example `@whynothugo/pi-subagents`, `@piotr-oles/pi-subagents`). Install the unscoped `pi-subagents` and confirm the author on its page.
- Run `/subagents-doctor` after install to check the setup.
- Do not install a second subagent extension next to it. The tools can clash.

Pi packages run code and shape agent behavior. Read the package source before you install it. Check the package page for the current version, because the listing changes.

Verify after install:
1. Restart Pi. The startup header lists loaded extensions and skills.
2. Run `/subagents-doctor`.
3. Ask: "Use a subagent to list the top-level folders of this repo." The agent should call the subagent tool.
4. Manage what loads with `pi config`.

## Pi: recommended extension set

Three extensions cover the usual Pi setup: subagents, Cursor models and a LiteLLM gateway.

| Extension | What it adds | Install |
|---|---|---|
| `pi-subagents` (nicopreme) | Subagents for delegation (required, see above) | `pi install npm:pi-subagents` |
| `pi-cursor-sdk` | Cursor models inside Pi through the local `@cursor/sdk` runtime, for example `cursor/grok-4.6` | `pi install npm:pi-cursor-sdk` |
| `pi-provider-litellm` | Models from a LiteLLM proxy, registered as Pi providers. Adds `/login litellm` and `/litellm-refresh` | `pi install npm:pi-provider-litellm` |

Requirements and gotchas, from the package pages (November 2026, not tested here):

- **`pi-cursor-sdk`:** needs Node.js 24 or newer and Pi 0.87.1 or newer. It needs a Cursor **user key or service-account key** for the SDK. Cursor Desktop and Agent CLI logins do not provide that key. It creates a fresh Cursor agent for each provider call. Keep the key in an environment variable, never in a committed file.
- **`pi-provider-litellm`:** needs Pi 0.99.2 or newer. On older Pi, install `pi-provider-litellm@3.4.0`. It discovers models from the proxy, so run `/litellm-refresh` after you add a model on the proxy. It can also expose LiteLLM MCP tools and inject skills from the LiteLLM Skills Gateway, so check what the gateway sends before you trust it.
- **Cost tracking:** with LiteLLM in the path, spend appears in the proxy logs. Cursor models called through `pi-cursor-sdk` do not pass through your LiteLLM proxy, so their cost lives in Cursor instead. Keep the two apart when you compare.
- **Subagent models:** subagents run on whichever provider the extension uses. Pick a cheaper model for exploration subagents to save cost.
- **Trust:** all three run code inside Pi. Read the source before you install or update them, and pin versions when you can.

Check after install: restart Pi, read the startup header for the loaded extensions, run `/login litellm` or set the Cursor key, then start Pi with one model from each provider.
