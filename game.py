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
 
    show_intro(constants.SHIP_NAME, constants.CREW_DESCRIPTION)
    galaxy = create_galaxy(constants.GALAXY_SIZE)
    
# game loop

    for i in range (len(galaxy)):
        destination = galaxy[i]
        oxygen -= 8


if __name__ == "__main__":
    main()
