# Cutting token cost

| Lever | Saves | Use when |
|---|---|---|
| RTK | Input tokens from command output | Always on |
| Caveman | Output tokens | Execution phases. Off for design and teaching |
| `caveman-compress` | Input tokens from memory files | `CLAUDE.md` or notes grow large |
| `cavecrew` subagents | Main-context tokens | Locating code, small edits, diff review |
| `caveman-stats` | Nothing, it measures | Check real usage in a session |

Check RTK with `rtk gain`.

Ponytail is a different lever: it cuts code the agent writes, not tokens. See [skills.md](../skills.md#ponytail-optional).
