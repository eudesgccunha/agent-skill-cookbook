# Refactor

1. **Pin behavior.** Make sure tests cover what must not change. Add them first with `tdd` if missing.
2. **Shape the target.** Use `codebase-design` to decide module interfaces and seams.
3. **Move in small steps.** Run the tests after each step.
4. **Review the diff** with `code-review`.

If the refactor changes domain terms, update the glossary with `domain-modeling`.
