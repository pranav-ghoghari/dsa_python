# 2026-04-07 Retryable Jobs Explanation

- The student gave a plain-English explanation of the outer key guard and the placement of `return count`.
- The explanation correctly described that missing-key jobs are skipped automatically and that `count` accumulates across the full loop before returning.
- The only missing explanation detail is the numeric filter: why `retries_left == 0` fails the inner condition.
