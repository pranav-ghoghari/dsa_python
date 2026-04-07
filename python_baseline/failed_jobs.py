
def count_failed_jobs(jobs: list[dict]) -> int:
    count = 0
    for job in jobs:
        if job.get("status") == "failed":
            count += 1
    return count


