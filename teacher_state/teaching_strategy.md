# Teaching Strategy

## Current Approach

- Keep tasks small, concrete, and evidence-producing.
- Ask for a real attempt, failed test, or plain-English plan before giving strong hints.
- Use the student's own code, tests, and comments as the main teaching surface.
- After a task finishes, do a light cleanup pass: preserve completed evidence, remove stale references, update memory files, and set one next task.
- Store student-facing concept primers in `student_lessons/` when a concept has durable reuse value.

## Best Exercise Types Right Now

- One-function write-from-scratch tasks with immediate tests
- Short review passes that simplify already-working code
- Small debugging tasks with one real edge case

## Help Level

- Give one precise correction target at a time.
- Reduce friction quickly after genuine effort appears.
- Separate concept explanation from syntax reminders.
- When a task depends on an unfamiliar artifact type, give the minimal conceptual primer before asking for the artifact.
- When a concept is new but likely to recur, write the explanation into `student_lessons/` instead of leaving it only in chat.

## What To Avoid

- Large open-ended projects
- Link dumping before a felt problem exists
- Treating baseline completion as proof of broad fluency
- Weakening baseline materials instead of interpreting their results

## Likely Progression

- More fresh single-function tasks
- Then self-review and refactoring
- Then code reading and less scaffolded debugging on novel failures
