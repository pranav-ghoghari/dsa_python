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
- When a task depends on a genuinely new concept pattern, give the minimal lesson first unless the new task is only a very small transfer from a pattern the student just demonstrated.
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

## Long-Range Direction

- The end goal is independent small-to-medium Python problem solving, not memorizing isolated syntax facts.
- Concretely, the target is that the student can read a requirement, choose workable data structures, write the function from a blank page, write or revise matching tests, debug failures, and explain the final logic in plain English.
- The current direction is staged:
  - first combine already-taught patterns reliably in one task
  - then reduce scaffolding so more of the debugging and review burden sits with the student
  - then move into slightly broader tasks that may need helper-function decomposition, stronger test design, and more novel reasoning
  - only after that shift toward more algorithmic or DSA-style problem solving without losing code clarity
- The timeline should stay evidence-based rather than calendar-fixed, but at the current pace the present "compose known patterns accurately" phase should last the next several tasks, the lower-scaffold debugging/refactoring phase is likely the next few weeks of steady work, and broader DSA-style tasks should begin only after repeated blank-page successes with less prompting.
