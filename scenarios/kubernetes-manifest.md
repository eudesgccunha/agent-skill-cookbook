# Kubernetes manifest

[All scenarios](README.md)

Goal: a manifest that validates, shows a clean diff and reaches the cluster only through a PR.

No skill in this toolset covers Kubernetes. The safety comes from rules in your instructions file plus validation commands. Put this block in `AGENTS.md` (see [getting-started/setup.md](../getting-started/setup.md) for how Claude Code reads it):

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
