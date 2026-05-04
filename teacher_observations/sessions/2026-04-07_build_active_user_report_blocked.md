# 2026-04-07 Build Active User Report Blocked

- The student wrote both `build_active_user_report.py` and its test file, but got stuck on exact string formatting.
- The focused test run showed the logic was mostly right and the only failure was a trailing `", "` at the end of the built string.
- Teaching implication: introduce the reusable `", ".join(...)` pattern as a student lesson rather than treating this as only a one-off bug.
