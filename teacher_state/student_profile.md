# Student Profile

## Current Summary

- Early 2026-04-05 evidence showed partial conceptual understanding but weak Python syntax fluency and weak debugging vocabulary.
- By 2026-04-06 the student completed the baseline assessment and all 15 baseline tests passed.
- On 2026-04-07 the student completed a fresh `failed_jobs.py` exercise after one targeted correction around missing-key handling.
- Later on 2026-04-07 the student drafted `count_retryable_jobs(...)` from scratch with the right loop/counter structure and proactive `dict.get(...)`, then correctly recognized that `else: return 0` would wrongly break out of the loop.
- The student has now completed `count_retryable_jobs(...)` with safe missing-key handling and the correct `retries_left > 0` filter.
- This gives stronger evidence that the student can finish a small debugging cycle after targeted feedback without being handed the full solution.
- The student also completed a fresh transfer task, `collect_retryable_job_ids(...)`, after correcting one tiny key-name typo and could explain why output order is preserved.
- The student then completed a fresh function-plus-test pair, `collect_active_usernames(...)` and `test_collect_active_usernames.py`, including a follow-up test revision after one failing assertion.
- The student has now also completed `build_active_user_report(...)` and its focused tests after switching from manual comma-building to `", ".join(...)`.
- The student has now also completed `count_jobs_by_status(...)` and its focused tests, showing a fresh dictionary-accumulation success.
- The student has now also written `build_status_summary(...)` and its tests, and the current focused test run passes.
- The student tightened `build_status_summary(...)` to enforce alphabetical sorting explicitly rather than relying on insertion order.
- The student has now also completed `group_job_ids_by_status(...)` and its focused tests, showing a fresh grouped-dictionary success.

## Strengths

- Can infer business intent from function names, docstrings, and tests.
- Can decompose small concrete tasks into plausible steps before coding.
- Can now produce working Python for baseline-sized functions.
- Can write a first draft for a small dictionary-filtering task without needing a starter body.
- Improves quickly when feedback points to one exact mismatch.
- Can transfer a recently learned filter pattern into a new list-building function on the first draft, with only one small key-name mistake.
- Can explain why list order is preserved when iterating left-to-right and appending matching items.
- Can revise a beginner `unittest` file to add a missing branch case after targeted feedback.
- Can now produce a fresh small function and matching unittest file from a blank page without needing the assertions written for them.
- Can use one failing assertion caused by stale expected output to finish a test-maintenance cycle.
- Can apply the `append()` then `", ".join(...)` pattern to produce exact comma-separated output without a trailing separator.
- Can explain why `join()` avoids a trailing comma and why the empty case still needs its own branch.
- Can transfer that pattern to numeric IDs by converting them to strings before joining.
- Can explain why `join()` fails on integers and why converting each integer with `str(...)` fixes it.
- Can write and test a small dictionary-counting function using `dict.get(key, 0) + 1`.
- Can explain the main role of `dict.get(key, 0) + 1`: default-to-zero then increment.
- Can explain why empty input returns `{}` in a dictionary-counting function: the loop never runs, so the accumulator stays empty.
- Can now revise both implementation and tests to enforce a missing requirement that earlier tests failed to prove.
- Can now build a dictionary whose values are lists, including first-seen key initialization and ordered `append(...)` grouping.

## Current Limits

- Edge-case handling is improving on small tasks, including skipping dictionaries with missing keys instead of crashing.
- Loop control is improving, and the student has now avoided the premature `return` from the earlier draft.
- Exact output requirements still benefit from close rereading, but this task now shows the student can correct an omitted condition after feedback.
- Syntax is functional but not yet consistently clean or idiomatic under pressure.
- Fresh-transfer drafts can still contain tiny string-literal slips such as an extra space inside a dictionary key name.
- Independent debugging on unfamiliar failures is less proven than debugging with nearby tests and focused review.
- There is less evidence so far for writing formal tests from scratch than for writing the functions themselves.
- Formal testing vocabulary and structure are not yet established: `unittest`, classes, `self`, assertion methods, and cross-file imports still need explicit teaching.
- After the `unittest` lesson, the student now understands the broad purpose of imports, `unittest`, `TestCase`, test discovery by `test_` naming, and why test methods return `None`.
- The remaining gap is mostly precision, not the big picture: `self` still needs to be understood as the current instance of the student's test class, not literally the `unittest.TestCase` class itself.
- The student can now run a unittest command and mostly interpret the output lines correctly, with only minor precision gaps around the module path in the command itself.
- There is still limited evidence for writing a new function-and-test pair from a blank page without leaning on a nearby example.
- Test coverage can still under-specify an "either key missing" rule by proving only one of the missing-key branches.
- When revising a test to cover an extra edge case, the expected output can lag behind the edited input data.
- Exact string formatting on fresh tasks is still less proven than list or count outputs.
- Exact string formatting is improving, but transfer of that pattern to slightly different output types is still less proven.
- The repeated filter/list/report pattern is now relatively strong.
- Dictionary accumulation now has one fresh success, and the student has explained the counting pattern back in plain English.
- The next useful transfer is to turn those counts into a formatted multi-line report.
- Multi-line report formatting from a count dictionary is now a demonstrated strength, including explicit alphabetical sorting.
- Grouping into dictionary lists is now demonstrated and has now also been explained back in plain English at a beginner but workable level.
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
- The broad purpose of a test file and the idea that `assertEqual` checks actual versus expected output.
- Why `unittest` looks for `test_` methods and why `actual`/`expected` belong inside the test body instead of the parameter list.
- Why an explicit empty-input test belongs in the current test file.
- The broad meaning of `test_name ... ok`, `Ran 4 tests`, and `OK` in unittest output.
- The overall purpose and basic shape of a fresh unittest file written for a new function.
- Why a trailing comma can appear when a string is built by repeated `+= name + ", "`.
- Why `", ".join(list_of_names)` avoids a trailing separator.
- Why the empty case still needs a separate branch instead of relying on `join()` alone.
- Why `", ".join(...)` needs strings and not raw integers.
- Why `str(i)` is needed before joining numeric IDs into one string.
- Why `dict.get(status, 0) + 1` is used when counting statuses.
- Why empty input returns `{}` because the count dictionary starts empty and the loop does not execute.
- Why grouping uses lists instead of counts, why the first-seen key needs an empty list, and why left-to-right `append(...)` preserves per-group order.

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
- A working first `unittest` test file by adapting the taught pattern, even though the surrounding class/self mechanics are still only partly understood.
- A working first `unittest` test file plus a mostly correct plain-English explanation of how the structure works.
- A revised `unittest` file that now includes the missing empty-input case and passes when run.
- A passing unittest command run plus a mostly correct interpretation of the output summary.
- A fresh passing function-plus-test pair for filtering active usernames.
- A passing revision after aligning edited test data with the expected output.
- A fresh passing function-plus-test pair for exact comma-separated string formatting.
- A fresh passing function-plus-test pair that formats numeric IDs correctly by converting them to strings before joining.
- A fresh passing function-plus-test pair for counting jobs by status with a dictionary.
- A fresh passing function-plus-test pair for a sorted multi-line status summary.
- A fresh passing function-plus-test pair for grouping job IDs into lists by status.

### Can Debug

- Narrow syntax and logic issues after running tests or receiving one precise correction target.
- Missing-key handling with `dict.get(...)` once the issue is made explicit.
- Premature return behavior inside a loop once the risk is pointed out.
- A revised draft that fixes the crash path but still under-filters because one requirement was omitted.
- Completion of a small follow-up debugging cycle after narrowing feedback to one missing condition.
- Plain-English explanation of the final loop behavior after finishing the coding task.

## Confidence Level

- Strong for the recent evidence that the student can complete small Python tasks and match them with focused unittest files.
- Medium for independent debugging, proactive edge-case design on the first draft, and code quality without nearby scaffolding.
