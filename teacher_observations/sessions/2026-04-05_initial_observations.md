# Initial Observations

Date: 2026-04-05

## What The Student Already Shows

- The student can read a function name and infer the business intent.
- The student understood that `normalize_username` needs a sequence of string transformations.
- The student correctly identified these likely steps:
  - trim whitespace at the beginning and end
  - lowercase the text
  - replace internal whitespace with `-`
- The student understood that `raise NotImplementedError` is a placeholder and that real code must return a value.
- The student inferred that `count_active_users(users: list[dict])` means a list where each element is a dictionary.
- The student understood that boolean fields such as `is_active` are checked for `True` or `False`.
- The student understood that solving `count_active_users` likely requires a loop, a counter, and a final `return`.
- The student is able to self-report their real limitation with useful honesty instead of pretending to know more than they do.
- The student explicitly wants ongoing teacher-style observation and strategic adjustment rather than static one-time feedback.
- The student can define a variable in approximate plain language as something that stores a value.
- The student can explain the general purpose of loops and `if` statements.
- The student now knows and successfully used the `.lower()` string method in actual code.
- The student is willing to write thought-process comments inside the code, which is useful evidence for teaching.

## What The Student Does Not Yet Show

- The student does not yet know the Python syntax well enough to translate their thinking into working code.
- The student still does not reliably know which exact Python string methods solve a task, even though `.lower()` is now recognized.
- The student has not yet demonstrated comfort with:
  - variable assignment in Python
  - `for` loop syntax
  - dictionary access syntax
  - conditional syntax
  - writing and returning values from a function
- The student has not yet demonstrated debugging skill from actual tracebacks.
- The student has not yet shown understanding of the difference between dictionary keys and dictionary values.
- The student has not yet shown a correct mental model of traceback or unit test behavior.

## Teacher Conclusion

- This is not "zero understanding."
- The student has early programming reasoning ability.
- The main gap appears to be syntax fluency and hands-on coding repetition, not total lack of logic.
- Teaching should start with writing tiny working Python statements and functions, then build upward.
- The student will likely benefit from a visible progress log because they care about whether the teaching model is adapting to new evidence.
- The student's comments reveal useful reasoning, but the jump from reasoning to executable Python is still the main bottleneck.
