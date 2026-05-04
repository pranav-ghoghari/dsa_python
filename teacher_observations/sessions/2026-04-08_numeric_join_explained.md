# 2026-04-08 Numeric Join Explained

- The student explained in plain English why `", ".join(ids)` fails when `ids` contains integers and why `", ".join(str(i) for i in ids)` works.
- This closes the formatting detail introduced by `build_retryable_job_report(...)`.
- Teaching implication: move away from repeated report formatting and test a fresh dictionary-accumulation task next.
