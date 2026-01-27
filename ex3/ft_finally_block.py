#!/usr/bin/env python 3.10

def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            try:
                print("Watering " + plant)
            except TypeError:
                print(f"Error: Cannot water {plant} - invalid plant!")
                return
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    plant_list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    plant_list2 = ["tomato", None, "carrots"]
    water_plants(plant_list2)
    print("\nCleanup always happens, even with errors!")
