import pygame, sys
from player import Player
from tilemaps import get_tilemap,draw_tilemap, get_obstacles, TILE_SIZE, room_spawns

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Time Detective")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
player = Player(500, 500)
current_floor = 1
current_room = "lobby"
tilemap = get_tilemap(current_floor, current_room)
spawn_x, spawn_y = room_spawns[(current_room, current_floor)]
player.rect.center = (spawn_x, spawn_y)




clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    print("Player Position:", player.rect.center)
    keys = pygame.key.get_pressed()
    obstacles = get_obstacles(tilemap)
    player.update(keys, obstacles)
    # Treppen-Check
    row = player.rect.centery // TILE_SIZE
    col = player.rect.centerx // TILE_SIZE

    if tilemap[row][col] == 2:  # Treppe hoch
        print("Hier würde es nach oben gehen – Etage fehlt noch!")
    elif tilemap[row][col] == 3:  # Treppe runter
        print("Hier würde es nach unten gehen – Etage fehlt noch!")
    
    row = player.rect.centery // TILE_SIZE
    col = player.rect.centerx // TILE_SIZE

    if tilemap[row][col] == 4:  # Tür
        if current_room == "lobby":
            current_room = "restaurant"
        elif current_room == "restaurant":
            current_room = "kitchen"
        elif current_room == "kitchen":
            current_room = "restaurant"
        
        tilemap = get_tilemap(current_floor, current_room)

        # Spawn direkt auf der neuen Türposition
        room_x, room_y = room_spawns[(current_room, current_floor)]
        player.rect.center = (room_x, room_y)

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
