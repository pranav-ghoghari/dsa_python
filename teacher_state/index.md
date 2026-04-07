# Teacher State Index

## Core State

- `student_profile.md`: concise current model of the student's strengths, limits, and explain/recognize/write/debug split.
- `syntax_fluency.md`: what Python syntax patterns the student can and cannot currently produce unaided.
- `concept_mastery.md`: current view of decomposition, control flow, data-structure reasoning, code reading, and abstraction level.
- `debugging_profile.md`: how the student reacts to failing tests, tracebacks, and precise correction targets.
- `work_habits.md`: effort patterns, pacing needs, helpful scaffolds, and avoidance risks.
- `active_hypotheses.md`: current beliefs under test and the evidence that would confirm or disconfirm them.
- `teaching_strategy.md`: current teaching approach, help level, and progression.
- `next_task.md`: exactly one concrete next task.
- `resource_map.md`: a short list of high-value references worth using when a real gap appears.

## Supporting Files

- `README.md`: how to use `teacher_state/` for ingest, query, and lint.
- `log.md`: append-only record of migrations, ingests, syntheses, and lint passes.
- `lint_checklist.md`: quick consistency checklist for maintenance passes.
- `../student_lessons/index.md`: student-facing lesson map for concepts that have already been taught or intentionally introduced.

## Important Persistent Evidence

- `../python_baseline/README.md`: baseline instructions and integrity constraints for the assessment zone.
- `../python_baseline/interview.md`: reflection answers that show early conceptual understanding and misunderstandings.
- `../python_baseline/assessment.py`: completed baseline code and the strongest current evidence for small-task implementation ability.
- `../python_baseline/failed_jobs.py`: first fresh write-from-scratch follow-up exercise after baseline completion.
- `../student_lessons/`: maintained student-facing explanations and concept primers.
- `../teacher_observations/sessions/`: dated historical notes and review history.
