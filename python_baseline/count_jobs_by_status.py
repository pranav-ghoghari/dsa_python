def count_jobs_by_status(jobs: list[dict]) -> dict[str, int]:
    count_jobs = {}
    for job in jobs:
        if "status" in job:
            status = job["status"]
            count_jobs[status] = count_jobs.get(status,0)+1
    return count_jobs
