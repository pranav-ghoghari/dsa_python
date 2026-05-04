# 2026-04-07 Collect Active Usernames First Pair

- The student wrote a fresh `collect_active_usernames(...)` function in `python_baseline/collect_active_username.py` and a matching `tests/test_collect_active_usernames.py` file.
- The focused test run passed with three tests: multiple active users, missing keys, and empty input.
- The main remaining issue is not a function bug but a coverage gap: the missing-keys test covers a missing `is_active` case but does not yet include a user missing `username`.
- Teaching implication: keep the next task narrow and focused on strengthening the test rather than changing the function.
