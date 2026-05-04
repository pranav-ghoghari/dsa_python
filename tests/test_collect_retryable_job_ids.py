import unittest
from python_baseline.collect_retryable_job_ids import collect_retryable_job_ids


class CollectRetryableJobIdsTests(unittest.TestCase):
    def test_multiple_jobs(self) -> None:
        jobs = [
            {"id": 1,"status": "failed","retries_left": 1},
            {"id": 2,"status": "completed","retries_left": 2},
            {"id": 3,"status": "failed","retries_left": 4}
        ]
        self.assertEqual(collect_retryable_job_ids(jobs),[1,3])

    def test_missing_key(self) -> None:
        jobs = [
            {"status": "failed","retries_left": 1},
        ]
        self.assertEqual(collect_retryable_job_ids(jobs),[])

    def test_retries_zero(self) -> None:
        jobs = [
            {"id": 1, "status": "failed","retries_left": 0},
        ]
        self.assertEqual(collect_retryable_job_ids(jobs),[])

    def test_empty_input(self) -> None:
        jobs = []
        self.assertEqual(collect_retryable_job_ids(jobs),[])

