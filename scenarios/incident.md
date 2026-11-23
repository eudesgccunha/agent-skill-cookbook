# Incident or live failure

> Last verified: 2026-11-23 · Level: read · Basis: written from the skill texts and docs; the scenario was not run end to end

[All scenarios](README.md)

1. **Read-only first.** Logs, `kubectl get`, `kubectl describe`. No writes.
2. **Rank causes with evidence** (`diagnosing-bugs`).
3. **Propose the fix as a PR.** Do not patch the cluster by hand (see the Kubernetes rules above).
4. **Write it down.** `retro` after the session, ADR if a decision came out of it.
