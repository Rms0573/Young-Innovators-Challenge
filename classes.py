class Ship:
    # "data" a.k.a. attrributes
    def __init__(self, 
                 oxygen, 
                 hull, 
                 name, 
                 crew): # constructor
        self.oxygen = oxygen
        self.hull = hull
        self.name = name
        self.crew = crew

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

# special methods
def __str__(self):
    return f""" 
    Ship object with the following parameters:
    oxygen = {self.oxygen}
    hull = {self.hull}
    name = {self.name}"""

# one "instance of the "ship" class
ship_one = Ship(10, 
                100, 
                "Python Crew", 
                "Awesome People")

class AsteroidField:
    def __init__(self, damage):
        self.damage = damage
        pass

class Raider:
    def __init__(self, damage):
        self.damage = damage
        pass

class Trader:
    def __init__(self, oxygen_refill, hull_repair):
        self.oxygen_refill = oxygen_refill
        self.hull_repair = hull_repair
        pass

class EmptySpace:
    pass
    