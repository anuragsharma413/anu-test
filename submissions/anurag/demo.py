"""A tiny demo: greet a name and compute its length."""


def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}! Your name has {len(name)} characters."


if __name__ == "__main__":
    import sys

    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(greet(name))