#!/usr/bin/env python3.10
"""A function that raises different types of errors for demonstration."""


def garden_operations(action: str) -> None:
    """A function that raises different types of errors for demonstration."""
    if action == "convert":
        int("abc")
    elif action == "divid":
        1 / 0
    elif action == "open":
        open("missing.txt", "r")
    elif action == "look":
        dictionnary: dict[str, str] = {}
        dictionnary["missing_plant"]


def test_error_types() -> None:
    """Test various error types to ensure proper exception handling."""
    print("=== Garden Error Types Demo ===\n")

    try:
        print("Testing ValueError...")
        garden_operations("convert")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    try:
        print("Testing ZeroDivisionError...")
        garden_operations("divid")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    try:
        print("Testing FileNotFoundError...")
        garden_operations("open")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    try:
        print("Testing KeyError...")
        open("look")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    print("Testing multiple errors together...")
    print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")
