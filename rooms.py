from room import Room, Door, Stair
from tilemaps import lobby_map, restaurant_map, kitchen_map, floor2_corridor , room01, room02, room03, room04, room05, room06, floor3_corridor, room01_b, room02_b, room03_b
from tilemaps import roof, floor4_corridor, swimming
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
        "from_restaurant": (10*TILE_SIZE, 18*TILE_SIZE),
        "from_corridor": (21*TILE_SIZE, 18*TILE_SIZE),
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
        "from_lobby": (5*TILE_SIZE, 40*TILE_SIZE),
        "from_kitchen": (17*TILE_SIZE, 40*TILE_SIZE)
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
        "from_restaurant": (6*TILE_SIZE, 13*TILE_SIZE)
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
        ),
        "to_room03": Door(
            "to_room03",
            position=(1, 9),
            target_room="room03",
            target_spawn="from_corridor"
        ),
        "to_room04": Door(
            "to_room04",
            position=(10, 9),
            target_room="room04",
            target_spawn="from_corridor"
        ),
        "to_room05": Door(
            "to_room05",
            position=(1, 1),
            target_room="room05",
            target_spawn="from_corridor"
        ),
        "to_room06": Door(
            "to_room06",
            position=(10, 1),
            target_room="room06",
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
        ),
        "floor2_corridor_up": Stair(
            "floor2_corridor_up",
            position=(10, 25),
            target_room="floor3_corridor",
            target_spawn="from_floor2_corridor",
            direction="up",
            floor_change=-1
        )
    },
    spawns={
        "from_lobby": (21*TILE_SIZE, 2*TILE_SIZE),
        "from_room01": (18*TILE_SIZE, 2*TILE_SIZE),
        "from_room02": (18*TILE_SIZE, 9*TILE_SIZE),
        "from_room03": (10*TILE_SIZE, 2*TILE_SIZE),
        "from_room04": (10*TILE_SIZE, 9*TILE_SIZE),
        "from_room05": (2*TILE_SIZE, 2*TILE_SIZE),
        "from_room06": (2*TILE_SIZE, 9*TILE_SIZE),
        "from_floor3_corridor": (21*TILE_SIZE, 9*TILE_SIZE)
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
        "from_corridor": (6*TILE_SIZE, 13*TILE_SIZE)
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
        "from_corridor": (6*TILE_SIZE, 13*TILE_SIZE)
    }
)

# --- Raum03 (2. Etage) ---
rooms["room03"] = Room(
    name="room03",
    floor=2,
    tilemap=room03,
    doors={
        "to_corridor": Door(
            "to_corridor",
            position=(14, 7),
            target_room="floor2_corridor",
            target_spawn="from_room03"
        )
    },
    stairs={},
    spawns={
        "from_corridor": (6*TILE_SIZE, 13*TILE_SIZE)
    }
)

# --- Raum04 (2. Etage) ---
rooms["room04"] = Room(
    name="room04",
    floor=2,
    tilemap=room04,
    doors={
        "to_corridor": Door(
            "to_corridor",
            position=(14, 7),
            target_room="floor2_corridor",
            target_spawn="from_room04"
        )
    },
    stairs={},
    spawns={
        "from_corridor": (6*TILE_SIZE, 13*TILE_SIZE)
    }
)

# --- Raum05 (2. Etage) ---
rooms["room05"] = Room(
    name="room05",
    floor=2,
    tilemap=room05,
    doors={
        "to_corridor": Door(
            "to_corridor",
            position=(14, 7),
            target_room="floor2_corridor",
            target_spawn="from_room05"
        )
    },
    stairs={},
    spawns={
        "from_corridor": (6*TILE_SIZE, 13*TILE_SIZE)
    }
)

# --- Raum06 (2. Etage) ---
rooms["room06"] = Room(
    name="room06",
    floor=2,
    tilemap=room06,
    doors={
        "to_corridor": Door(
            "to_corridor",
            position=(14, 7),
            target_room="floor2_corridor",
            target_spawn="from_room06"
        )
    },
    stairs={},
    spawns={
        "from_corridor": (6*TILE_SIZE, 13*TILE_SIZE)
    }
)


# --- Flur (3. Etage) ---
rooms["floor3_corridor"] = Room(
    name="floor3_corridor",
    floor=3,
    tilemap=floor3_corridor,
    doors={
        "to_room01_b": Door(
            "to_room01_b",
            position=(1, 13),
            target_room="room01_b",
            target_spawn="from_corridor"
        ),
        "to_room02_b": Door(
            "to_room02_b",
            position=(10, 13),
            target_room="room02_b",
            target_spawn="from_corridor"
        ),
        "to_room03_b": Door(
            "to_room03_b",
            position=(1, 1),
            target_room="room03_b",
            target_spawn="from_corridor"
        ),
        "to_room04_b": Door(
            "to_room04_b",
            position=(10, 1),
            target_room="room04_b",
            target_spawn="from_corridor"
        )
    },
    stairs={
        "floor3_corridor_down": Stair(
            "floor3_corridor_down",
            position=(1, 25),     
            target_room="floor2_corridor",
            target_spawn="from_floor3_corridor",
            direction="down",
            floor_change=-1
        ),
        "floor3_corridor_up": Stair(
            "floor3_corridor_up",
            position=(10, 25),
            target_room="floor4_corridor",
            target_spawn="from_floor3_corridor",
            direction="up",
            floor_change=+1
        )
    },
    spawns={
        "from_floor2_corridor": (21*TILE_SIZE, 2*TILE_SIZE),
        "from_room01_b": (14*TILE_SIZE, 2*TILE_SIZE),
        "from_room02_b": (14*TILE_SIZE, 9*TILE_SIZE),
        "from_room03_b": (2*TILE_SIZE, 2*TILE_SIZE),
        "from_room04_b": (2*TILE_SIZE, 9*TILE_SIZE),
        "from_floor4_corridor": (21*TILE_SIZE, 9*TILE_SIZE)
    }
)

rooms["room01_b"] = Room(
    name="room01_b",
    floor=3,
    tilemap=room01_b,
    doors={
        "to_corridor": Door(
            "to_corridor",
            position=(21, 13),
            target_room="floor3_corridor",
            target_spawn="from_room01_b"
        )
    },
    stairs={},
    spawns={
        "from_corridor": (14*TILE_SIZE, 20*TILE_SIZE)
    }
)

rooms["room02_b"] = Room(
    name="room02_b",
    floor=3,
    tilemap=room02_b,
    doors={
        "to_corridor": Door(
            "to_corridor",
            position=(21, 13),
            target_room="floor3_corridor",
            target_spawn="from_room02_b"
        )
    },
    stairs={},
    spawns={
        "from_corridor": (14*TILE_SIZE, 20*TILE_SIZE)
    }
)

rooms["room03_b"] = Room(
    name="room03_b",
    floor=3,
    tilemap=room03_b,
    doors={
        "to_corridor": Door(
            "to_corridor",
            position=(21, 13),
            target_room="floor3_corridor",
            target_spawn="from_room03_b"
        )
    },
    stairs={},
    spawns={
        "from_corridor": (14*TILE_SIZE, 20*TILE_SIZE)
    }
)

rooms["room04_b"] = Room(
    name="room04_b",
    floor=3,
    tilemap=room03_b,
    doors={
        "to_corridor": Door(
            "to_corridor",
            position=(21, 13),
            target_room="floor3_corridor",
            target_spawn="from_room04_b"
        )
    },
    stairs={},
    spawns={
        "from_corridor": (14*TILE_SIZE, 20*TILE_SIZE)
    }
)

rooms["floor4_corridor"] = Room(
    name="floor4_corridor",
    floor=4,
    tilemap=floor4_corridor,
    doors={
        "to_swimming": Door(
            "to_swimming",
            position=(1, 13),
            target_room="swimming",
            target_spawn="from_corridor"
        )
    },
    stairs={
        "floor4_corridor_down": Stair(
            "floor4_corridor_down",
            position=(1, 25),     
            target_room="floor3_corridor",
            target_spawn="from_floor4_corridor",
            direction="down",
            floor_change=-1
        )
    },
    spawns={
        "from_floor3_corridor": (21*TILE_SIZE, 2*TILE_SIZE),
        "from_swimming": (14*TILE_SIZE, 2*TILE_SIZE)
    },
)

rooms["swimming"] = Room(
    name="swimming",
    floor=4,
    tilemap=swimming,
    doors={
        "to_corridor": Door(
            "to_corridor",
            position=(6, 25),
            target_room="floor4_corridor",
            target_spawn="from_swimming"
        )
    },
    stairs={},
    spawns={
        "from_corridor": (24*TILE_SIZE, 4*TILE_SIZE)
    }
)

rooms["roof"] = Room(
    name="roof",
    floor=5,
    tilemap=roof,
    doors={},
    stairs={
        "to_corridor": Stair(
            "to_corridor",
            position=(16, 15),
            target_room="floor4_corridor",
            target_spawn="from_roof",
            direction="down",
            floor_change=-1
        )
    },
    spawns={
        "from_corridor": (17*TILE_SIZE, 17*TILE_SIZE)
    }
)