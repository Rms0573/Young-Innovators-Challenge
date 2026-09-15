# ============================================================
# SPACE EXPLORER — Your Ship, Your Story
# ============================================================
# Change these values to make the game your own.
# Run the game after each change to see what happens!
# ============================================================

# --- Your ship ---
SHIP_NAME = "The Horizon"
CREW_DESCRIPTION = "A band of explorers seeking fortune at the edge of the galaxy"

# --- Starting resources ---
STARTING_OXYGEN = 100
STARTING_HULL = 100

# --- Galaxy ---
GALAXY_SIZE = 8
USE_CUSTOM_PLANETS = True
PLANETS = ["freddy", "BOBO", "Nere"]
print(PLANETS)
print(len(PLANETS))
print(PLANETS[2])

PLANETS.append({
    "name": "Betty",
    "description": "Bioluminescent forest cover the surface",
    "danger_level": 1,
    "has_water": True,
    "encounter": "empty"
})
PLANETS.append({
    "name": "Franny",
    "description": "A barren world inside an asteroid belt",
    "danger_level": 3,
    "has_water": False,
    "encounter": "asteroid_field"
})