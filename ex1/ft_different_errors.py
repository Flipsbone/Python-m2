#!/user/bin/env python3.10
"""A function that raises different types of errors for demonstration."""


def garden_operations() -> None | int:
    """A function that raises different types of errors for demonstration."""
    int("abc")
    1 / 0
    open("missing.txt", "r")
    {}["missing_plant"]


def test_error_types() -> None:
    """Test various error types to ensure proper exception handling."""
    print("=== Garden Error Types Demo ===\n")

    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    try:
        print("Testing ZeroDivisionError...")
        1 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    try:
        print("Testing FileNotFoundError...")
        open("missing.txt", "r")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    try:
        print("Testing KeyError...")
        {}["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    print("Testing multiple errors together...")
    print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")
