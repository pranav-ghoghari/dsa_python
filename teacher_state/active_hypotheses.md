# Active Hypotheses

## Hypothesis 1

The student can now write small functions from scratch when requirements are concrete and tests are available.

Would confirm:

- The next fresh task starts with a valid loop/condition/return structure without scaffolded code.
- Review focuses on edge cases or cleanup rather than basic syntax survival.
- The student can name and fix a loop-control bug in their own first draft without needing the corrected code supplied.
- The student transfers the retryable-job pattern into a new output shape and only needs a tiny correction such as a key-name typo.
- The student can also turn that finished function into a small formal test file without needing the assertions provided.

Would disconfirm:

- A similarly sized task still stalls at the blank-page or syntax stage.

## Hypothesis 2

The main remaining gap is proactive edge-case handling, not basic control-flow construction.

Would confirm:

- The student solves the happy path quickly but misses optional keys, blank inputs, or exact formatting.
- A single edge-case reminder is enough to finish the task.
- The student reaches for `dict.get(...)` without prompting but still needs one reminder about guarding numeric comparisons and not returning too early.

Would disconfirm:

- The next task reveals trouble building even the basic loop or conditional skeleton.

## Hypothesis 3

Short, single-task cycles reduce passivity and improve output quality.

Would confirm:

- Narrow assignments keep the student attempting code and using tests without prolonged drift.
- "Exactly one next task" continues to produce follow-through.

Would disconfirm:

- Even with one narrow task, the student avoids writing code or loses momentum quickly.

## Hypothesis 4

Comment-first planning helps only when it turns into code quickly.

Would confirm:

- Brief `#` comments lead directly into executable lines on the next attempt.

Would disconfirm:

- Comments become a substitute for coding or introduce more confusion than structure.
