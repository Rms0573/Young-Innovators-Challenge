from engine.display import(
)
from engine.galaxy import create_galaxy
from engine.encounters import process_water_planet
from engine.journey import process_encounter
import constants
from classes import Ship

#function to define if to stop at planet or not
def should_stop() -> None:
    answer = input("Do you want to stop here? if yes, type y, else, type n (y/n):")
    if answer == "y":
        return True
    elif answer == "n":
        return False
  
def check_defeat_status(oxygen, hull):
    if oxygen <= 0:
        return " Oxygen depleted"
    elif hull <= 0:
        return " Hull destroyed"
    return None

def scan_destination(planet):
    danger_level = planet["danger_level"]
    if danger_level < 3: # 1 or 2
        return "SAFE"
    elif danger_level == 3:
        return "RISKY"
    return "DANGEROUS"

def process_destination(destination, ship):
    if should_stop():
        ship.oxygen, ship.hull, narration = process_encounter(destination, ship.oxygen, ship.hull)
        show_encounter(narration)
        if destination["has_water"]:
            ship.oxygen, ship.hull, water_narration = process_water_planet(ship.oxygen, ship.hull)
            show_encounter(narration)
    else:
        show_encounter("  You fly past without stopping")
    return ship.oxygen, ship.hull

