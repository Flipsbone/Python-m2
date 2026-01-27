#!/usr/bin/env python3.10
"""A simple program to check garden temperature inputs and handle
    exceptions."""


def check_temperature(temp_str: str) -> int | None:
    """
    Check if the given temperature string is valid for plants.
    Valid temperatures are between 0 and 40 degrees Celsius.
    Args:
        temp_str (str): The temperature input as a string.
        Returns:
        int | None: The valid temperature as an integer, or None if invalid.
    """
    try:
        temperature = int(temp_str)
        if temperature > 40:
            print(f"Error: {temperature}°C is too hot for plants (max 40°C)\n")
            return None
        elif temperature < 0:
            print(f"Error: {temperature}°C is too cold for plants (min 0°C)\n")
            return None
        else:
            print(f"Temperature {temperature}°C is perfect for plants!\n")
            return temperature
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None


def test_temperature_input() -> None:
    """Test various temperature inputs to ensure proper exception handling."""
    print("=== Garden Temperature Checker ===\n")
    print("Testing temperature: 25")
    check_temperature("25")
    print("Testing temperature: abc")
    check_temperature("abc")
    print("Testing temperature: 100")
    check_temperature("100")
    print("Testing temperature: -50")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")
