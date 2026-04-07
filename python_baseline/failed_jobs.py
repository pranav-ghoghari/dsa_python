
def count_retryable_jobs(jobs: list[dict]) -> int:
    count = 0
    for job in jobs:
        if "status"  in job and "retries_left" in job:
            if job["status"] == "failed" and job["retries_left"] > 0:
                count += 1
    return count



# input: [{"status": "failed", "retries_left": 1}] this should count because status is failed and retries_left greater than 0
# expected: 1
# input: [{"status": "failed"}] this should not count because it has retries_left key missing
# expected: 0
# [{"status": "failed", "retries_left": 0}] this would be skipped because status is failed but retries_left is 0
# expected: 0