import pygame

# Tilegröße (wir skalieren später Assets auf diese Größe)
TILE_SIZE = 32

# Beispiel-Lobby-Map (20x15 Tiles)
lobby_map = [
    [1]*25,  # obere Wand
]
# mittlere Reihen mit Boden und Rezeption
for i in range(18):
    row = [1] + [0]*23 + [1]
    if i == 2:
        row[1:7] = [5,5,5,5,5,5]  # Rezeptionstresen
    lobby_map.append(row)
# untere Reihe mit Treppen
row = [1] + [0]*20 + [4] + [2,3] + [1]
lobby_map.append(row)
# untere Wand
lobby_map.append([1]*25)


# Restaurant (25x20 Tiles)
restaurant_map = [
    [1]*25,
]
for i in range(18):
    row = [1] + [0]*23 + [1]
    if i == 5:
        row[5:20:3] = [6,6,6,6,6]  # einfache Platzhalter für Tische
    restaurant_map.append(row)
# Tür zurück zur Lobby
row = [1] + [0]*11 + [4] + [0]*11 + [1]
restaurant_map.append(row)
restaurant_map.append([1]*25)


# Küche (15x15 Tiles)
kitchen_map = [
    [1]*15,
]
for i in range(13):
    row = [1] + [0]*13 + [1]
    if i == 3:
        row[3:12] = [5,5,5,5,5,5,5,5,5]  # Arbeitsfläche
    kitchen_map.append(row)
# Tür zurück zum Restaurant
row = [1] + [0]*6 + [4] + [0]*7 + [1]
kitchen_map.append(row)
kitchen_map.append([1]*15)

# Farben für die Tiles
tile_colors = {
    0: (200, 200, 200),  # Boden
    1: (100, 100, 100),  # Wand
    2: (0, 0, 255),      # Treppe hoch
    3: (0, 255, 0),      # Treppe runter
    4: (150, 75, 0),     # Tür
    5: (255, 0, 0),      # Rezeptionstresen
    6: (180, 180, 50),   # Tisch
}
room_spawns = {
    ("lobby", 1): (200, 500),
    ("restaurant", 1): (420, 550),
    ("kitchen", 1): (260, 400),
}


def get_tilemap(floor, room):
    if floor == 1 and room == "lobby":
        return lobby_map
    elif floor == 1 and room == "restaurant":
        return restaurant_map
    elif floor == 1 and room == "kitchen":
        return kitchen_map
    else:
        raise ValueError("Tilemap nicht gefunden")


def draw_tilemap(screen, camera_x, camera_y, tilemap):
    for row_index, row in enumerate(tilemap):
        for col_index, tile in enumerate(row):
            x = col_index * TILE_SIZE - camera_x
            y = row_index * TILE_SIZE - camera_y
            color = tile_colors.get(tile, (0, 0, 0))
            pygame.draw.rect(screen, color, (x, y, TILE_SIZE, TILE_SIZE))

def get_obstacles(tilemap):
    obstacles = []
    for row_index, row in enumerate(tilemap):
        for col_index, tile in enumerate(row):
            if tile == 1 or tile == 5:  # Wände und Tresen sind solid
                rect = pygame.Rect(col_index * TILE_SIZE,
                                   row_index * TILE_SIZE,
                                   TILE_SIZE, TILE_SIZE)
                obstacles.append(rect)
    return obstacles
