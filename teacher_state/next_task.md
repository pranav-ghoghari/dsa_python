# Next Task

## Task

Create one new small function and its test file:

- file: `python_baseline/build_grouped_job_report.py`
- function: `build_grouped_job_report(jobs: list[dict]) -> str`
- file: `tests/test_build_grouped_job_report.py`

Rules for the function:

- group job `id` values by `status`
- skip jobs missing either `id` or `status`
- preserve input order inside each status line
- if there are no valid jobs, return exactly: `No jobs found.`
- otherwise return one line per status in this format: `status: 1, 3`
- sort the status lines alphabetically by status name
- join lines with `\n`

## Success Condition

- The function returns the exact required string output.
- The test file covers:
  - repeated statuses
  - missing `id` or `status` keys being skipped
  - empty input returning `No jobs found.`
  - non-alphabetical input order still producing alphabetically sorted status lines
- `python -m unittest tests.test_build_grouped_job_report -v` passes.

## Why This Is Next

- The grouped-list pattern is now both coded and explained.
- The next useful step is to combine that pattern with exact string formatting and explicit sorting in one small task.

## Evidence This Will Produce

- Whether the student can compose several already-taught patterns into one correct report function
- Whether sorting plus numeric string-joining still holds up when combined with grouped dictionary logic
