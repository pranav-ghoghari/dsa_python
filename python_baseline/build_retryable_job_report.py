def build_retryable_job_report(jobs: list[dict]) -> str:
    ids = []
    for job in jobs:
        if "status" in job and "retries_left" in job and "id" in job:
            if job["status"] == "failed" and job["retries_left"] > 0:
                ids.append(job["id"])
    if len(ids):
        users_list = ", ".join(str(i) for i in ids)
    else:
        users_list = "none"
    return "Retryable jobs: " + users_list
