# Counting With Dictionaries

## What This Lesson Is About

This lesson explains a common pattern:

- read items one by one
- look at one key, such as `"status"`
- keep counts in a dictionary

Example goal:

```python
{"failed": 2, "running": 1}
```

## The Core Idea

You use one dictionary to store counts.

Example:

```python
counts = {}
```

Then for each job:

- read its status
- increase that status count by 1

## Why `get(..., 0)` Is Useful

If a status has not been seen before, it is not in the dictionary yet.

So this helps:

```python
counts[status] = counts.get(status, 0) + 1
```

Read it as:

- look up the current count for this status
- if it does not exist yet, use `0`
- then add `1`

## Example

Start:

```python
counts = {}
```

First job:

```python
status = "failed"
counts["failed"] = counts.get("failed", 0) + 1
```

Now:

```python
{"failed": 1}
```

Second failed job:

```python
counts["failed"] = counts.get("failed", 0) + 1
```

Now:

```python
{"failed": 2}
```

## Skipping Missing Keys

If a job has no `"status"` key, skip it.

Example:

```python
if "status" in job:
    status = job["status"]
    counts[status] = counts.get(status, 0) + 1
```

If `"status"` is missing:

- do not enter the block
- do not crash
- move to the next item

## Why Empty Input Returns `{}`

If the input list is empty:

- the loop never runs
- the dictionary stays empty

So returning `counts` gives:

```python
{}
```

## Recommended Pattern

```python
def count_jobs_by_status(jobs: list[dict]) -> dict[str, int]:
    counts = {}

    for job in jobs:
        if "status" in job:
            status = job["status"]
            counts[status] = counts.get(status, 0) + 1

    return counts
```

## Core Idea To Remember

When you want to count categories:

- use a dictionary
- use the category value as the key
- update with `dict.get(key, 0) + 1`

## Turning Counts Into A Sorted Report

Sometimes you do not want to return the raw dictionary.

You want a stable report string such as:

```text
failed: 2
running: 1
success: 3
```

For that:

- count first
- then sort the keys
- then build the lines

Example idea:

```python
"\n".join(f"{k}: {v}" for k, v in sorted(counts.items()))
```

Why sort?

- dictionary insertion order depends on when keys were first seen
- the requirement might instead ask for alphabetical order

So sorting makes the output stable and requirement-based, not accidental.
