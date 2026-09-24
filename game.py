from engine.display import(
    show_intro,
    show_destination,
    show_encounter,
    show_defeat,
    show_victory
)
from engine.galaxy import create_galaxy
from engine.encounters import process_water_planet
from engine.journey import process_encounter 
import constants
from classes import Ship
from functions import check_defeat_status, scan_destination, process_destination, show_resources

#function to define if to stop at planet or not
def should_stop() -> None:
    answer = input("  Do you want to stop here? if yes, Type y, else, Type n (y/n):")
    if answer == "y":
        return True
    else:
        return False

def main() -> None:

# TODO: create and instance of ship class
    ship = Ship(constants.STARTING_OXYGEN, 
                constants.STARTING_HULL, 
                constants.SHIP_NAME, 
                constants.CREW_DESCRIPTION)

    show_intro(ship.name, ship.crew)
    galaxy = create_galaxy(constants.GALAXY_SIZE)
    
# game loop
    for i in range (len(galaxy)):
        destination = galaxy[i]
        ship.use_oxygen()
        show_destination(destination, i, len(galaxy))
        scan_destination(destination) 
        process_destination(destination, ship)
        ship.show_resources()
        cause = ship.check_defeat_status()

        if cause:
            show_defeat(ship.name, cause)
            return
        
    show_victory(ship.name)         

if __name__ == "__main__":
    main()