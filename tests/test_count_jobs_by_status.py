import unittest
from python_baseline.count_jobs_by_status import count_jobs_by_status

class CountJobsByStatus(unittest.TestCase):
    def test_repeat_statuses(self) -> None:
        jobs = [
            {"id": 1, "status": "failed", "retries_left": 1},
            {"id": 2, "status": "running", "retries_left": 2},
            {"id": 3, "status": "failed", "retries_left": 4}
        ]
        self.assertEqual(count_jobs_by_status(jobs),{"failed": 2, "running": 1})

    def test_missing_statuses(self) -> None:
        jobs = [
            {"id": 1, "status": "failed", "retries_left": 1},
            {"id": 2, "status": "running", "retries_left": 2},
            {"id": 3,  "retries_left": 4},
            {"id": 4, "status": "failed", "retries_left": 4}
        ]
        self.assertEqual(count_jobs_by_status(jobs),{"failed": 2, "running": 1})

    def test_empty_input(self) -> None:
        jobs = []
        self.assertEqual(count_jobs_by_status(jobs), {})