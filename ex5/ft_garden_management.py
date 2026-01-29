#!/usr/bin/env python3.10

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water_level: int, sun: int):
        self.name = name
        self.water_level = int(water_level)
        self.sun = sun


class GardenManager:

    def __init__(self) -> None:

        self.plants: list[Plant] = []

    def adding_plant(self, name: str, water_level: int, sun: int) -> None:
        """Add a plant to the garden, raising errors for invalid names.
        Args:
            name (str): The name of the plant to add.
        Raises:
            PlantError: If the plant name is empty or not found in catalog.
        """
        if not name.strip():
            raise PlantError("Plant name cannot be empty!")
        new_plant = Plant(name, water_level, sun)
        self.plants.append(new_plant)
        print(f"Added {name} successfully")

    def watering_plants(self) -> None:
        print("Watering plants...")
        print("Opening watering system")
        try:
            for plant in self.plants:
                plant.water_level += 1
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)\n")

    def checking_plants_health(self) -> None:
        print("Checking plant health...")
        for plant in self.plants:
            try:
                if plant.water_level > 10:
                    raise WaterError(
                        f"{plant.name}: Water level {plant.water_level} "
                        "is too high (max 10)")
                print(
                    f"{plant.name}: healthy (water: {plant.water_level}, "
                    f"sun: {plant.sun})")
            except WaterError as e:
                print(f"Error checking {e}\n")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    garden = GardenManager()
    print("Adding plants to garden...")
    plant_data = [("tomato", 4, 8), ("lettuce", 14, 8), ("", 5, 8)]

    for name, water_level, sun in plant_data:
        try:
            garden.adding_plant(name, water_level, sun)
        except PlantError as e:
            print(f"Error adding plant: {e}\n")

    garden.watering_plants()
    garden.checking_plants_health()
    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")
    print("System recovered and continuing...")
    print("Garden management system test complete!")
