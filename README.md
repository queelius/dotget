# `dotget`: Simple, Exact Addressing

> "Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away."
>
> — Antoine de Saint-Exupéry

**Get a value from a nested data structure using a precise path. Nothing more.**

```python
>>> from dotget import get
>>> data = {"users": [{"name": "Alice", "email": "alice@example.com"}]}
>>> get(data, "users.0.name")
'Alice'
```

## The Philosophy: Do One Thing Well

In the Unix tradition, `dotget` does one thing: get a value from a specific, known location. It doesn't validate, transform, or query. Its goal isn't to be powerful—it's to be **obvious**.

It is the foundation of the `dot` ecosystem's **Addressing Pillar**, representing the first and simplest layer:

1.  **`dotget` (Exact Addressing):** For when you know the *exact* path to a value (e.g., `users.0.name`). It is the simplest tool for the job.
2.  **`dotstar` (Pattern Addressing):** For when you need to gather all items that match a simple wildcard pattern (e.g., `users.*.name`).
3.  **`dotselect` (Advanced Selection):** For when you need more complex queries, including attribute checks, deep searches, and custom logic, powered by the `dotpath` engine.

`dotget` is for when you know exactly where you're going and need the most direct, reliable, and simple way to get there. It embodies the "Principle of Least Power."

## Install

```bash
pip install dotget
```

## Usage

### As a Library

`dotget` provides a single function: `get`.

```python
from dotget import get

data = {"user": {"contacts": [{"type": "email", "value": "alice@example.com"}]}}

# Get a value using a dot-separated path
email = get(data, "user.contacts.0.value")
# -> "alice@example.com"

# Returns None if the path is invalid
city = get(data, "user.address.city")
# -> None
```

### From the Command Line

`dotget` also includes a simple CLI for shell scripting.

```sh
# Extract the version from a package.json file
$ cat package.json | dotget version
"1.2.3"

# Use it in a script to read from a file
$ VERSION=$(dotget package.json version)
$ echo "Building version $VERSION..."
```

## Boundaries: When to Use `dotget`

Use `dotget` when you need to:
✅ Access data from a known, fixed path in an API response.
✅ Write a quick, reliable script that depends on a stable data structure.
✅ Read from a configuration object.
✅ Avoid writing `try/except KeyError/IndexError` chains for simple lookups.

Do **not** use `dotget` when you need to:
❌ Use wildcards (`*` or `**`). **Use `dotstar` or `dotselect`**.
❌ Find an item based on its value (`[key=value]`). **Use `dotselect`**.
❌ Modify data. **Use `dotmod`**.
❌ Transform data into a new shape. **Use `dotpipe`**.

## "Steal This Code"

Don't want a dependency? The core of this library is simple. Copy it.

```python
def get(data, path, default=None):
    """Gets a value from nested data using a dot-separated path."""
    try:
        for segment in path.split('.'):
            if isinstance(data, list) and segment.isdigit():
                data = data[int(segment)]
            elif isinstance(data, dict):
                data = data[segment]
            else:
                return default
        return data
    except (KeyError, IndexError, TypeError):
        return default
```

