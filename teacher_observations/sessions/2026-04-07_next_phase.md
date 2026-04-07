# Next Phase

Date: 2026-04-07

## New Evidence

- The student created `python_baseline/failed_jobs.py` without being given a starter function body.
- The student correctly used:
  - a loop
  - a counter
  - a string equality check
  - a final return

## Current Gap

- The likely missed detail is requirement handling for missing dictionary keys.
- The student used direct indexing with `job["status"]`, which will fail if a job has no `"status"` key.
- After one targeted correction, the student updated the code to use `job.get("status")` and the exercise now passes.

## Teaching Response

- Keep using write-from-scratch exercises.
- Add a small test suite immediately so requirements become concrete.
- Review edge-case handling explicitly, not only the happy path.
- The student is ready for more small from-scratch tasks with one hidden edge case each.
