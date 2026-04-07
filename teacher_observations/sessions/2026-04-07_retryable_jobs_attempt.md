# 2026-04-07 Retryable Jobs Attempt

- Reviewed the student's draft of `count_retryable_jobs(jobs: list[dict]) -> int` in `python_baseline/failed_jobs.py`.
- The student independently wrote the function skeleton, loop, counter, and combined condition.
- The student independently chose `job.get(...)` for dictionary access, which is stronger evidence of emerging missing-key awareness than earlier tasks.
- The draft still returned `0` from inside the loop on the first non-matching item.
- The draft also left an incomplete edge-case guard: `job.get("retries_left") > 0` is still unsafe when `status` is `"failed"` but `retries_left` is missing.
- Teaching implication: keep the next task on debugging the student's own draft rather than moving to a larger new function.
