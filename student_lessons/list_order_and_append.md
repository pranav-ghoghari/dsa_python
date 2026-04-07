# List Order And Append

## What This Lesson Is About

This lesson explains why a filtered result list can keep the same order as the input list.

## How Order Gets Preserved

Suppose you have:

```python
ids = []

for job in jobs:
    if some_condition:
        ids.append(job["id"])
```

This preserves order because:

- `for job in jobs` reads the input list from left to right
- `append()` adds each matching item to the end of the new list
- Python lists keep the order in which items were appended

So the output list becomes:

- the matching items only
- in the same order they appeared in the input

## Example

```python
jobs = [
    {"id": 10, "status": "failed", "retries_left": 2},
    {"id": 20, "status": "running", "retries_left": 5},
    {"id": 30, "status": "failed", "retries_left": 1},
]
```

If you append only the matching failed jobs with retries left, the result is:

```python
[10, 30]
```

It is not `[30, 10]` because job `10` appeared first and was appended first.

## Core Idea

Filtering with a left-to-right loop plus `append()` keeps input order automatically.
