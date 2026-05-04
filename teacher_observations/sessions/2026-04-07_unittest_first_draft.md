# 2026-04-07 Unittest First Draft

- After reading the first `unittest` lesson, the student could explain the broad purpose of imports, test files, and expected-versus-actual checking.
- The student remained unsure about what `unittest` specifically is, why test classes inherit from `unittest.TestCase`, what `self` really refers to, how the runner finds tests, and why test methods are written as `def test_x(self) -> None:`.
- The student nevertheless wrote a working `tests/test_collect_retryable_job_ids.py` by adapting the lesson pattern, and the file passed when run with `python -m unittest tests.test_collect_retryable_job_ids -v`.
- Teaching implication: keep the next step on execution mechanics and naming conventions before treating test-file structure as independently mastered.
