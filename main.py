import pygame, sys
from player import Player
from rooms import rooms
from tilemaps import TILE_SIZE, load_tiles

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Time Detective")

WHITE = (255, 255, 255)

# Start in der Lobby
current_room = rooms["lobby"]
spawn_x, spawn_y = current_room.spawns["from_restaurant"]
player = Player(spawn_x, spawn_y)

load_tiles()

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
    player.update(keys, current_room.obstacles)

    # Tür-Check
    row = player.rect.centery // TILE_SIZE
    col = player.rect.centerx // TILE_SIZE
    door = current_room.check_for_door(row, col)

    # Treppen-Check
    stair = current_room.check_for_stair(row, col)
    if stair:
        current_room = rooms[stair.target_room]
        spawn_x, spawn_y = current_room.spawns[stair.target_spawn]
        player.rect.center = (spawn_x, spawn_y)    

    if door:
        current_room = rooms[door.target_room]
        spawn_x, spawn_y = current_room.spawns[door.target_spawn]
        player.rect.center = (spawn_x, spawn_y)

    # Kamera
    camera_x = player.rect.x - WIDTH // 2
    camera_y = player.rect.y - HEIGHT // 2

    screen.fill(WHITE)
    current_room.draw(screen, camera_x, camera_y)

    # Spieler zeichnen
    screen.blit(
        player.image,
        (player.rect.centerx - camera_x - player.image.get_width() // 2,
         player.rect.centery - camera_y - player.image.get_height() // 2 - 10)
    )

    pygame.display.flip()
    clock.tick(60)
