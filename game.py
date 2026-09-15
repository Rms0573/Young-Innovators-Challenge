from engine.display import(
    show_intro,
    show_destination,
    show_encounter,
    show_defeat
)
from engine.galaxy import create_galaxy
from engine.encounters import process_water_planet
from engine.journey import process_encounter
import constants

#function to define if to stop at planet or not
def should_stop() -> None:
    answer = input("Do you want to stop here? if yes, type y, else, type n (y/n):")

    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        print("you either chose, y or n")


def main() -> None:
    oxygen = constants.STARTING_OXYGEN
    hull = constants.STARTING_HULL
    ship_name = constants.SHIP_NAME
    crew_desc = constants.CREW_DESCRIPTION
    galaxy = constants.GALAXY_SIZE
 
    show_intro(ship_name, crew_desc)
    galaxy = create_galaxy(galaxy)
    
# game loop

    for i in range (len(galaxy)):
        destination = galaxy[i]
        oxygen -= 8
        show_destination(destination, i, len(galaxy))

        if should_stop():
            oxygen, hull, narration = process_encounter(destination, oxygen, hull)
            show_encounter(narration)
            if destination["has_water"]:
                oxygen, hull, water_narration = process_water_planet(oxygen, hull)
                show_encounter(water_narration)
        else:
            show_encounter("  You fly past without stopping")

        print(f"  Oxygen levels: {oxygen}, Hull integrity: {hull}")
        if oxygen <= 0:
            show_defeat(ship_name, " Oxygen depleted")
            return
        elif hull <= 0:
            show_defeat(ship_name, "  Hull destroyed")
            return         

if __name__ == "__main__":
    main()
f