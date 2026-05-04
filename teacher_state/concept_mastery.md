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
- The student has now also grouped values into dictionary-held lists by key, not only counted categories.
- Optional-key handling still needs reinforcement.

## Code-Reading Ability

- Stronger than raw syntax fluency.
- The student can read intent from starter code, test cases, and docstrings even when exact syntax is still shaky.

## Abstraction Level

- Works best with narrow, business-like functions and explicit requirements.
- There is not yet enough evidence for broader abstraction, reusable design, or algorithm-heavy tasks without scaffolding.
- Formal testing structure currently sits outside the student's evidenced model and should be taught as a new artifact type rather than assumed from function-writing ability.
- The student now has a workable beginner testing model: `TestCase` provides assertion helpers, `unittest` discovers `test_` methods, and test methods perform checks instead of returning values.
- The remaining conceptual fuzziness is local to `self` and object identity, not the whole testing workflow.
- The student can now connect most unittest output lines to the tests in the file.
- The student has now integrated code-writing and test-writing on a fresh small task.
- The student has now sharpened a two-branch missing-key test and aligned the expected output after a failing assertion.
- The next useful step is a fresh task where output formatting must be exact, not just list filtering.
- The student has now completed one fresh exact-formatting task by combining filtering with `join()` and an explicit empty case.
- The student has now also explained that formatting pattern back in plain English.
- The student has now transferred the formatting pattern to numeric IDs by using string conversion before `join()`.
- The student has now also explained that numeric-string conversion in plain English.
- The student has now completed a fresh dictionary-accumulation task from scratch and tested it successfully.
- The student has now explained most of the `dict.get(..., 0) + 1` counting pattern in plain English.
- The student has now also clarified the empty-input case correctly.
- The student has now started composing a report from dictionary counts rather than only returning the raw dictionary.
- The student has now enforced and tested the alphabetical-sort requirement explicitly.
- The student has now also completed a fresh dictionary task that groups values into lists instead of only incrementing counts.
- The student has now also explained the grouped-list pattern back in plain English, including the need for first-seen empty-list initialization and left-to-right `append(...)`.
- The next useful step is a more compositional report task that combines grouping, joining, and explicit sorting.
