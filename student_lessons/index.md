# Student Lessons Index

## Current Lesson Map

- `python_guards_and_loop_flow.md`: taught; checking dictionary keys safely and understanding skip versus early `return`
- `list_order_and_append.md`: taught; why filtering with a `for` loop and `append()` preserves order
- `unittest_basics.md`: taught; what a test file is, how imports work across files, and the minimum `unittest` structure
- `joining_strings_for_reports.md`: taught; how to build comma-separated output without leaving a trailing comma
- `counting_with_dictionaries.md`: taught; how `dict.get(key, 0) + 1` builds category counts safely
- `grouping_values_in_dictionaries.md`: taught; how to build a dictionary whose values are lists and append matching items into the right group

## Taught So Far

- dictionary key checks with `"key" in some_dict`
- why missing-key items can be skipped safely
- the difference between skipping one loop iteration and returning from the whole function
- why appending matching items in a left-to-right loop preserves input order
- the purpose of a test file versus a normal Python script
- why `", ".join(...)` is cleaner than manually adding commas in a loop
- how `dict.get(key, 0) + 1` is used to count categories
- why sorted output may need `sorted(dict.items())` instead of relying on insertion order
- how to create a list for a key the first time it appears and then keep appending later matches to that same list

## Introduced But Not Yet Practiced Independently

- importing a function from one repo file into another
- `unittest`
- test classes as containers for test methods
- `self` inside a test method
- `self.assertEqual(actual, expected)`

## Not Yet Taught In Lesson Form

- object-oriented programming beyond the minimal test-file usage of `class` and `self`
- other assertion methods such as `assertTrue` or `assertRaises`
- `pytest`
- mocks, fixtures, or advanced test organization
