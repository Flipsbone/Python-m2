#!/usr/bin/env python3.10

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass

class GardenManager:

    def __init__(self, name: str)-> None :
        self.plants: dict[str,dict] = {}

    def add_plant(self, name: str)-> None :
        if name not in self.plants:
            self.plants.append(name)
          
def test_garden_management()
    print("=== Garden Management System ===\n")

    try:
        print(add_plant(self, name))