#!/usr/bin/env python3.10

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:

    def __init__(self) -> None:

        self.plants: dict[str, dict] = {}
        self.plants_catalog = {
            'tomato': {'water': 5, 'sun': 8},
            'lettuce': {'water': 15, 'sun': 8},
            ' ': {'water': 0, 'sun': 0}
        }

    def adding_plant(self, name: str) -> None:
        """Add a plant to the garden, raising errors for invalid names.
        Args:
            name (str): The name of the plant to add.
        Raises:
            PlantError: If the plant name is empty or not found in catalog.
        """
        if not name.strip():
            raise PlantError("Plant name cannot be empty!")
        if name not in self.plants_catalog:
            raise PlantError("Plant not found!")
        self.plants[name] = self.plants_catalog[name]
        print(f"Added {name} successfully")

    def watering_plants(self) -> None:
        try:
            print("Opening watering system")
            for plant in self.plants:
                if not isinstance(self.plants[plant]['water'], int):
                    raise WaterError(
                        f"{self.plants[plant]['water']} is not a number")
                self.plants[plant]['water'] += 1
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    garden = GardenManager()
    try:
        print("Adding plants to garden...")
        garden.adding_plant("tomato")
        garden.adding_plant("lettuce")
        garden.adding_plant("")
    except PlantError as e:
        print(f"Error adding plant: {e}\n")

    try:
        print("Watering plants...")
        garden.watering_plants()
    except WaterError as e:
        print(f"Error water level: {e}\n")


test_garden_management()
