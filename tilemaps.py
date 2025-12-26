import pygame

TILE_SIZE = 32

def get_tile(sheet, x, y, w=16, h=16):
    tile = pygame.Surface((w, h), pygame.SRCALPHA)
    tile.blit(sheet, (0, 0), (x, y, w, h))
    return pygame.transform.scale(tile, (TILE_SIZE, TILE_SIZE))

tile_images = {}
def load_tiles():
    global tile_images

    sprite_sheet = pygame.image.load("assets/Tileset_my.png").convert_alpha()

    floor_carpet = get_tile(sprite_sheet, 0, 0, 16, 16)
    up_wall = get_tile(sprite_sheet, 16, 0, 16, 16)
    down_wall = get_tile(sprite_sheet, 32, 0, 16, 16)
    up_side_wall = get_tile(sprite_sheet, 48, 0, 16, 16)
    left_side_wall = get_tile(sprite_sheet, 64, 0, 16, 16)
    right_side_wall = get_tile(sprite_sheet, 80, 0, 16, 16)
    left_corner_up_wall = get_tile(sprite_sheet, 96, 0, 16, 16)
    right_corner_up_wall = get_tile(sprite_sheet, 112, 0, 16, 16)
    left_corner_down_wall = get_tile(sprite_sheet, 128, 0, 16, 16)
    right_corner_down_wall = get_tile(sprite_sheet, 144, 0, 16, 16)

    tile_images.clear()
    tile_images[0] = floor_carpet
    tile_images[1]= up_wall
    tile_images[1.1] = down_wall
    tile_images[1.2] = up_side_wall
    tile_images[1.3] = left_side_wall
    tile_images[1.4] = right_side_wall
    tile_images[1.5] = left_corner_up_wall
    tile_images[1.6] = right_corner_up_wall
    tile_images[1.7] = left_corner_down_wall
    tile_images[1.8] = right_corner_down_wall


# Farben
tile_colors = {
    0: (200, 200, 200),  # Boden
    1: (100, 100, 100),  # Wand
    1.1: (100, 100, 100), #Wand Seite
    2: (0, 0, 255),      # Treppe hoch
    3: (0, 255, 0),      # Treppe runter
    4: (150, 75, 0),     # Tür
    5: (255, 0, 0),      # Tresen / Arbeitsfläche
    6: (180, 180, 50),   # Tisch
}


# Lobby 
lobby_map = [
    [1.5]+[1.2]*23+[1.6],
]
lobby_map.append([1.3]+[1]*23+[1.4])
row = [1.3] + [4]+ [0]*22 + [1.4]
lobby_map.append(row)
for i in range(17):
    row = [1.3] + [0]*23 + [1.4]
    if i == 2:
        row[5:11] = [5,5,5,5,5,5]  # Tresen
    lobby_map.append(row)
row = [1.3] + [0]*10 + [4] + [0]*9 + [0, 0, 2] + [1.4]
lobby_map.append(row)
lobby_map.append([1.7]+[1.1]*23+[1.8])

#Buero
office = [
    [1.5]+[1.2]*15+[1.6]
]
office.append([1.3]+[1]*15+[1.4])
for i in range(20):
    row = [1.3] + [0]*15 + [1.4]
    office.append(row)
row = [1.3] + [0]*7 + [4] + [0]*7 + [1.4]
office.append(row)
office.append([1.7]+[1.1]*15+[1.8])

# Restaurant 
restaurant_map = [
    [1.5]+ [1.2]*23+[1.6],
]
restaurant_map.append([1.3]+[1]*23+[1.4])
for i in range(40):
    row = [1.3] + [0]*23 + [1.4]
    if i == 5:
        row[5:20:3] = [6,6,6,6,6]  # Tische
    restaurant_map.append(row)
row = [1.3] + [0]*5 + [4] + [0]*11 + [4] + [0]*5 + [1.4]
restaurant_map.append(row)
restaurant_map.append([1.7]+[1.1]*23+[1.8])


# Küche
kitchen_map = [
    [1.5]+[1.2]*13+[1.6],
]
kitchen_map.append([1.3]+[1]*13+[1.4])
for i in range(13):
    row = [1.3] + [0]*13 + [1.4]
    if i == 3:
        row[3:12] = [5]*9  # Arbeitsfläche
    kitchen_map.append(row)
row = [1.3] + [0]*6 + [4] + [0]*6 + [1.4]
kitchen_map.append(row)
kitchen_map.append([1.7]+[1.1]*13+[1.8])


# Flur (2. Etage)
floor2_corridor = [
    [1.5]+[1.2]*25+[1.6]
]
floor2_corridor.append([1.3]+[1]*25+[1.4])
row = [1.3] + [4] + [0]*7 + [4] + [0]*7 + [4] + [0]*7 + [3] + [1.4]
floor2_corridor.append(row)
for i in range(8):
    row = [1.3] + [0]*25 + [1.4]  # langer Gang
    floor2_corridor.append(row)
row = [1.3] + [4] + [0]*7 + [4] + [0]*7 + [4] + [0]*7 + [2] + [1.4]
floor2_corridor.append(row)
# untere Wand
floor2_corridor.append([1.7]+[1.1]*25+[1.8])


# Raum01 (2. Etage)
room01  = [
    [1.5]+[1.2]*13+[1.6]
]
room01.append([1.3] +[1]*13+[1.4])
for i in range(13):
    row = [1.3] + [0]*13 + [1.4]
    room01.append(row)
row = [1.3] + [0]*6 + [4] + [0]*6 + [1.4]
room01.append(row)
room01.append([1.7]+[1.1]*13+[1.8])

# Raum02 (2. Etage)
room02  = [
    [1.5]+[1.2]*13+[1.6]
]
room02.append([1.3] +[1]*13+[1.4])
for i in range(13):
    row = [1.3] + [0]*13 + [1.4]
    room02.append(row)
row = [1.3] + [0]*6 + [4] + [0]*6 + [1.4]
room02.append(row)
room02.append([1.7]+[1.1]*13+[1.8])

# Raum03 (2. Etage)
room03  = [
    [1.5]+[1.2]*13+[1.6]
]
room03.append([1.3] +[1]*13+[1.4])
for i in range(13):
    row = [1.3] + [0]*13 + [1.4]
    room03.append(row)
row = [1.3] + [0]*6 + [4] + [0]*6 + [1.4]
room03.append(row)
room03.append([1.7]+[1.1]*13+[1.8])

# Raum04 (2. Etage)
room04  = [
    [1.5]+[1.2]*13+[1.6]
]
room04.append([1.3] +[1]*13+[1.4])
for i in range(13):
    row = [1.3] + [0]*13 + [1.4]
    room04.append(row)
row = [1.3] + [0]*6 + [4] + [0]*6 + [1.4]
room04.append(row)
room04.append([1.7]+[1.1]*13+[1.8])

# Raum05 (2. Etage)
room05  = [
    [1.5]+[1.2]*13+[1.6]
]
room05.append([1.3] +[1]*13+[1.4])
for i in range(13):
    row = [1.3] + [0]*13 + [1.4]
    room05.append(row)
row = [1.3] + [0]*6 + [4] + [0]*6 + [1.4]
room05.append(row)
room05.append([1.7]+[1.1]*13+[1.8])

# Raum06 (2. Etage)
room06  = [
    [1.5]+[1.2]*13+[1.6]
]
room06.append([1.3] +[1]*13+[1.4])
for i in range(13):
    row = [1.3] + [0]*13 + [1.4]
    room06.append(row)
row = [1.3] + [0]*6 + [4] + [0]*6 + [1.4]
room06.append(row)
room06.append([1.7]+[1.1]*13+[1.8])


#Flur Etage 3
floor3_corridor = [
    [1]*27,  # obere Wand
]
row = [1] + [4] + [0]*11 + [4] + [0]*11 + [3] + [1]
floor3_corridor.append(row)
for i in range(8):
    row = [1] + [0]*25 + [1]  # langer Gang
    floor3_corridor.append(row)
row = [1] + [4] + [0]*11 + [4] + [0]*11 + [2] + [1]
floor3_corridor.append(row)
# untere Wand
floor3_corridor.append([1]*27)

#großer Raum 1
room01_b = [
    [1]*27
]
for i in range(20):
    row = [1] + [0]*25 + [1]
    room01_b.append(row)
row = [1] + [0]*12 + [4] + [0]*12 + [1]
room01_b.append(row)
room01_b.append([1]*27)

#großer Raum 2
room02_b = [
    [1]*27
]
for i in range(20):
    row = [1] + [0]*25 + [1]
    room02_b.append(row)
row = [1] + [0]*12 + [4] + [0]*12 + [1]
room02_b.append(row)
room02_b.append([1]*27)

#großer Raum 3
room03_b = [
    [1]*27
]
for i in range(20):
    row = [1] + [0]*25 + [1]
    room03_b.append(row)
row = [1] + [0]*12 + [4] + [0]*12 + [1]
room03_b.append(row)
room03_b.append([1]*27)

#großer Raum 4
room04_b = [
    [1]*27
]
for i in range(20):
    row = [1] + [0]*25 + [1]
    room04_b.append(row)
row = [1] + [0]*12 + [4] + [0]*12 + [1]
room04_b.append(row)
room04_b.append([1]*27)

#Dachboden
roof = [
    [1]*31
]
for i in range(31):
    if i == 15:
        row = [1] + [0]*14 + [3] + [0]*14 + [1]
    else:
        row = [1] + [0]*29 +[1]
    roof.append(row)
roof.append([1]*31)

#Flur Etage 4
floor4_corridor = [
    [1]*27,  # obere Wand
]
row = [1] + [0] + [0]*11 + [4] + [0]*11 + [3] + [1]
floor4_corridor.append(row)
for i in range(8):
    row = [1] + [0]*25 + [1]  # langer Gang
    floor4_corridor.append(row)
row = [1] + [0] + [0]*11 + [4] + [0]*11 + [2] + [1]
floor4_corridor.append(row)
# untere Wand
floor4_corridor.append([1]*27)

#Schwimmbad
swimming = [
    [1]*27
]
for i in range(11):
    if i == 5:
        row = [1] + [0]*24 +[4] +[1]
    else:
        row = [1] + [0]*25 + [1]
    swimming.append(row)
swimming.append([1]*27)

#Bar
bar = [
    [1]*21
]
for i in range(16):
    row = [1] + [0]*19 + [1]
    bar.append(row)
row = [1] + [0]*9 + [4] + [0]*9 + [1]
bar.append(row)
bar.append([1]*21)