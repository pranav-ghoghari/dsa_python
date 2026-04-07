# Baseline Assessment Zone

`python_baseline/` is a controlled assessment and practice area.

Use it to measure what the student can actually do, not to smuggle in answers.

## Rules

- Preserve assessment integrity.
- Do not add full solutions or answer-key style hints to baseline prompts, README files, or tests.
- Prefer asking for one of these before giving strong help:
  - a code attempt
  - a failed test run
  - a plain-English explanation
  - short `#` comments showing the student's intended steps
- Distinguish conceptual understanding from syntax fluency.
- Treat tests, tracebacks, and student edits as evidence.
- Keep student comments when they reveal reasoning unless they are clearly obsolete.
- If real effort has happened and the student is blocked, reduce friction and help directly.

## Interpretation Rules

- A correct explanation does not prove independent coding ability.
- A passing test on one task does not prove general mastery.
- Missing-key errors, formatting mismatches, and API misuse are useful evidence, not just bugs to erase.

## Update Rule

After meaningful work in this directory:

- update the relevant `teacher_state/` files
- add or update a dated note in `teacher_observations/sessions/` when the event matters historically
- keep the baseline materials themselves solution-free

## Cleanup Rule

When a baseline or follow-up task is finished:

- keep the completed student code as evidence
- do not clear finished files just to make room for the next task
- clean up stale tests or stale task references if they no longer match the current file/function
- prefer creating a new small file for the next exercise rather than overwriting old evidence
