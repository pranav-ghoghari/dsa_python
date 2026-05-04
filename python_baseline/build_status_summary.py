def build_status_summary(jobs: list[dict]) -> str:
    count_jobs = {}
    for job in jobs:
        if "status" in job:
            status = job["status"]
            count_jobs[status] = count_jobs.get(status,0)+1
    combined_jobs = ""
    if count_jobs:
        combined_jobs = "\n".join(f"{k}: {v}" for k,v in sorted(count_jobs.items()))
    else:
        combined_jobs = "No jobs found."

    return combined_jobs
