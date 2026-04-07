# Unittest Basics

## What This Lesson Is About

This lesson explains the minimum needed to read and write a small test file in this repo.

It covers:

- what a test file is
- how it differs from a normal Python script
- what `import` does
- what `unittest` is
- why there is a `class`
- what `self` means in a test method
- what `self.assertEqual(actual, expected)` checks

## What A Test File Is

A normal Python file usually does the main work.

Examples:

- clean input
- count things
- build a list
- return a result

A test file has a different job.

Its job is to check whether another file's code behaves correctly.

So the function file is the worker.

The test file is the checker.

## Normal Script Versus Test File

Normal script idea:

```python
result = collect_retryable_job_ids(jobs)
print(result)
```

Test file idea:

```python
self.assertEqual(collect_retryable_job_ids(jobs), [10, 30])
```

The first one runs code and shows a result.

The second one checks whether the result matches what you expected.

## What `import` Does

`import` lets one file use code that was written in another file.

Example:

```python
from python_baseline.collect_retryable_job_ids import collect_retryable_job_ids
```

Read that as:

- go to the `python_baseline` folder
- open the file `collect_retryable_job_ids.py`
- bring the function `collect_retryable_job_ids` into this file

So import means:

"Use code that already exists somewhere else."

## What `unittest` Is

`unittest` is Python's built-in testing tool.

It gives you a structure for organizing tests and checking expected results.

Example:

```python
import unittest
```

That line brings in Python's testing tools.

## Why There Is A `class`

In test files, the class is mainly a container that groups related tests together.

Example:

```python
class CollectRetryableJobIdsTests(unittest.TestCase):
```

For now, read that as:

"This is the group of tests for `collect_retryable_job_ids`."

You do not need full object-oriented programming to use this pattern yet.

## What `self` Means

Inside a class method, Python passes in the current object as the first parameter.

That parameter is usually named `self`.

In a test file, the practical meaning is simple:

- write `self` as the first parameter of each test method
- use `self` to access test helper methods such as `assertEqual`

Example:

```python
def test_empty_input(self) -> None:
```

For now, treat `self` as:

"the thing this test method uses to get access to test tools."

## What `assertEqual` Checks

This is the main comparison tool you will use first:

```python
self.assertEqual(actual, expected)
```

It checks whether:

- the actual result from your code
- is equal to the expected result you wrote down

If they are equal, the test passes.

If they are different, the test fails.

Example:

```python
self.assertEqual(collect_retryable_job_ids([]), [])
```

That means:

"I expect this function to return an empty list for empty input."

## Small Full Example

```python
import unittest

from python_baseline.collect_retryable_job_ids import collect_retryable_job_ids


class CollectRetryableJobIdsTests(unittest.TestCase):
    def test_empty_input(self) -> None:
        self.assertEqual(collect_retryable_job_ids([]), [])
```

## How To Read The Example

Line by line:

- `import unittest`
  brings in Python's built-in testing tools
- `from python_baseline.collect_retryable_job_ids import collect_retryable_job_ids`
  imports the function you want to test
- `class CollectRetryableJobIdsTests(unittest.TestCase):`
  creates a group for related tests
- `def test_empty_input(self) -> None:`
  defines one test method
- `self.assertEqual(collect_retryable_job_ids([]), [])`
  checks that the function result matches the expected value

## The Core Pattern

Most beginner tests follow this pattern:

1. build a small input
2. call the function
3. write the expected output
4. compare actual and expected

Example:

```python
def test_returns_ids_in_input_order(self) -> None:
    jobs = [
        {"id": 10, "status": "failed", "retries_left": 2},
        {"id": 20, "status": "running", "retries_left": 5},
        {"id": 30, "status": "failed", "retries_left": 1},
    ]
    self.assertEqual(collect_retryable_job_ids(jobs), [10, 30])
```

## What You Do Not Need Yet

You do not need to understand all of these yet:

- advanced class design
- inheritance details
- other testing libraries
- every kind of assertion method

For the next step, the minimum is enough:

- import the function
- put tests inside a `TestCase` class
- write `test_...` methods
- use `self.assertEqual(actual, expected)`
