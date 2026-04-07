# Concept Mastery

## Problem Decomposition

- Strongest relative area.
- The student can usually infer the intended steps of a small task from function names, docstrings, and tests.

## Control-Flow Reasoning

- Can map requirements onto loops, counters, conditions, and returns for small concrete functions.
- Baseline completion and `failed_jobs.py` both support this.
- Can now explain that a failed outer key-check simply falls through to the next loop iteration when there is no `else`/`return`, and that `return count` belongs after the loop so the full total accumulates first.
- Can also explain that `retries_left == 0` fails the inner `> 0` condition and therefore does not increase the counter.

## Data-Structure Understanding

- Improved materially during the baseline.
- Early notes showed confusion around dictionary keys, values, and field access.
- Later evidence shows successful dictionary aggregation and boolean config parsing.
- Optional-key handling still needs reinforcement.

## Code-Reading Ability

- Stronger than raw syntax fluency.
- The student can read intent from starter code, test cases, and docstrings even when exact syntax is still shaky.

## Abstraction Level

- Works best with narrow, business-like functions and explicit requirements.
- There is not yet enough evidence for broader abstraction, reusable design, or algorithm-heavy tasks without scaffolding.
- Formal testing structure currently sits outside the student's evidenced model and should be taught as a new artifact type rather than assumed from function-writing ability.
