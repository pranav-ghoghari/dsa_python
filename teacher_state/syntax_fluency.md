# Syntax Fluency

## Variables And Assignment

- Can write simple assignments and counter updates such as `count += 1`.
- Earlier C++ transfer around `++` appears corrected by the 2026-04-06 baseline work.
- Cleanup details such as spacing and consistency still need attention.

## Loops

- Can write simple `for` loops over lists for counting, deduplication, aggregation, and report building.
- No meaningful evidence yet for `while` loops, nested loops, or more complex iteration patterns.

## Conditionals

- Can write equality checks and combined boolean conditions in small tasks.
- Exact edge conditions still benefit from rereading the requirement and tight feedback.
- The student can now verbally distinguish an early `return` from a skip-on-this-item outcome.
- Writing that distinction correctly in code still needs reinforcement, especially when `continue`-style thinking is needed instead of an early `return`.

## Functions

- Can implement small functions directly from signatures and docstrings.
- No strong evidence yet for splitting larger tasks into helper functions.

## Arguments And Returns

- Broad conceptual understanding is present.
- Earlier confusion about `print` versus `return` seems reduced after the baseline iteration cycle.

## Indexing And Dictionary Access

- Can use list append, dictionary assignment, and direct field access when keys are expected.
- Has now independently reached for `dict.get(...)` on a fresh task.
- Can now safely guard direct dictionary indexing with explicit key checks such as `"key" in job`.
- Can now combine key checks, direct indexing, string equality, and numeric comparisons correctly in a small loop-and-counter task after review.
- On a fresh transfer task, the overall guard pattern carried over correctly, but exact key spelling in string literals still needs close attention.
- Can now initialize a missing dictionary key with `[]` and then `append(...)` grouped values under that key.

## String And Collection Patterns

- Can now use `.strip()`, `.lower()`, `split()`, `join()`, `.replace()`, membership checks, and simple dict accumulation.
- Precision about method behavior can still slip when several similar operations are available.

## Patterns Not Yet Evidenced

- Nested data traversal beyond a list of flat dictionaries
- Larger functions with internal helper decomposition
- Consistently idiomatic cleanup without review pressure
- Independent test-file structure design from a blank page without a nearby example
- Independent cross-file import design without a nearby example
