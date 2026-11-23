# Bug fix

1. **Reproduce and rank causes.** Run `diagnosing-bugs` for unknown, intermittent or slow failures. For an obvious bug, skip to step 3.
2. **Confirm the cause with evidence** before editing anything.
3. **Write a failing test** (Superpowers `test-driven-development`, or Pocock `tdd`).
4. **Fix at the narrowest layer.** Keep surrounding behavior unchanged.
5. **Run the test suite.**

Use either `diagnosing-bugs` (Pocock) or Superpowers `systematic-debugging` in one session, not both.
