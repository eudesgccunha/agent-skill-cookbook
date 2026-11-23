# Incident or live failure

[All scenarios](README.md)

1. **Read-only first.** Logs, `kubectl get`, `kubectl describe`. No writes.
2. **Rank causes with evidence** (`diagnosing-bugs`).
3. **Propose the fix as a PR.** Do not patch the cluster by hand (see the Kubernetes rules above).
4. **Write it down.** `retro` after the session, ADR if a decision came out of it.
