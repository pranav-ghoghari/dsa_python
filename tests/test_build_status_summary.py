import unittest
from python_baseline.build_status_summary import build_status_summary

class TestBuildStatusSummary(unittest.TestCase):
    def test_repeated_statuses(self) -> None:
        jobs = [
            {"id": 1, "status": "running", "retries_left": 1},
            {"id": 2, "status": "failed", "retries_left": 2},
            {"id": 3, "status": "failed", "retries_left": 4}
        ]
        self.assertEqual(build_status_summary(jobs),"failed: 2\nrunning: 1")

    def test_missing_statuses(self) -> None:
        jobs = [
            {"id": 1, "status": "failed", "retries_left": 1},
            {"id": 2, "status": "running", "retries_left": 2},
            {"id": 2,  "retries_left": 2},
            {"id": 3, "status": "failed", "retries_left": 4}
        ]
        self.assertEqual(build_status_summary(jobs), "failed: 2\nrunning: 1")

    def test_empty_statuses(self) -> None:
        jobs = []
        self.assertEqual(build_status_summary(jobs), "No jobs found.")
