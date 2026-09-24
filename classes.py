class Ship:
    # "data" a.k.a. attrributes
    def __init__(self, 
                 oxygen, 
                 hull, 
                 name, 
                 crew, 
                 morale): # constructor
        self.oxygen = oxygen
        self.hull   = hull
        self.name   = name
        self.crew   = crew
        self.morale = morale

    # methods a.k.a "behaviours"
    def check_defeat_status(self):
        if self.oxygen <= 0:
            return " Oxygen depleted"
        elif self.hull <= 0:
            return " Hull destroyed"
        return None

#TODO: Create show_status method to print attributes to the screen
    def show_resources(self):
        print(f"  Oxygen levels: {self.oxygen}, Hull integrity: {self.hull}")

    def use_oxygen(self):
        self.oxygen -= 8

# special methods
def __str__(self):
    return f""" 
    Ship object with the following parameters:
    oxygen = {self.oxygen}
    hull = {self.hull}
    name = {self.name}"""

class AsteroidField:
    def __init__(self, danger_level):
        self.danger_level = danger_level
        self.base_damage = 10
        pass

class Raider:
    def __init__(self, danger_level):
        self.danger_level = danger_level
        self.base_damage = 12
        self.oxygen_cost = 5

    def process(self, ship):
        ship.oxygen -= self.oxygen_cost
        ship.morale -= 5
        return f" Raider attack: -- {self.base_damage} hull, --{self.oxygen_cost}, -5 morale."


class Trader:
    def __init__(self, oxygen_refill, hull_repair):
        self.oxygen_refill = oxygen_refill
        self.hull_repair = hull_repair
        pass

class EmptySpace:

    def process(self, ship):
        ship.morale += 5
        return " Empty space: +5 morale."