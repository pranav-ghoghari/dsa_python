# Student Profile

## Current Summary

- Early 2026-04-05 evidence showed partial conceptual understanding but weak Python syntax fluency and weak debugging vocabulary.
- By 2026-04-06 the student completed the baseline assessment and all 15 baseline tests passed.
- On 2026-04-07 the student completed a fresh `failed_jobs.py` exercise after one targeted correction around missing-key handling.
- Later on 2026-04-07 the student drafted `count_retryable_jobs(...)` from scratch with the right loop/counter structure and proactive `dict.get(...)`, then correctly recognized that `else: return 0` would wrongly break out of the loop.
- The student has now completed `count_retryable_jobs(...)` with safe missing-key handling and the correct `retries_left > 0` filter.
- This gives stronger evidence that the student can finish a small debugging cycle after targeted feedback without being handed the full solution.
- The student also completed a fresh transfer task, `collect_retryable_job_ids(...)`, after correcting one tiny key-name typo and could explain why output order is preserved.

## Strengths

- Can infer business intent from function names, docstrings, and tests.
- Can decompose small concrete tasks into plausible steps before coding.
- Can now produce working Python for baseline-sized functions.
- Can write a first draft for a small dictionary-filtering task without needing a starter body.
- Improves quickly when feedback points to one exact mismatch.
- Can transfer a recently learned filter pattern into a new list-building function on the first draft, with only one small key-name mistake.
- Can explain why list order is preserved when iterating left-to-right and appending matching items.

## Current Limits

- Edge-case handling is improving on small tasks, including skipping dictionaries with missing keys instead of crashing.
- Loop control is improving, and the student has now avoided the premature `return` from the earlier draft.
- Exact output requirements still benefit from close rereading, but this task now shows the student can correct an omitted condition after feedback.
- Syntax is functional but not yet consistently clean or idiomatic under pressure.
- Fresh-transfer drafts can still contain tiny string-literal slips such as an extra space inside a dictionary key name.
- Independent debugging on unfamiliar failures is less proven than debugging with nearby tests and focused review.
- There is less evidence so far for writing formal tests from scratch than for writing the functions themselves.
- Formal testing vocabulary and structure are not yet established: `unittest`, classes, `self`, assertion methods, and cross-file imports still need explicit teaching.
- There is not yet enough evidence for larger or more abstract tasks.

## Current Separation

### Can Explain

- The broad role of variables, loops, `if`, parameters, and return values.
- The intended behavior of small business-like functions.
- Why `return 0` inside this loop would end the function instead of skipping one job.
- The guard-and-count logic in `count_retryable_jobs(...)`, including why missing-key jobs are skipped and why the total is returned only after the loop.
- Why a failed job with `retries_left == 0` is skipped by the inner value check.
- Small comment-based test examples for the function, though expected outputs still need one correction pass.
- Why `collect_retryable_job_ids(...)` preserves input order.

### Can Recognize

- Likely transformation steps from docstrings and tests.
- Common tool families such as string methods, loops, counters, and dictionary aggregation.

### Can Write Unaided

- Small functions with loops, counters, list building, dictionary accumulation, and basic string parsing when the task is concrete.
- Happy-path logic for small dictionary-based tasks.
- Combined boolean checks over dictionary fields in a first draft.
- The first pass of missing-key-aware dictionary access using `dict.get(...)`.
- Safe key-existence guards before direct dictionary indexing.
- Small dictionary-filtering logic that combines key checks, equality checks, numeric comparisons, and counting.
- The same filter logic transferred into list building with preserved order.

### Can Debug

- Narrow syntax and logic issues after running tests or receiving one precise correction target.
- Missing-key handling with `dict.get(...)` once the issue is made explicit.
- Premature return behavior inside a loop once the risk is pointed out.
- A revised draft that fixes the crash path but still under-filters because one requirement was omitted.
- Completion of a small follow-up debugging cycle after narrowing feedback to one missing condition.
- Plain-English explanation of the final loop behavior after finishing the coding task.

## Confidence Level

- Strong for the recent evidence that the student can complete small Python tasks.
- Medium for independent debugging, proactive edge-case design on the first draft, and code quality without nearby scaffolding.
