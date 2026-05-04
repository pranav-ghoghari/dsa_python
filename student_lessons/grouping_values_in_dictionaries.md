# Grouping Values In Dictionaries

Sometimes you do not want a single count for each category. You want a list of the matching values for each category.

Example goal:

```python
{
    "failed": [1, 3],
    "running": [2]
}
```

That is different from counting:

```python
{
    "failed": 2,
    "running": 1
}
```

## The Core Pattern

```python
groups = {}

for job in jobs:
    if "status" in job and "id" in job:
        status = job["status"]

        if status not in groups:
            groups[status] = []

        groups[status].append(job["id"])

return groups
```

## Why The Empty List Is Needed

When a status appears for the first time, there is no list there yet.

So this line:

```python
groups[status] = []
```

creates an empty list for that status.

After that, `append(...)` has a real list to add to.

## Why This Is Grouping And Not Counting

In a counting task, each key stores one number:

```python
counts["failed"] = 2
```

In a grouping task, each key stores a list of values:

```python
groups["failed"] = [1, 3]
```

So the question is:

- counting: "how many failed jobs are there?"
- grouping: "which job IDs are failed?"

## Why Order Is Preserved

The loop reads the input list from left to right.

Each time a job matches, you do:

```python
groups[status].append(job["id"])
```

`append(...)` adds to the end of that list.

So each status list keeps the IDs in the same order they were seen in the original input.
