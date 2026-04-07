
def collect_retryable_job_ids(jobs: list[dict]) -> list[int]:
    ids = []
    for job in jobs:
        if "status" in job and "retries_left" in job and "id" in job:
            if job["status"] == "failed" and job["retries_left"] > 0:
                ids.append(job["id"])
    return ids
