# Unittest Basics

## What This Lesson Is About

This lesson explains the minimum needed to read and write a small test file in this repo.

It covers:

- what a test file is
- how it differs from a normal Python script
- what `import` does
- what `unittest` is
- why there is a `class`
- why the class inherits from `unittest.TestCase`
- what `self` means in a test method
- what `self.assertEqual(actual, expected)` checks
- how the test runner finds and runs test methods
- why test methods usually return `None`

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

`import` can be used for:

- your own repo files
- Python's built-in modules such as `unittest`
- installed third-party libraries

## What `unittest` Is

`unittest` is Python's built-in testing tool.

It gives you a structure for organizing tests and checking expected results.

Example:

```python
import unittest
```

That line brings in Python's testing tools.

More precisely:

- `unittest` is a module from Python's standard library
- "standard library" means it comes with Python
- so you do not have to install it separately

## Why There Is A `class`

In test files, the class is mainly a container that groups related tests together.

Example:

```python
class CollectRetryableJobIdsTests(unittest.TestCase):
```

For now, read that as:

"This is the group of tests for `collect_retryable_job_ids`."

You do not need full object-oriented programming to use this pattern yet.

## Why The Class Inherits From `unittest.TestCase`

This part:

```python
class CollectRetryableJobIdsTests(unittest.TestCase):
```

does two useful things:

- it makes a group for related tests
- it gives the class access to testing tools from `TestCase`

Because it inherits from `unittest.TestCase`, the methods inside can use things like:

- `self.assertEqual(...)`

and the test runner knows:

- this class contains tests

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

More precisely:

- when Python runs a method on an object, it passes that object in as the first argument
- inside a test method, `self` is the current test-case object
- that is why `self.assertEqual(...)` works

You do not invent the value of `self` yourself.

Python passes it in automatically when the method is called.

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

Important detail:

- `assertEqual` is not mainly used like a normal function that returns `True` or `False` for you to store
- if the values match, the test keeps going
- if they do not match, `unittest` marks the test as failed

## Small Full Example

```python
import unittest

from python_baseline.collect_retryable_job_ids import collect_retryable_job_ids


class CollectRetryableJobIdsTests(unittest.TestCase):
    def test_empty_input(self) -> None:
        self.assertEqual(collect_retryable_job_ids([]), [])
```

## How The Test Runner Knows What To Run

When you run:

```python
python -m unittest tests.test_collect_retryable_job_ids -v
```

`unittest` looks for:

- classes that inherit from `unittest.TestCase`
- methods whose names start with `test_`

So in a class like this:

```python
class CollectRetryableJobIdsTests(unittest.TestCase):
    def test_a(self) -> None:
        ...

    def test_b(self) -> None:
        ...
```

both `test_a` and `test_b` will be run.

That is why your file can have three test methods and all three get executed.

## How To Read The Run Command

Example:

```bash
python -m unittest tests.test_collect_retryable_job_ids -v
```

Read it like this:

- `python`
  starts Python
- `-m unittest`
  tells Python to run the standard-library module `unittest` as a program
- `tests.test_collect_retryable_job_ids`
  is the module path of the test file you want to run
- `-v`
  means verbose, so you get one output line per test

Important precision:

- `tests.test_collect_retryable_job_ids` is not "all unittest modules from the tests folder"
- it is one specific test module
- the dots act like folder/file separators in module notation

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

## Why The Parameter List Is Just `self`

You asked why the method is written like this:

```python
def test_multiple_jobs(self) -> None:
```

instead of something like:

```python
def test_multiple_jobs(self, actual) -> expected:
```

The reason is:

- the test runner calls the test method for you
- it does not know what `actual` or `expected` parameters you want
- so test methods are written with no user-supplied input parameters
- inside the method body, you build the input, call the function, and write the expected result there

Example:

```python
def test_multiple_jobs(self) -> None:
    jobs = [
        {"id": 1, "status": "failed", "retries_left": 1},
        {"id": 2, "status": "completed", "retries_left": 2},
        {"id": 3, "status": "failed", "retries_left": 4},
    ]
    actual = collect_retryable_job_ids(jobs)
    expected = [1, 3]
    self.assertEqual(actual, expected)
```

Here:

- `jobs`, `actual`, and `expected` are local variables inside the test
- they are not function parameters

## Why The Return Type Is `-> None`

This part:

```python
def test_multiple_jobs(self) -> None:
```

means:

- this method does not return a useful value

That matches how tests work.

The point of a test is not to return some data to another part of your program.

The point is to perform checks.

So test methods usually:

- set up data
- call code
- assert expectations
- return nothing useful

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
- remember that the runner finds `TestCase` classes and `test_...` methods automatically
