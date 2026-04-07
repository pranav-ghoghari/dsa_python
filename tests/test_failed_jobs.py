import unittest

from python_baseline.failed_jobs import count_retryable_jobs


class CountRetryableJobsTests(unittest.TestCase):
    def test_counts_only_failed_jobs_with_retries_left(self) -> None:
        jobs = [
            {"id": 1, "status": "failed", "retries_left": 2},
            {"id": 2, "status": "running", "retries_left": 5},
            {"id": 3, "status": "failed", "retries_left": 1},
            {"id": 4, "status": "success", "retries_left": 3},
            {"id": 5, "status": "failed", "retries_left": 0},
        ]
        self.assertEqual(count_retryable_jobs(jobs), 2)

    def test_skips_jobs_with_missing_required_keys(self) -> None:
        jobs = [
            {"id": 1, "status": "failed", "retries_left": 1},
            {"id": 2},
            {"id": 3, "status": "failed"},
            {"id": 4, "retries_left": 3},
            {"id": 5, "status": "success", "retries_left": 9},
        ]
        self.assertEqual(count_retryable_jobs(jobs), 1)

    def test_returns_zero_for_empty_input(self) -> None:
        self.assertEqual(count_retryable_jobs([]), 0)


if __name__ == "__main__":
    unittest.main()
