"""
dotget - Simple paths for nested data.

A tiny library for accessing nested data structures using dot notation.
No dependencies. No magic. Just simple paths.

Basic usage:
    >>> from dotget import get, Path
    >>> data = {"user": {"name": "Alice", "email": "alice@example.com"}}
    >>> get(data, "user.name")
    'Alice'

Or steal this code - it's designed to be copied.
"""

__version__ = "1.0.0"
__all__ = ["get", "exists", "Path"]


def get(data, path, default=None):
    """
    Get value at dot-path from nested data.

    Args:
        data: The nested data structure (dict, list, or any object)
        path: Dot-separated path string (e.g., "user.name", "items.0")
        default: Value to return if path not found

    Returns:
        Value at path, or default if not found

    Examples:
        >>> data = {"user": {"name": "Alice"}}
        >>> get(data, "user.name")
        'Alice'
        >>> get(data, "user.email", "none@example.com")
        'none@example.com'
        >>> get(data, "items.0.price", 0)
        0
    """
    if isinstance(path, Path):
        path = str(path)

    try:
        for segment in path.split('.'):
            data = data[int(segment)] if segment.isdigit() else data[segment]
        return data
    except (KeyError, IndexError, TypeError, AttributeError):
        return default


def exists(data, path):
    """
    Check if path exists in data.

    Args:
        data: The nested data structure
        path: Dot-separated path string

    Returns:
        True if path exists, False otherwise

    Examples:
        >>> data = {"user": {"name": "Alice"}}
        >>> exists(data, "user.name")
        True
        >>> exists(data, "user.email")
        False
    """
    sentinel = object()
    return get(data, path, sentinel) is not sentinel


class Path:
    """
    A path object for composable data access.

    Examples:
        >>> p = Path("user.name")
        >>> p.get({"user": {"name": "Alice"}})
        'Alice'

        >>> # Path composition
        >>> user = Path("user")
        >>> name = user / "name"
        >>> str(name)
        'user.name'
    """

    def __init__(self, path=""):
        """Create a path from string."""
        self.path = path

    def __str__(self):
        """String representation of path."""
        return self.path

    def __repr__(self):
        """Developer representation."""
        return f"Path({self.path!r})"

    def __truediv__(self, other):
        """
        Join paths using / operator.

        Examples:
            >>> user = Path("user")
            >>> email = user / "email"
            >>> str(email)
            'user.email'
        """
        if isinstance(other, Path):
            other = str(other)

        if not self.path:
            return Path(other)
        if not other:
            return Path(self.path)

        return Path(f"{self.path}.{other}")

    def get(self, data, default=None):
        """Get value from data using this path."""
        return get(data, self.path, default)

    def exists(self, data):
        """Check if this path exists in data."""
        return exists(data, self.path)


# Steal This Section
# ==================
# If you just need basic path access, copy this function:

def simple_get(data, path, default=None):
    """
    Minimal dot-path accessor in ~10 lines.
    Copy this into your project if you don't want the dependency.
    """
    try:
        for segment in path.split('.'):
            data = data[int(segment)] if segment.isdigit() else data[segment]
        return data
    except (KeyError, IndexError, TypeError, AttributeError):
        return default
