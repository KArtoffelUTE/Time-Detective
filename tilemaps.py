import pygame

TILE_SIZE = 32

# Farben
tile_colors = {
    0: (200, 200, 200),  # Boden
    1: (100, 100, 100),  # Wand
    2: (0, 0, 255),      # Treppe hoch
    3: (0, 255, 0),      # Treppe runter
    4: (150, 75, 0),     # Tür
    5: (255, 0, 0),      # Tresen / Arbeitsfläche
    6: (180, 180, 50),   # Tisch
}


# Lobby 
lobby_map = [
    [1]*25,
]
for i in range(18):
    row = [1] + [0]*23 + [1]
    if i == 2:
        row[5:11] = [5,5,5,5,5,5]  # Tresen
    lobby_map.append(row)
row = [1] + [0]*10 + [4] + [0]*9 + [0, 0, 2] + [1]
lobby_map.append(row)
lobby_map.append([1]*25)


# Restaurant 
restaurant_map = [
    [1]*25,
]
for i in range(40):
    row = [1] + [0]*23 + [1]
    if i == 5:
        row[5:20:3] = [6,6,6,6,6]  # Tische
    restaurant_map.append(row)
row = [1] + [0]*5 + [4] + [0]*11 + [4] + [0]*5 + [1]
restaurant_map.append(row)
restaurant_map.append([1]*25)


# Küche
kitchen_map = [
    [1]*15,
]
for i in range(13):
    row = [1] + [0]*13 + [1]
    if i == 3:
        row[3:12] = [5]*9  # Arbeitsfläche
    kitchen_map.append(row)
row = [1] + [0]*6 + [4] + [0]*6 + [1]
kitchen_map.append(row)
kitchen_map.append([1]*15)


# Flur (2. Etage)
floor2_corridor = [
    [1]*27,  # obere Wand
]
row = [1] + [4] + [0]*7 + [4] + [0]*7 + [4] + [0]*7 + [3] + [1]
floor2_corridor.append(row)
for i in range(8):
    row = [1] + [0]*25 + [1]  # langer Gang
    floor2_corridor.append(row)
row = [1] + [4] + [0]*7 + [4] + [0]*7 + [4] + [0]*8 + [1]
floor2_corridor.append(row)
# untere Wand
floor2_corridor.append([1]*27)


# Raum01 (2. Etage)
room01  = [
    [1]*15
]
for i in range(13):
    row = [1] + [0]*13 + [1]
    room01.append(row)
row = [1] + [0]*6 + [4] + [0]*6 + [1]
room01.append(row)
room01.append([1]*15)

# Raum02 (2. Etage)
room02  = [
    [1]*15
]
for i in range(13):
    row = [1] + [0]*13 + [1]
    room02.append(row)
row = [1] + [0]*6 + [4] + [0]*6 + [1]
room02.append(row)
room02.append([1]*15)

# Raum03 (2. Etage)
room03  = [
    [1]*15
]
for i in range(13):
    row = [1] + [0]*13 + [1]
    room03.append(row)
row = [1] + [0]*6 + [4] + [0]*6 + [1]
room03.append(row)
room03.append([1]*15)