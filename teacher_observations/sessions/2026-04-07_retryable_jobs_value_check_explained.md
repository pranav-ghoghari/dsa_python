# 2026-04-07 Retryable Jobs Value Check Explained

- The student correctly explained that `{"status": "failed", "retries_left": 0}` does not get counted because it fails the inner `retries_left > 0` condition.
- This completes the plain-English explanation of the function's key guard, value filter, and return placement.
- Teaching implication: move from explanation to small test-case design.
