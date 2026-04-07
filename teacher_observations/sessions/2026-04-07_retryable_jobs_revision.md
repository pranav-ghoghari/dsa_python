# 2026-04-07 Retryable Jobs Revision

- The student revised `count_retryable_jobs(...)` to check that both `status` and `retries_left` keys exist before direct indexing.
- This removes the earlier missing-key crash risk and avoids the premature `return 0` problem.
- The draft still does not fully match the requirement because it counts any failed job with a present `retries_left` key, including `0` or negative values.
- Teaching implication: keep feedback narrowed to rereading and enforcing the last missing condition rather than changing the whole structure.
