import pygame
from tilemaps import TILE_SIZE, tile_colors, tile_images

class Door:
    def __init__(self, door_id, position, target_room, target_spawn, locked=False):
        self.id = door_id
        self.position = position      # (row, col)
        self.target_room = target_room
        self.target_spawn = target_spawn
        self.locked = locked

class Stair:
    def __init__(self, stair_id, position, target_room, target_spawn,
                 direction, floor_change, locked=False, label=None):
        self.id = stair_id
        self.position = position          # (row, col)
        self.target_room = target_room
        self.target_spawn = target_spawn
        self.direction = direction        # "up" oder "down"
        self.floor_change = floor_change  # +1 oder -1
        self.locked = locked
        self.label = label


class Room:
    def __init__(self, name, floor, tilemap, doors, stairs, spawns):
        self.name = name
        self.floor = floor
        self.tilemap = tilemap
        self.doors = doors            # dict: door_id -> Door
        self.spawns = spawns          # dict: spawn_id -> (x, y)
        self.stairs = stairs          # dict: stair_id -> Stair
        self.obstacles = self._build_obstacles()

    def _build_obstacles(self):
        obstacles = []
        for r, row in enumerate(self.tilemap):
            for c, tile in enumerate(row):
                if tile in (1, 5, 6, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8):  # Wand, Tresen, Tisch
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

                image = tile_images.get(tile)

                if image:
                    # Bild existiert → zeichnen
                    screen.blit(image, (x, y))
                else:
                    # Kein Bild → fallback auf Farbe
                    color = tile_colors.get(tile, (255, 0, 255))  # Pink = Fehler sichtbar
                    pygame.draw.rect(screen, color, (x, y, TILE_SIZE, TILE_SIZE))

    def check_for_door(self, player_row, player_col):
        for door in self.doors.values():
            if door.position == (player_row, player_col):
                if door.locked:
                    return None  # Tür ist zu
                return door
        return None
    
    def check_for_stair(self, player_row, player_col):
        for stair in self.stairs.values():
            if stair.position == (player_row, player_col):
                if stair.locked:
                    return None
                return stair
        return None


