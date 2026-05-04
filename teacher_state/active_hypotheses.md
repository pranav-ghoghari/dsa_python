# Active Hypotheses

## Hypothesis 1

The student can now write small functions from scratch when requirements are concrete and tests are available.

Would confirm:

- The next fresh task starts with a valid loop/condition/return structure without scaffolded code.
- Review focuses on edge cases or cleanup rather than basic syntax survival.
- The student can name and fix a loop-control bug in their own first draft without needing the corrected code supplied.
- The student transfers the retryable-job pattern into a new output shape and only needs a tiny correction such as a key-name typo.
- The student can also turn that finished function into a small formal test file without needing the assertions provided.
- The student can revise that file to add a missing branch case and keep it passing.
- The student can run the unittest command and interpret the main output lines meaningfully.
- The student can write one fresh small function and one fresh matching test file from a blank page.
- The student can finish a test-maintenance cycle after a failing assertion caused by stale expected output.
- The student can explain why numeric IDs must be converted to strings before using `join()`.
- The student can explain why empty input leaves a counting dictionary unchanged.
- The student can strengthen a passing implementation by noticing when a requirement is not really enforced by the current tests.
- The student can shift from counting categories into grouping values under those categories without stalling.

Would disconfirm:

- A similarly sized task still stalls at the blank-page or syntax stage.

## Hypothesis 2

The main remaining gap is proactive edge-case handling, not basic control-flow construction.

Would confirm:

- The student solves the happy path quickly but misses optional keys, blank inputs, or exact formatting.
- A single edge-case reminder is enough to finish the task.
- The student reaches for `dict.get(...)` without prompting but still needs one reminder about guarding numeric comparisons and not returning too early.
- On the next fresh task, the student handles exact output formatting carefully instead of only getting the filtering logic right.
- The next formatting task works even when the reported values start as integers rather than strings.
- The next fresh task can change from filtering/reporting to dictionary accumulation without stalling.
- The next fresh task can build a formatted report from accumulated dictionary counts without stalling.
- The next fresh task can change from counting into grouping values into dictionary lists without stalling.
- The student can initialize grouped-list buckets on first use and preserve per-group order with `append(...)`.

Would disconfirm:

- The next task reveals trouble building even the basic loop or conditional skeleton.

## Hypothesis 3

Short, single-task cycles reduce passivity and improve output quality.

Would confirm:

- Narrow assignments keep the student attempting code and using tests without prolonged drift.
- "Exactly one next task" continues to produce follow-through.
- After writing a test file, the student can also read the command output meaningfully instead of treating the runner as a black box.
- The next narrow task can combine one new function and one new test file without causing stall.
- The student can then strengthen one incomplete edge-case test instead of treating "all green" as the end of thinking.

Would disconfirm:

- Even with one narrow task, the student avoids writing code or loses momentum quickly.

## Hypothesis 4

Comment-first planning helps only when it turns into code quickly.

Would confirm:

- Brief `#` comments lead directly into executable lines on the next attempt.

Would disconfirm:

- Comments become a substitute for coding or introduce more confusion than structure.
