# Learning Roadmap

This file tracks the phase-based teaching plan.

It is not the task backlog.

Use `next_task.md` for the one concrete immediate assignment.

## Tracking Rules

- Advance by evidence, not by elapsed time alone.
- Do not mark a phase complete after one passing task.
- Promote only when recent evidence supports all four categories:
  - explain
  - recognize
  - write unaided
  - debug
- Rough timing estimates assume steady work on several small tasks per week.
- If pace or evidence changes, update this file in place.

## Phase 1 | Current | Core Function Fluency

### Goal

Turn small requirements into correct Python functions and matching tests with less rescue.

### Lesson Focus

- loops, conditionals, returns, and accumulator patterns
- safe dictionary access and missing-key handling
- filtering, counting, grouping, joining, and sorting
- exact output formatting
- `unittest` basics and reading test output

### Exit Signals

- The student can complete several fresh function-plus-test tasks from a blank page with only light prompting.
- Edge cases such as missing keys, empty input, and exact formatting are missed less often on the first draft.
- A failing test can be used to revise either the code or the expected output without the fix being supplied.
- The final code can be explained in plain English after completion.

### Rough Timing

- Current phase.
- Likely the next several tasks.
- Roughly the next 2 to 4 weeks if work stays steady.

## Phase 2 | Next | Broader Everyday Python

### Goal

Widen the toolbox without losing reliability on the basics.

### Lesson Focus

- sets and tuples
- helper-function decomposition
- list and dictionary comprehensions
- exceptions and defensive handling
- module/import structure
- basic file I/O

### Exit Signals

- The student chooses between list, dict, set, and tuple for a clear reason.
- Small functions can be split into helper functions without losing the behavior.
- Basic exceptions can be read and handled without stalling the whole task.
- A small multi-file exercise or file-I/O task can be completed with tests.

### Rough Timing

- Starts after repeated Phase 1 blank-page wins.
- Likely a short middle phase rather than a long one.
- Roughly 2 to 6 weeks after Phase 1 is solid, depending on transfer speed.

## Phase 3 | Later | Objects And State

### Goal

Introduce classes only when they solve a real modeling problem instead of adding syntax noise.

### Lesson Focus

- `class` and object instances
- `self`
- `__init__`
- instance attributes and instance methods
- when a class is a better fit than a plain function

### Exit Signals

- The student can write a small class with `__init__` and explain what state each instance stores.
- Method calls and attribute access make sense without mixing up class-level and instance-level ideas.
- The student can compare a function-based solution to a small class-based solution and explain the tradeoff.

### Rough Timing

- After Phase 2 fundamentals are reliable.
- Mid-course, not immediate.
- Timing depends more on modeling readiness than on calendar date.

## Phase 4 | Later | Broader DSA-Style Problem Solving

### Goal

Transfer Python fluency into wider problem-solving tasks with less scaffolding.

### Lesson Focus

- arrays/strings style tasks
- hash-map and set reasoning
- stacks, queues, and basic recursion when appropriate
- beginner complexity reasoning
- stronger debugging on more novel failures
- self-review and small refactors after correctness

### Exit Signals

- The student can solve fresh small algorithmic tasks from a blank page.
- Data-structure choices are deliberate rather than accidental.
- The student can explain the main tradeoff of one approach versus another at a beginner level.
- Debugging remains functional even when the failure pattern is less familiar.

### Rough Timing

- Begins only after core Python fluency is stable enough that the main struggle is the problem, not the syntax.
- Expected to overlap with continued Python cleanup and test practice.

## Phase 5 | Later | Advanced Python Abstractions

### Goal

Teach higher-level Python features after the function model and object model are already stable.

### Lesson Focus

- decorators
- generators and `yield`
- context managers and `with`
- `@dataclass` and other convenience abstractions when useful
- deeper typing only when it helps real tasks

### Exit Signals

- The student can explain how a simple decorator wraps and returns a function.
- A small decorator can be written and tested without hiding the core behavior.
- `yield` can be used when sequence generation benefits from it.
- Context-manager usage is understood as resource setup/cleanup, not just copied syntax.

### Rough Timing

- Later phase.
- Starts only after the student is already comfortable with functions, closures at a basic level, and object state.

## Current Placement

- The student is currently in Phase 1.
- The immediate milestone is to combine grouping, joining, sorting, and testing in one small task.
- Do not widen the surface just to cover more topics; widen it when the current phase is producing repeated independent wins.
