"""A small starting point for your project's public Python API."""


def greet(name: str) -> str:
    """Return a greeting for a non-empty name.

    :param name: Person or caller to greet.
    :raises ValueError: If the name is empty or only whitespace.
    """
    if not name.strip():
        raise ValueError("Name must not be empty")
    return f"Hello, {name}!"
