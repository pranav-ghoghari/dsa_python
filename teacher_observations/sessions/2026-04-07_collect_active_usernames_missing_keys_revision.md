# 2026-04-07 Collect Active Usernames Missing Keys Revision

- The student revised `test_missing_keys` in `tests/test_collect_active_usernames.py` to include both required missing-key branches.
- The test now has the right edge-case shape, but the expected output list is stale and still includes `"nishi"` even though there is no valid `"nishi"` user in the current input data.
- Teaching implication: keep the next step on expected-output alignment rather than moving to a new task yet.
