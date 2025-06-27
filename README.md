# `dotget`: Simple, Exact Addressing

**Get a value from a nested data structure. Nothing more.**

```python
>>> from dotget import get
>>> data = {"users": [{"name": "Alice", "email": "alice@example.com"}]}
>>> get(data, "users.0.name")
'Alice'
```

## The Philosophy: Do One Thing Well

In the Unix tradition, `dotget` does one thing: get a value from a specific, known location. It doesn't validate, transform, or query. Its goal isn't to be powerful—it's to be **obvious**.

It is the foundation of the `dot` ecosystem's **Addressing Layer**:

*   **`dotget` provides exact addressing:** `users.0.name`
*   `dotstar` builds on this with pattern addressing: `users.*.name`
*   `dotquery` completes it with conditional addressing: `users[name=Alice]`

`dotget` is for when you know exactly where you're going and need the most direct, reliable, and simple way to get there. It embodies the "Principle of Least Power": use the simplest possible tool for the job.

## Install

```bash
pip install dotget
```

## Usage

### As a Library

`dotget` provides two functions: `get` and `exists`.

```python
from dotget import get, exists

data = {"user": {"contacts": [{"type": "email", "value": "alice@example.com"}]}}

# Get a value using a dot-separated path
email = get(data, "user.contacts.0.value")
# -> "alice@example.com"

# Return a default value if the path is invalid
city = get(data, "user.address.city", "Unknown")
# -> "Unknown"

# Check if a path is valid
if exists(data, "user.contacts.1"):
    print("User has a second contact.")
# -> (no output)
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
✅ Access data from an API response.
✅ Write a quick, reliable script.
✅ Read from a configuration object.
✅ Avoid writing `try/except KeyError/IndexError` chains.

Do **not** use `dotget` when you need to:
❌ Use wildcards (`*` or `**`). **Use `dotstar` or `dotpath`**.
❌ Find an item based on its value (`[key=value]`). **Use `dotpath`**.
❌ Modify data. **Use `dotmod`**.
❌ Transform data into a new shape. **Use `dotpipe`**.

## "Steal This Code"

Don't want a dependency? The core of this library is one function. Copy it.

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
    except (KeyError, IndexError, TypeError, AttributeError):
        return default
```

## License

MIT. Do whatever you want with this code.

> "Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away." - Antoine de Saint-Exupéry
