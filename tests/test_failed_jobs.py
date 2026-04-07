import unittest

from python_baseline.failed_jobs import count_failed_jobs


class CountFailedJobsTests(unittest.TestCase):
    def test_counts_failed_jobs(self) -> None:
        jobs = [
            {"id": 1, "status": "failed"},
            {"id": 2, "status": "running"},
            {"id": 3, "status": "failed"},
            {"id": 4, "status": "success"},
        ]
        self.assertEqual(count_failed_jobs(jobs), 2)

    def test_ignores_jobs_with_missing_status(self) -> None:
        jobs = [
            {"id": 1, "status": "failed"},
            {"id": 2},
            {"id": 3, "status": "success"},
        ]
        self.assertEqual(count_failed_jobs(jobs), 1)

    def test_returns_zero_for_empty_input(self) -> None:
        self.assertEqual(count_failed_jobs([]), 0)


if __name__ == "__main__":
    unittest.main()
