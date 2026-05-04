# Teacher State Log

## [2026-04-07] migration | initialized persistent teacher wiki

- Renamed `AGENT.md` to `AGENTS.md` and rewrote it as the top-level operating manual for the three-layer architecture.
- Created `teacher_state/` with canonical state pages, a README, index, lint checklist, and append-only log.
- Added local `AGENTS.md` files for `python_baseline/`, `teacher_observations/`, and `teacher_state/`.
- Revised the root README and directory READMEs to reflect the persistent teaching-memory workflow.

## [2026-04-07] migration | reorganized historical evidence

- Created `teacher_observations/sessions/`.
- Moved the dated observation files into `teacher_observations/sessions/`.
- Kept session notes as historical evidence instead of treating them as canonical state.

## [2026-04-07] synthesis | seeded canonical student model from existing evidence

- Synthesized `teacher_state/` from `python_baseline/interview.md`, `python_baseline/assessment.py`, `python_baseline/failed_jobs.py`, baseline tests, and the dated session notes.
- Resolved the early 2026-04-05 assumption of "cannot complete any coding task" in favor of newer 2026-04-06 and 2026-04-07 evidence showing baseline completion and a passing write-from-scratch follow-up task.
- Preserved uncertainty around independent debugging on novel failures, proactive edge-case handling, and code-quality fluency without nearby scaffolding.

## [2026-04-07] lint | checked migration coherence

- Verified that raw evidence, canonical state, and schema layers are now separate.
- Verified that `next_task.md` contains exactly one task and that session notes are no longer the sole source of current truth.
- Verified that no baseline solutions were added to assessment materials during the migration.

## [2026-04-07] ingest | reviewed retryable jobs first draft

- Reviewed the student's first draft of `count_retryable_jobs(...)` in `python_baseline/failed_jobs.py`.
- Updated the canonical state to reflect stronger unaided drafting: correct loop/counter shape and proactive `dict.get(...)` use on a fresh task.
- Kept the main open gap focused on loop control and incomplete missing-key guarding after the draft returned `0` too early and still risked a missing-`retries_left` failure.

## [2026-04-07] ingest | retryable jobs follow-up question narrowed the gap

- The student explicitly recognized that `else: return 0` would break out of the loop instead of skipping one non-matching job.
- Updated the canonical state to reflect stronger control-flow reasoning in explanation, while keeping missing numeric-key guarding as the active syntax/debugging target.

## [2026-04-07] ingest | retryable jobs revision fixed safety but missed one filter

- Reviewed the revised `count_retryable_jobs(...)` draft in `python_baseline/failed_jobs.py`.
- The student now safely checks for both keys before direct indexing and no longer exits the loop early.
- The remaining gap is requirement completeness: the code counts failed jobs even when `retries_left` is `0` or negative because it only checks key presence.

## [2026-04-07] ingest | retryable jobs exercise completed

- Reviewed the latest `count_retryable_jobs(...)` revision in `python_baseline/failed_jobs.py`.
- The student now correctly combines key checks, `status == "failed"`, and `retries_left > 0` inside the loop.
- Updated the next task from code correction to explaining the finished logic in plain English.

## [2026-04-07] ingest | student explained loop and return behavior

- The student explained that missing-key jobs are skipped because the outer key-check fails and the loop moves to the next iteration.
- The student also explained that `count` accumulates across iterations and `return count` comes only after the loop finishes.
- The remaining explanation target is the value-check distinction: why `retries_left == 0` is not counted.

## [2026-04-07] ingest | student completed the explanation of the numeric filter

- The student explained that a failed job with `retries_left == 0` is skipped because it does not satisfy the inner `> 0` check.
- Updated the next task from explanation to writing small concrete test cases for the finished function.

## [2026-04-07] ingest | student drafted comment-based test cases

- The student wrote three example cases as comments directly in `python_baseline/failed_jobs.py`.
- The cases target the right branches, but one expected outcome is still mixed up: a job missing `retries_left` should be skipped, not counted.

## [2026-04-07] ingest | comment-based test cases partly corrected

- The student revised the comment-based examples to include explicit expected outputs.
- Two cases are now aligned with the function behavior, but the prose for the missing-key case still says "should count" while the expected value correctly says `0`.

## [2026-04-07] ingest | moved on after comment-based case practice

- The student chose to stop iterating on the comment-based examples and move to the next task.
- Updated `next_task.md` from same-function example writing to a fresh list-building function that reuses the same retryable-job logic.

## [2026-04-07] ingest | clarified post-task cleanup policy

- The student asked whether finished files like `assessment.py` and `failed_jobs.py` should be cleared after a task ends.
- Preserved the repo's evidence-first rule: completed exercise files stay in place, while cleanup focuses on stale tests, stale references, and current teacher-state updates.
- Updated top-level and baseline `AGENTS.md` files plus the READMEs to make this post-task cleanup policy explicit.

## [2026-04-07] lint | cleaned stale retryable-jobs test

- Updated `tests/test_failed_jobs.py` to target `count_retryable_jobs(...)` instead of the old `count_failed_jobs(...)` name and behavior.
- This keeps the repo cleaner without deleting finished student work.

## [2026-04-07] ingest | first draft of retryable job id collector

- Reviewed the first draft of `collect_retryable_job_ids(...)` in `python_baseline/collect_retryable_job_ids.py`.
- The student transferred the loop, guard, and value-filter pattern correctly into a list-building task.
- The only observed bug is a key-name typo in the guard: `"id "` instead of `"id"`.

## [2026-04-07] ingest | retryable job id collector completed

- The student corrected the key-name typo in `collect_retryable_job_ids(...)` and correctly explained why the function preserves input order.
- Updated `next_task.md` from function-writing to writing a small formal test file for the finished function.

## [2026-04-07] ingest | clarified prerequisite explanations for new task types

- The student explicitly asked for fundamentals before being assigned a test-file task they may not already know how to structure.
- Updated the top-level instructions and teaching strategy to explain unfamiliar artifact types before asking for independent work.

## [2026-04-07] ingest | test-file prerequisites made explicit

- The student stated that `unittest`, `class`, `self`, `assertEqual`, and cross-file imports are not yet known concepts.
- Updated `next_task.md` from independent test writing to a fundamentals-first primer on test-file structure.

## [2026-04-07] migration | added student lesson layer

- Created `student_lessons/` with its own `AGENTS.md`, `README.md`, and `index.md`.
- Added reusable student-facing lesson files for dictionary guards and loop flow, list order with `append()`, and `unittest` basics.
- Updated the root `AGENTS.md` and `README.md` so the repo now explicitly tracks a student-facing lesson layer alongside teacher-state and historical observations.

## [2026-04-07] ingest | student requested durable lesson notes

- The student asked for a `student_lessons/` folder so taught concepts can be stored in markdown and reused later.
- Updated the teaching strategy and work-habits pages to reflect the preference for a reusable lesson shelf.
- Updated `next_task.md` so the immediate next move is to read `student_lessons/unittest_basics.md` and explain the core concepts back.

## [2026-04-07] ingest | first unittest explanation and test draft

- The student explained the broad purpose of imports, `unittest`, classes, `self`, and `assertEqual`, but still showed clear uncertainty about `TestCase`, test discovery, and why test methods use `self` with `-> None`.
- The student also wrote `tests/test_collect_retryable_job_ids.py` by adapting the lesson pattern.
- Ran `python -m unittest tests.test_collect_retryable_job_ids -v`; all 3 tests passed.
- Updated `student_lessons/unittest_basics.md` and `next_task.md` to focus on the remaining mechanics rather than repeating the already-understood basics.

## [2026-04-07] ingest | unittest mechanics explained back

- The student gave a mostly correct explanation of why tests inherit from `unittest.TestCase`, how `unittest` finds `test_` methods, why test methods use `-> None`, and why assertions live inside the method body.
- The only remaining precision gap is that `self` refers to the current instance of the student's test class, not literally the `unittest.TestCase` class object.
- Updated `next_task.md` from concept explanation to a small coverage revision in `tests/test_collect_retryable_job_ids.py`.

## [2026-04-07] ingest | collect_retryable_job_ids test coverage revised

- Reviewed the updated `tests/test_collect_retryable_job_ids.py`; it now includes the requested empty-input case and still keeps the other useful checks.
- Ran `python -m unittest tests.test_collect_retryable_job_ids -v`; all 4 tests passed.
- Updated `next_task.md` from test-file revision to interpreting unittest output lines.

## [2026-04-07] ingest | unittest output interpreted

- The student ran `python -m unittest tests.test_collect_retryable_job_ids -v` and gave a mostly correct explanation of the per-test `... ok` lines, `Ran 4 tests`, and `OK`.
- The only real precision gap was the command path: `tests.test_collect_retryable_job_ids` is the module path for one specific test file, not "all unittest modules from the tests folder."
- Updated `student_lessons/unittest_basics.md` with a short section on how to read the run command.
- Updated `next_task.md` from output interpretation to a fresh small function-plus-test pair.

## [2026-04-07] ingest | collect_active_usernames function-plus-test pair completed

- Reviewed `python_baseline/collect_active_username.py` and `tests/test_collect_active_usernames.py`.
- Ran `python -m unittest tests.test_collect_active_usernames -v`; all 3 tests passed.
- The student successfully produced a fresh small function and matching test file from a blank page.
- The remaining gap on this task is test completeness: the missing-keys test currently proves a missing `is_active` case but not a missing `username` case.

## [2026-04-07] ingest | collect_active_usernames missing-key test revised but still failing

- Reviewed the updated `tests/test_collect_active_usernames.py`; the missing-keys test now includes both a missing-`is_active` record and a missing-`username` record.
- Ran `python -m unittest tests.test_collect_active_usernames -v`; `test_missing_keys` failed because the expected list still included `"nishi"` even though no valid `"nishi"` record remains in that test input.
- Updated `next_task.md` to the exact remaining fix: align the expected output with the edited input data.

## [2026-04-07] ingest | collect_active_usernames test fix completed

- Rechecked `tests/test_collect_active_usernames.py` after the expected output was corrected.
- Ran `python -m unittest tests.test_collect_active_usernames -v`; all 3 tests passed.
- Updated `next_task.md` from test-fix cleanup to a fresh string-formatting function plus test file.

## [2026-04-07] ingest | build_active_user_report blocked on string join formatting

- Reviewed `python_baseline/build_active_user_report.py` and `tests/test_build_active_user_report.py`.
- Ran `python -m unittest tests.test_build_active_user_report -v`; the empty case passed, but the other two tests failed because the built string had a trailing `", "`.
- Added `student_lessons/joining_strings_for_reports.md` and updated the lesson index so the string-joining pattern is stored as reusable student-facing guidance.

## [2026-04-07] ingest | build_active_user_report completed

- Rechecked `python_baseline/build_active_user_report.py` after the switch to list collection plus `", ".join(...)`.
- Ran `python -m unittest tests.test_build_active_user_report -v`; all 3 tests passed.
- Updated `next_task.md` from finishing the code to explaining the `join()` formatting pattern in plain English.

## [2026-04-07] ingest | join pattern explained back

- The student correctly explained that repeated `+= name + ", "` leaves a trailing separator, that `", ".join(names)` fixes that, and that the empty case still needs a separate branch.
- Updated `student_lessons/index.md` to treat `joining_strings_for_reports.md` as a taught lesson rather than a current lesson.
- Updated `next_task.md` to a fresh formatting-transfer task using retryable job IDs.

## [2026-04-07] ingest | build_retryable_job_report completed

- Reviewed `python_baseline/build_retryable_job_report.py` and `tests/test_build_retryable_job_report.py`.
- Ran `python -m unittest tests.test_build_retryable_job_report -v`; all 4 tests passed.
- The student correctly transferred the filtering-plus-formatting pattern to numeric IDs by converting them to strings before `join()`.
- Updated `student_lessons/joining_strings_for_reports.md` and `next_task.md` so the immediate follow-up is explaining why `join()` needs strings.

## [2026-04-08] ingest | numeric join explanation completed

- The student correctly explained that `join()` does not work on raw integers and that converting each integer with `str(...)` before joining fixes the problem.
- Updated `next_task.md` from explanation to a fresh dictionary-accumulation task: `count_jobs_by_status(...)`.

## [2026-04-08] ingest | count_jobs_by_status completed

- Reviewed `python_baseline/count_jobs_by_status.py` and `tests/test_count_jobs_by_status.py`.
- Ran `python -m unittest tests.test_count_jobs_by_status -v`; all 3 tests passed.
- Added `student_lessons/counting_with_dictionaries.md` and updated the lesson index so the dictionary-counting pattern is stored as reusable guidance.
- Updated `next_task.md` from writing the function to explaining the `dict.get(..., 0) + 1` counting pattern in plain English.

## [2026-04-08] ingest | counting pattern mostly explained, empty-input reason still fuzzy

- The student correctly explained that `0` is the fallback value and that `+ 1` increments the count.
- The only remaining mismatch is the empty-input explanation: `count_jobs_by_status([])` returns `{}` because the loop never runs, not because an empty input "does not contain the status key."
- Updated `next_task.md` to that one narrow clarification instead of moving on yet.

## [2026-04-08] ingest | counting pattern explanation completed

- The student corrected the empty-input explanation and tied it to the actual loop behavior: the loop never runs, so the count dictionary stays empty.
- Updated `student_lessons/index.md` so `counting_with_dictionaries.md` is now treated as a taught lesson.
- Updated `next_task.md` from explanation cleanup to a fresh report-building task based on dictionary counts.

## [2026-04-08] ingest | build_status_summary passes tests but misses explicit sort enforcement

- Reviewed `python_baseline/build_status_summary.py` and `tests/test_build_status_summary.py`.
- Ran `python -m unittest tests.test_build_status_summary -v`; all 3 tests passed.
- The implementation currently uses dictionary insertion order, and the tests currently happen to match that order, so the alphabetical-sort requirement is not yet explicitly enforced.
- Updated `next_task.md` to tighten both the test and the implementation around alphabetical sorting.

## [2026-04-08] ingest | build_status_summary sort enforcement completed

- Rechecked `python_baseline/build_status_summary.py` and `tests/test_build_status_summary.py` after the sorting revision.
- Ran `python -m unittest tests.test_build_status_summary -v`; all 3 tests passed.
- The implementation now sorts explicitly with `sorted(count_jobs.items())`, and the revised test data no longer lets insertion-order output pass accidentally.
- Updated `student_lessons/counting_with_dictionaries.md` and `next_task.md` so the next task shifts from counting/reporting to grouping IDs into dictionary lists.

## [2026-04-09] ingest | group_job_ids_by_status completed

- Reviewed `python_baseline/group_job_ids_by_status.py` and `tests/test_group_job_ids_by_status.py`.
- Ran `python -m unittest tests.test_group_job_ids_by_status -v`; all 3 tests passed.
- Updated the canonical state to reflect a fresh grouped-dictionary success, not just counting or reporting.
- Added `student_lessons/grouping_values_in_dictionaries.md` and updated `next_task.md` so the immediate follow-up is explaining the grouped-list pattern in plain English.

## [2026-04-09] process | made lesson-before-task preference explicit

- The student asked that genuinely new concepts be introduced with a short lesson before the exercise, not only new artifact types.
- Updated the root `AGENTS.md`, `teacher_state/teaching_strategy.md`, and `teacher_state/work_habits.md` to make that ordering explicit.

## [2026-04-09] ingest | grouping pattern explained back

- The student explained the main grouped-list dictionary pattern in plain English: lists hold the grouped IDs, first-seen empty-list initialization avoids a missing-key failure, and left-to-right `append(...)` preserves order.
- Updated `teacher_state/next_task.md` from explanation to a small compositional report task that combines grouping, joining, and sorting.

## [2026-04-09] process | clarified long-term roadmap and timeline

- The student asked for the longer teaching plan, end goal, and expected timeline.
- Updated `teacher_state/teaching_strategy.md` to preserve the staged progression from composition of known patterns to lower-scaffold debugging and then broader DSA-style tasks.
- Updated `teacher_state/work_habits.md` to record that a visible phase-based roadmap is helpful structure for this student.

## [2026-04-09] process | added canonical learning roadmap

- The student asked for a markdown roadmap that can be tracked and updated over time.
- Added `teacher_state/roadmap.md` with phase goals, lesson focus, exit signals, and rough timing.
- Updated `teacher_state/index.md` to include the new roadmap page.
- Rechecked that `teacher_state/next_task.md` still holds exactly one concrete immediate task.
