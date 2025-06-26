# dotget

**Simple paths for nested data. Nothing more.**

```python
>>> from dotget import get
>>> data = {"users": [{"name": "Alice", "email": "alice@example.com"}]}
>>> get(data, "users.0.name")
'Alice'
```

That's it. That's the library.

## Why?

Because sometimes you just need to get `data["users"][0]["name"]` without all the ceremony.

Because sometimes you don't want to `pip install` another 50 dependencies.

Because sometimes the best code is the code you understand completely.

## Install

```bash
pip install dotget
```

Or just copy the 20 lines of code you need. Seriously. This library is designed to be stolen.

## The Simplest Thing That Could Work

```python
from dotget import get

data = {
    "user": {
        "name": "Alice",
        "contacts": [
            {"type": "email", "value": "alice@example.com"},
            {"type": "phone", "value": "555-1234"}
        ]
    }
}

# Get nested values
name = get(data, "user.name")                      # "Alice"
email = get(data, "user.contacts.0.value")         # "alice@example.com"

# With defaults
city = get(data, "user.address.city", "Unknown")   # "Unknown"

# Check existence  
from dotget import exists
if exists(data, "user.contacts"):
    print("User has contacts")
```

## The Zen of dotget

- **Flat is better than nested** - but sometimes data is nested
- **Simple is better than complex** - this is just dots and integers
- **Readability counts** - `user.name` is obvious
- **Practicality beats purity** - copy this code if you want
- **There should be one obvious way** - dots traverse, numbers index

## When to use dotget

✅ You have nested data from an API  
✅ You're writing a quick script  
✅ You need to access config values  
✅ You're tired of writing `try`/`except` for nested access  

## When NOT to use dotget

❌ You need wildcards or pattern matching (wait for `dotstar`)  
❌ You need to modify data (this is for reading)  
❌ You need type validation (use Pydantic)  
❌ You need SQL-like queries (use JMESPath)  

## Path Objects (if you need them)

For slightly more complex use cases:

```python
from dotget import Path

# Compose paths
users = Path("users")
first_user = users / "0"
user_name = first_user / "name"

# Use paths
name = user_name.get(data)

# Reuse paths
USER_EMAIL = Path("user.contact.email")
email = USER_EMAIL.get(data)
```

## Steal This Code

Don't want a dependency? Copy this:

```python
def get(data, path, default=None):
    try:
        for segment in path.split('.'):
            data = data[int(segment)] if segment.isdigit() else data[segment]
        return data
    except (KeyError, IndexError, TypeError, AttributeError):
        return default
```

That's it. That's 90% of the library.

## Philosophy

In the Unix tradition, this tool does one thing: navigate to a specific location in nested data. It doesn't validate, transform, or query. It just gets values.

The goal isn't to be powerful - it's to be obvious. When you see `get(data, "user.name")`, you know exactly what it does. No documentation needed.

## Prior Art

This isn't a new idea. It's been reinvented many times because it's useful:

- [dpath](https://github.com/akesterson/dpath-python) - wildcards and searching
- [dotty-dict](https://github.com/pawelzny/dotty_dict) - dict wrapper with dot access  
- [jmespath](https://jmespath.org/) - full query language
- Every project that has a `get_nested()` utility

`dotget` is the minimal version. One function, one syntax, one purpose.

## License

MIT. Do whatever you want with this code.

---

*"Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away."* - Antoine de Saint-Exupéry
