# Debugging Profile

## Reaction To Failing Tests

- The student benefits from short cycles of attempt, test run, review, and retry.
- Passing the baseline suggests tests are now useful feedback rather than something purely confusing.

## Traceback Handling

- Early reflection answers showed weak understanding of what a traceback is.
- Later work shows the student can fix a `SyntaxError` or missing-key bug after guidance.
- Independent traceback reading on a novel task is still not well evidenced.

## Guessing Versus Reasoning

- The student often has the right high-level plan but guesses the exact method or expression detail.
- One precise correction target works better than a broad lecture.

## Use Of Error Feedback

- Productive when the feedback points to one concrete mismatch.
- Less proven when several failures interact or when the issue is not already localized by tests.
- The student can use a control-flow warning to reason correctly about why an in-loop `return` ends the whole function.
- The student can make a focused safety fix after feedback and then align the final logic with the exact spec on the next pass.
- After the fix, the student can also explain the final control flow in plain English rather than only presenting the code.

## Current Debugging Target

- Move from reactive fixes after a failure toward proactive handling of edge cases before the first run.
- Practice tracing loop behavior item by item so a single non-matching record does not incorrectly end the whole function.
