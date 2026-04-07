# 2026-04-07 Retryable Jobs Comment Tests

- The student wrote three comment-based examples under `count_retryable_jobs(...)` rather than jumping directly to a test framework.
- The examples target the main branches: one countable job, one missing-key job, and one zero-retries job.
- One expected outcome is still incorrect: the missing-`retries_left` example was described as counting even though the function should skip it.
- Teaching implication: keep the focus on expected outputs and branch meaning before moving to formal unit-test syntax.
