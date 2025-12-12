from room import Room, Door
from tilemaps import lobby_map, restaurant_map, kitchen_map, TILE_SIZE

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
    spawns={
        "from_restaurant": (11*TILE_SIZE, 18*TILE_SIZE)
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
    spawns={
        "from_restaurant": (7*TILE_SIZE, 13*TILE_SIZE)
    }
)
