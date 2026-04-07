# 2026-04-07 Retryable Jobs Comment Tests Revision

- The student revised the comment-based examples under `count_retryable_jobs(...)` to include explicit `expected` lines.
- The countable case and the `retries_left == 0` case are now conceptually correct.
- The missing-key case still has a wording mismatch: the comment says it should count, but the expected value correctly says `0`.
- Teaching implication: keep feedback extremely narrow and focus on aligning prose with expected behavior.
