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
