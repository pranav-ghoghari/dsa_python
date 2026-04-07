# Student Lessons

`student_lessons/` stores student-facing explanations of concepts that have already been taught or intentionally introduced.

This directory is not raw evidence and not canonical teacher-state.

It is the maintained lesson record for the student.

## Purpose

Use this directory to:

- explain new concepts in plain language before expecting independent use
- preserve what has already been taught so the same fundamentals do not need to be rebuilt from scratch each time
- keep student-facing explanations separate from teacher-only assessment notes

## Writing Rules

- write to the student, not about the student
- use plain, concrete language
- prefer short examples over abstract theory
- explain only the minimum needed for the current stage
- clearly separate "what this is" from "how to use it"
- avoid assuming knowledge of concepts that have not yet been taught
- when a concept uses a new artifact type, explain the artifact first

## Maintenance Rules

- keep `index.md` current when adding or renaming lesson files
- update existing lesson files in place when a clearer explanation replaces an older one
- add a new lesson file when a genuinely new concept or workflow is introduced
- avoid turning this directory into a long journal; lessons should be maintained references
- when a lesson materially changes the teaching process, reflect that in `teacher_state/` and `teacher_state/log.md`

## Relationship To Other Directories

- `python_baseline/` and `tests/` are where the student writes code and produces evidence
- `teacher_observations/sessions/` stores dated historical notes
- `teacher_state/` stores the teacher's current evidence-based model
- `student_lessons/` stores reusable student-facing explanations
