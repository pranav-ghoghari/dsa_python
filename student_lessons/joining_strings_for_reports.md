# Joining Strings For Reports

## What This Lesson Is About

This lesson explains a common pattern:

- collect matching items first
- then turn them into one formatted string without an extra comma at the end

## The Problem With Adding `", "` Every Time

If you do this:

```python
users_text = ""

for user in users:
    if some_condition:
        users_text += user["username"] + ", "
```

then every matching name gets:

- the name
- plus a comma
- plus a space

That means the last name also gets `", "` after it.

Example result:

```python
"pranav, nishi, rushab, "
```

But the required output is:

```python
"pranav, nishi, rushab"
```

So the extra comma and space at the end causes test failures.

## The Cleaner Pattern

Instead of building one string directly, first build a list of names:

```python
names = []
```

Append each matching username:

```python
names.append(user["username"])
```

Then join them with:

```python
", ".join(names)
```

This puts `", "` between items, not after the last one.

## Example

```python
names = ["pranav", "nishi", "rushab"]
text = ", ".join(names)
```

Now `text` becomes:

```python
"pranav, nishi, rushab"
```

No trailing comma.

## When The Values Are Numbers Instead Of Strings

`join()` works on strings.

So this is fine:

```python
names = ["pranav", "nishi"]
", ".join(names)
```

But this is not fine:

```python
ids = [1, 3]
", ".join(ids)
```

That fails because `1` and `3` are integers, not strings.

So first convert each number to a string:

```python
ids = [1, 3]
", ".join(str(i) for i in ids)
```

Now the result becomes:

```python
"1, 3"
```

## Handling The Empty Case

If there are no matching names:

```python
names = []
```

then:

```python
", ".join(names)
```

becomes:

```python
""
```

So for this task, you should handle the empty case separately:

```python
if len(names) == 0:
    return "Active users: none"
```

Otherwise:

```python
return "Active users: " + ", ".join(names)
```

## Recommended Pattern For This Task

```python
def build_active_user_report(users: list[dict]) -> str:
    names = []

    for user in users:
        if "username" in user and "is_active" in user:
            if user["is_active"] is True:
                names.append(user["username"])

    if len(names) == 0:
        return "Active users: none"

    return "Active users: " + ", ".join(names)
```

## Core Idea

When the output is a comma-separated string:

- collect values in a list
- then use `", ".join(list_name)`

If the values are not already strings:

- convert them first, for example with `str(i)`

That is usually cleaner and safer than manually adding commas each time.
