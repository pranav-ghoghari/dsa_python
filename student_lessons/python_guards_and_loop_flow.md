# Python Guards And Loop Flow

## What This Lesson Is About

This lesson is about two ideas:

- checking whether a dictionary has the keys you need before reading them
- understanding the difference between "skip this item" and "end the whole function"

## Checking Dictionary Keys Safely

If you write:

```python
job["status"]
```

Python expects the key `"status"` to exist.

If it does not exist, your code crashes with a key error.

To avoid that, first check:

```python
if "status" in job:
```

If this is true, the key exists and it is safe to read:

```python
job["status"]
```

You also learned another related tool:

```python
job.get("status")
```

That returns the value if the key exists, or `None` if it does not.

## What A Guard Means

A guard is just an early safety check before you do the real logic.

Example:

```python
if "status" in job and "retries_left" in job:
```

This means:

- only continue if both keys exist
- otherwise do not enter the block

## Skip Versus Return

Inside a loop, these are very different:

```python
return 0
```

This ends the whole function immediately.

It does not just skip one item.

If you want to skip one non-matching item and keep going, there are two common patterns:

1. Put the real work only inside the `if` block.
2. Use `continue`.

Example:

```python
for job in jobs:
    if "status" in job and "retries_left" in job:
        if job["status"] == "failed" and job["retries_left"] > 0:
            count += 1
```

If the outer `if` is false, Python does not enter that block.

The loop simply moves to the next job.

## Core Idea

Use guards to make code safe.

Use `return` only when you really want to leave the whole function.
