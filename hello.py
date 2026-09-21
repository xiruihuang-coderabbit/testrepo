"""A small greeting CLI for exercising the CodeRabbit review workflow."""

import argparse


def greet(name: str) -> str:
    """Return a greeting, using World for an empty or whitespace-only name."""
    display_name = name.strip() or "World"
    return f"Hello, {display_name}!"


def main() -> None:
    """Parse the command-line name and print its greeting."""
    parser = argparse.ArgumentParser(description="Print a friendly greeting.")
    parser.add_argument("name", nargs="?", default="World")
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
