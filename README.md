# Python Teaching Memory Repo

This repository supports an ongoing Python tutoring workflow.

It separates raw student evidence from a maintained teacher wiki so future sessions can start from current knowledge instead of scattered notes.

## Repo Structure

- `python_baseline/`: controlled assessment and practice area. This is where student code, reflection prompts, and small evidence-generating exercises live.
- `tests/`: executable evidence for the baseline and follow-up practice tasks.
- `teacher_observations/`: dated historical session notes and review updates.
- `teacher_state/`: the current synthesized student model, teaching strategy, and next task.
- `student_lessons/`: student-facing lesson notes for concepts that have already been taught or are being introduced.
- `AGENTS.md`: operating rules for how the agent should ingest evidence, answer questions, and maintain the repo.

## How The Workflow Works

1. The student works on a baseline or practice task.
2. Code, tests, failures, and reflection become raw evidence.
3. The agent updates `teacher_state/` in place to reflect the current best model of the student.
4. Student-facing explanations are stored in `student_lessons/` when a concept is taught.
5. Significant events are preserved in `teacher_observations/sessions/`.
6. Future questions such as "what can the student do?" or "what next?" start from `teacher_state/`, not from old session notes.

## Cleanup Policy

- Finished exercises remain in the repo as raw evidence.
- Cleanup means removing stale references, updating tests, and keeping `teacher_state/` current.
- Cleanup does not mean wiping completed files like `python_baseline/assessment.py`.

## Start Points

- For the baseline assessment: read `python_baseline/README.md`.
- For the current student model: read `teacher_state/index.md`.
- For the operating rules: read `AGENTS.md`.

## Intent

This repo is meant to support a persistent teaching process, not one-off chat help.

The baseline remains a real assessment. The teaching wiki exists to interpret results and plan the next task without weakening the assessment itself.
