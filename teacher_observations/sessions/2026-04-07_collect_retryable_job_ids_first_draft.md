# 2026-04-07 Collect Retryable Job IDs First Draft

- The student wrote a fresh first draft of `collect_retryable_job_ids(...)` without starter code.
- The draft correctly uses a list accumulator, preserves input order, and reuses the missing-key and `retries_left > 0` guard pattern from the previous task.
- The only bug is a small key-name typo: the outer check uses `"id "` with a trailing space, which prevents valid jobs from being collected.
- Teaching implication: keep feedback narrow and focused on exact string-literal accuracy rather than changing the function structure.
