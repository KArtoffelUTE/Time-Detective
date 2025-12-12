import pygame
from tilemaps import TILE_SIZE, tile_colors
from tilemaps import lobby_map, restaurant_map, kitchen_map

class Door:
    def __init__(self, door_id, position, target_room, target_spawn, locked=False):
        self.id = door_id
        self.position = position      # (row, col)
        self.target_room = target_room
        self.target_spawn = target_spawn
        self.locked = locked

class Room:
    def __init__(self, name, floor, tilemap, doors, spawns):
        self.name = name
        self.floor = floor
        self.tilemap = tilemap
        self.doors = doors            # dict: door_id -> Door
        self.spawns = spawns          # dict: spawn_id -> (x, y)

        self.obstacles = self._build_obstacles()

    def _build_obstacles(self):
        obstacles = []
        for r, row in enumerate(self.tilemap):
            for c, tile in enumerate(row):
                if tile in (1, 5, 6):  # Wand, Tresen, Tisch
                    rect = pygame.Rect(
                        c * TILE_SIZE,
                        r * TILE_SIZE,
                        TILE_SIZE,
                        TILE_SIZE
                    )
                    obstacles.append(rect)
        return obstacles

    def draw(self, screen, camera_x, camera_y):
        for r, row in enumerate(self.tilemap):
            for c, tile in enumerate(row):
                x = c * TILE_SIZE - camera_x
                y = r * TILE_SIZE - camera_y
                color = tile_colors.get(tile, (0, 0, 0))
                pygame.draw.rect(screen, color, (x, y, TILE_SIZE, TILE_SIZE))

    def check_for_door(self, player_row, player_col):
        for door in self.doors.values():
            if door.position == (player_row, player_col):
                if door.locked:
                    return None  # Tür ist zu
                return door
        return None
