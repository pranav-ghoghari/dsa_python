# Python Baseline Assessment

This is a practical baseline, not a trick quiz.

The goal is to find out which Python fundamentals you can already use without relying on copy-paste or AI generation.

## Timebox

Aim for 45 to 90 minutes.

## What This Measures

- Reading function signatures and docstrings
- Basic Python syntax
- Strings, lists, dictionaries, and loops
- Conditionals and return values
- Handling edge cases
- Reading tests to understand expected behavior

## How To Take It

1. Open `assessment.py`.
2. Implement each function in order.
3. Run the tests after each function:

```bash
python -m unittest discover -s tests -v
```

4. Do not worry if many tests fail at first.
5. Keep short notes about where you got stuck.

## How I Will Read The Result

- `0-2` functions solved: you can probably read some code, but writing code from scratch is still shaky.
- `3-4` functions solved: you have partial foundations and can start writing small scripts with coaching.
- `5-6` functions solved: the basics are there, and the focus shifts to debugging, fluency, and code quality.

## How This Fits Into The Repo

- Work in this folder is raw evidence for the teaching record.
- Results from this assessment should update `teacher_state/`, not the prompt itself.
- Keep this area solution-free so it remains a real measurement of independent skill.
- Completed files in this folder should usually stay in place as evidence; start new follow-up tasks in new files instead of clearing old ones.

## Written Reflection

After the coding part, answer the prompts in `interview.md` in chat or in your own notes. That helps separate "I got lucky with syntax" from "I actually understand the concepts."
