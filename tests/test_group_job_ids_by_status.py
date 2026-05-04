import unittest
from python_baseline.group_job_ids_by_status import group_job_ids_by_status

class GroupJobIdsByStatus(unittest.TestCase):
    def test_repeated_status(self) -> None:
        jobs = [
            {"id": 1, "status": "failed", "retries_left": 1},
            {"id": 2, "status": "running", "retries_left": 2},
            {"id": 3, "status": "failed", "retries_left": 4}
        ]
        self.assertEqual(group_job_ids_by_status(jobs), {"failed": [1,3], "running": [2]} )

    def test_missing_keys(self) -> None:
        jobs = [
            {"id": 1, "status": "failed", "retries_left": 1},
            {"id": 2, "status": "running", "retries_left": 2},
            {"id": 3, "retries_left": 2},
            {"status": "running", "retries_left": 2},
            {"id": 5, "status": "failed", "retries_left": 4}
        ]
        self.assertEqual(group_job_ids_by_status(jobs), {"failed": [1,5], "running": [2]} )

    def test_empty_input(self) -> None:
        jobs = []
        self.assertEqual(group_job_ids_by_status(jobs), {} )