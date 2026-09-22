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