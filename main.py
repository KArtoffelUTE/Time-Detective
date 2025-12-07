import pygame, sys
from player import Player
from tilemaps import get_tilemap, draw_tilemap, get_obstacles, TILE_SIZE, room_spawns, door_links

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Time Detective")

WHITE = (255, 255, 255)

current_floor = 1
current_room = "lobby"
tilemap = get_tilemap(current_floor, current_room)

# Start direkt vor der Lobby-Tür ins Restaurant
spawn_x, spawn_y = room_spawns[(current_room, current_floor, "to_restaurant")]
player = Player(spawn_x, spawn_y - TILE_SIZE *2)

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

    row = player.rect.centery // TILE_SIZE
    col = player.rect.centerx // TILE_SIZE

    # Tür-Check
    if tilemap[row][col] == 4:
        # Bestimme Zielraum anhand aktueller Raum-Logik
        if current_room == "lobby":
            next_room, spawn_key = door_links[(current_room, current_floor)]
        elif current_room == "restaurant":
            # Unterscheide, welche Tür benutzt wurde
            if col == 6:  # Tür links
                next_room, spawn_key = door_links[(current_room, current_floor, "to_lobby")]
            elif col == 18:  # Tür rechts
                next_room, spawn_key = door_links[(current_room, current_floor, "to_kitchen")]
        elif current_room == "kitchen":
            next_room, spawn_key = door_links[(current_room, current_floor)]

        current_room = next_room
        tilemap = get_tilemap(current_floor, current_room)
        spawn_x, spawn_y = room_spawns[(current_room, current_floor, spawn_key)]
        player.rect.center = (spawn_x, spawn_y - TILE_SIZE *2)

    # Kamera folgt Spieler
    camera_x = player.rect.x - WIDTH // 2
    camera_y = player.rect.y - HEIGHT // 2

    screen.fill(WHITE)
    draw_tilemap(screen, camera_x, camera_y, tilemap)

    # Spieler zeichnen
    screen.blit(player.image,
        (player.rect.centerx - camera_x - player.image.get_width() // 2,
         player.rect.centery - camera_y - player.image.get_height() // 2 - 10))
    pygame.draw.rect(screen, (255, 0, 0),
        (player.rect.x - camera_x,
         player.rect.y - camera_y,
         player.rect.width,
         player.rect.height), 2)

    pygame.display.flip()
    clock.tick(60)
