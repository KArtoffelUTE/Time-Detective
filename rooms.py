from room import Room, Door, Stair
from tilemaps import lobby_map, restaurant_map, kitchen_map, floor2_corridor , room01, room02
from tilemaps import TILE_SIZE

rooms = {}

# --- Lobby ---
rooms["lobby"] = Room(
    name="lobby",
    floor=1,
    tilemap=lobby_map,
    doors={
        "to_restaurant": Door(
            "to_restaurant",
            position=(19, 11),
            target_room="restaurant",
            target_spawn="from_lobby"
        )
    },
    stairs={
        "lobby_up": Stair(
            "lobby_up",
            position=(19, 23),      # Tile 2
            target_room="floor2_corridor",
            target_spawn="from_lobby",
            direction="up",
            floor_change=+1
        ),
    },
    spawns={
        "from_restaurant": (11*TILE_SIZE, 18*TILE_SIZE),
        "from_corridor": (21*TILE_SIZE, 18*TILE_SIZE),
        "from_basement": (22*TILE_SIZE, 18*TILE_SIZE),
    }
)

# --- Restaurant ---
rooms["restaurant"] = Room(
    name="restaurant",
    floor=1,
    tilemap=restaurant_map,
    doors={
        "to_lobby": Door(
            "to_lobby",
            position=(41, 6),
            target_room="lobby",
            target_spawn="from_restaurant"
        ),
        "to_kitchen": Door(
            "to_kitchen",
            position=(41, 18),
            target_room="kitchen",
            target_spawn="from_restaurant"
        )
    },
    stairs={},  # Restaurant hat keine Treppen
    spawns={
        "from_lobby": (6*TILE_SIZE, 40*TILE_SIZE),
        "from_kitchen": (18*TILE_SIZE, 40*TILE_SIZE)
    }
)

# --- Küche ---
rooms["kitchen"] = Room(
    name="kitchen",
    floor=1,
    tilemap=kitchen_map,
    doors={
        "to_restaurant": Door(
            "to_restaurant",
            position=(14, 7),
            target_room="restaurant",
            target_spawn="from_kitchen"
        )
    },
    stairs={},  # Küche hat keine Treppen
    spawns={
        "from_restaurant": (7*TILE_SIZE, 13*TILE_SIZE)
    }
)

# --- Flur (2. Etage) ---
rooms["floor2_corridor"] = Room(
    name="floor2_corridor",
    floor=2,
    tilemap=floor2_corridor,
    doors={
        "to_room01": Door(
            "to_room01",
            position=(1, 17),
            target_room="room01",
            target_spawn="from_corridor"
        ),
        "to_room02": Door(
            "to_room02",
            position=(10, 17),
            target_room="room02",
            target_spawn="from_corridor"
        )
    },  
    stairs={
        "floor2_corridor_down": Stair(
            "floor2_corridor_down",
            position=(1, 25),      # Treppe zurück zur Lobby
            target_room="lobby",
            target_spawn="from_corridor",
            direction="down",
            floor_change=-1
        )
    },
    spawns={
        "from_lobby": (21*TILE_SIZE, 2*TILE_SIZE),
        "from_room01": (18*TILE_SIZE, 2*TILE_SIZE),
        "from_room02": (18*TILE_SIZE, 9*TILE_SIZE)
    }
)

# --- Raum01 (2. Etage) ---
rooms["room01"] = Room(
    name="room01",
    floor=2,
    tilemap=room01,
    doors={
        "to_corridor": Door(
            "to_corridor",
            position=(14, 7),
            target_room="floor2_corridor",
            target_spawn="from_room01"
        )
    },
    stairs={},
    spawns={
        "from_corridor": (7*TILE_SIZE, 13*TILE_SIZE)
    }
)

# --- Raum02 (2. Etage) ---
rooms["room02"] = Room(
    name="room02",
    floor=2,
    tilemap=room02,
    doors={
        "to_corridor": Door(
            "to_corridor",
            position=(14, 7),
            target_room="floor2_corridor",
            target_spawn="from_room02"
        )
    },
    stairs={},
    spawns={
        "from_corridor": (7*TILE_SIZE, 13*TILE_SIZE)
    }
)