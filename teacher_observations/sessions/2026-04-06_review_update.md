# Review Update

Date: 2026-04-06

## New Evidence

- The student fixed the blocking `SyntaxError` in `count_active_users`.
- The student successfully converted C++-style increment thinking into valid Python with `count += 1`.
- The student completed a working draft of `deduplicate_preserve_order`.
- The student improved `normalize_username` so that trimming and lowercasing now work.
- The student is still missing one precise behavior in `normalize_username`: collapsing multiple spaces into a single hyphen.
- The student followed the hint toward `split()` and `join()`, which is the correct tool family.
- The student used `split(' ')` instead of whitespace-aware splitting, which produced empty strings and extra hyphens at the edges.
- The student corrected that detail by switching to `split()` with no argument.
- `normalize_username` now passes all of its tests.
- The student successfully completed `group_expenses_by_category` after switching from whole-dictionary views to specific field extraction.
- In `parse_feature_flags`, the student now understands the broad parsing shape:
  - blank-input check
  - split by comma
  - split each piece by equals
- The student can now complete the core parse-and-convert logic for valid inputs.
- The current blocker is turning each parsed `key=value` pair into a dictionary assignment with the correct boolean conversion and loop structure.
- The remaining blockers are now edge-case handling and exact output formatting, not the core algorithm.
- The student fixed the runtime `KeyError` in `count_active_users` by using `dict.get(...)`.
- The student fixed the logic mismatch in `count_active_users`; that function now passes its tests.
- The student is attempting dictionary aggregation in `group_expenses_by_category`, but the key/value model is still shaky.
- The student is testing ideas in `parse_feature_flags`, but is currently using `strip()` for a job it does not do.

## Teacher Interpretation

- This is real forward movement.
- The student can absorb targeted syntax feedback and apply it on the next attempt.
- The dominant bottleneck is now API precision, requirement reading, and data-shape reasoning, not basic fear of writing code.
- The student often reaches the correct concept but misses one exact method detail or default behavior.
- When given one precise correction target, the student can usually close the gap quickly.
- The student is showing a repeatable pattern: one focused conceptual fix often unlocks the whole function.
- When stuck, the student often has the right high-level steps but not the exact Python statement that joins them together.
- The student is benefiting from short cycles of: attempt, run tests, review, retry.
- The student can fix a narrow logic bug when the task boundary is kept small and explicit.

## Strategic Next Step

- Keep the next task narrow.
- Do not switch to all remaining functions at once.
- `count_active_users` is complete enough for now.
- Fix the whitespace-collapse issue in `normalize_username` next before moving to the unfinished dictionary-heavy functions.
- Specifically teach the difference between `split(' ')` and `split()` because that exact distinction is currently blocking progress.
- `normalize_username` is complete enough for now.
- The next isolated target should be `group_expenses_by_category`, because it reinforces dictionary basics before moving to the more string-parsing-heavy `parse_feature_flags`.
- In `group_expenses_by_category`, the student is still mixing up:
- checking whether a key exists in a dictionary
- reading the value stored under a key
- using the literal string `"category"` versus the category value from the current expense
- The student is also treating `expense.keys()` and `expense.values()` as if they were the current category and amount, rather than collections describing the whole dictionary.
- `group_expenses_by_category` is complete enough for now.
- The next target should be `parse_feature_flags`, which introduces multi-step string parsing and validation.
- In `parse_feature_flags`, the next teaching move should focus on:
  - extracting `key` and `value_text` from `section`
  - converting only that one `value_text`
  - assigning into `config[key]`
- The baseline is now complete, so the next stage can shift from raw completion to code quality, simplification, and explanation.
