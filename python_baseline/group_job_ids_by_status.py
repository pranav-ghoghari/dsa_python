def group_job_ids_by_status(jobs: list[dict]) -> dict[str, list[int]]:
    job_group = {}
    for job in jobs:
        if "status" in job and "id" in job:
            status = job["status"]
            if status not in job_group:
                job_group[status] = []

            job_group[status].append(job["id"])
    return job_group