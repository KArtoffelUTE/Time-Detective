import pygame, sys
from player import Player
from tilemaps import get_tilemap, TILE_SIZE

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Time Detective")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

current_floor = 1
current_room = "lobby"
tilemap = get_tilemap(current_floor, current_room)

def draw_tilemap(screen, camera_x, camera_y, tilemap):
    for row_index, row in enumerate(tilemap):
        for col_index, tile in enumerate(row):
            x = col_index * TILE_SIZE - camera_x
            y = row_index * TILE_SIZE - camera_y

            if tile == 0:  # Boden
                color = (200, 200, 200)
            elif tile == 1:  # Wand
                color = (100, 100, 100)
            elif tile == 2:  # Treppe
                color = (0, 0, 255)
            elif tile == 3: #Treppe runter
                color = (0, 255, 0)

            pygame.draw.rect(screen, color, (x, y, TILE_SIZE, TILE_SIZE))

def get_obstacles(tilemap):
    obstacles = []
    for row_index, row in enumerate(tilemap):
        for col_index, tile in enumerate(row):
            if tile == 1:  # nur Wände sind solid
                rect = pygame.Rect(col_index * TILE_SIZE,
                                   row_index * TILE_SIZE,
                                   TILE_SIZE, TILE_SIZE)
                obstacles.append(rect)
    return obstacles



player = Player(400, 300)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    keys = pygame.key.get_pressed()
    obstacles = get_obstacles(tilemap)
    player.update(keys, obstacles)
    # Treppen-Check
    row = player.rect.centery // TILE_SIZE
    col = player.rect.centerx // TILE_SIZE

    if tilemap[row][col] == 2:  # Treppe nach oben
        current_floor = 2
        current_room = "corridor"
        tilemap = get_tilemap(current_floor, current_room)
        player.rect.center = (100, 100)

    elif tilemap[row][col] == 3:  # Treppe nach unten
        current_floor = 1
        current_room = "lobby"
        tilemap = get_tilemap(current_floor, current_room)
        player.rect.center = (100, 100)

    # Kamera folgt Spieler
    camera_x = player.rect.x - WIDTH // 2
    camera_y = player.rect.y - HEIGHT // 2

    screen.fill(WHITE)
    draw_tilemap(screen, camera_x, camera_y, tilemap)



    # Spieler zeichnen (immer mittig)
    screen.blit(player.image,
            (player.rect.centerx - camera_x - player.image.get_width() // 2,
             player.rect.centery - camera_y - player.image.get_height() // 2 -10))
    pygame.draw.rect(screen, (255, 0, 0),
                 (player.rect.x - camera_x,
                  player.rect.y - camera_y,
                  player.rect.width,
                  player.rect.height), 2)

    pygame.display.flip()
    clock.tick(60)
