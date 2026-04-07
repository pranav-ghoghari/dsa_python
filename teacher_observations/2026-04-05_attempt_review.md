# Attempt Review

Date: 2026-04-05

## Evidence From `interview.md`

- Variable: partial understanding, mostly correct.
- List vs dictionary: incomplete and partly incorrect.
  - The student mentioned repeated values versus unique values.
  - The missing precision is that dictionary keys are unique; values can repeat.
- Function parameter: broadly correct.
- `return`: broadly correct, but still described informally.
- `None`: guessed as similar to null, which is a useful starting point.
- Loop: broadly correct.
- `if`: broadly correct but too vague.
- Traceback: currently misunderstood.
- Unit test: partially understood as checking a small piece of code, but the purpose and structure are still unclear.

## Evidence From `normalize_username`

- The student wrote valid assignment syntax such as `username = raw_username.lower()`.
- The student used a correct Python string method: `.lower()`.
- The student tried to inspect whitespace with `.startswith(' ')` and `.endswith(' ')`.
- The student has not yet identified the right tool for removing edge whitespace.
- The student returned a partially transformed value.
- The student added a reflective comment explaining the reasoning struggle.
- The student's file still imports and runs, which means the attempt is executable Python rather than only pseudocode.
- Test results show the lowercase step works, while trimming and replacing internal spaces are still missing.
- The student expects terminal output from running a script even when the function containing `print(...)` is never called.
- The student can now chain multiple string methods in one expression.
- The student is attempting loops, conditionals, list building, and dictionary accumulation without waiting for the answer first.
- The student is transferring syntax habits from C++ into Python, especially around increment syntax and control-flow punctuation.
- The student currently uses triple-quoted strings as comments inside the file; this shows reasoning, but they are not the right comment form for this purpose.

## Important Teaching Interpretation

- This is useful progress.
- The student is not frozen at the blank-page stage anymore.
- The main issue is no longer "can they type any Python at all?"
- The current issue is "can they choose the right Python operation and combine steps into a correct result?"
- Another current gap is the execution model: defining a function versus actually calling it, and `return` versus `print`.
- A new concrete gap is Python syntax precision under pressure: quotes for dictionary keys, `:` after `if`, and no `++` operator in Python.

## Immediate Teaching Priority

- Teach `.strip()` next.
- Then teach how to replace runs of spaces in the middle.
- Keep the scope to one function until the student gets a full win.
- Explicitly teach why running a Python file with only definitions often prints nothing.
- Teach the difference between real comments (`#`) and standalone string literals.
