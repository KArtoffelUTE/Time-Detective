import pygame, sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Time Detective")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Spielerposition in der Welt (nicht Bildschirm!)
player_x, player_y = 400, 300
player_w, player_h = 50, 50
speed = 5

# Eine „Welt“ mit Objekten
world_objects = [
    pygame.Rect(100, 100, 100, 100),
    pygame.Rect(600, 400, 150, 150),
    pygame.Rect(1000, 200, 200, 200)
]

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= speed
    if keys[pygame.K_s]:
        player_y += speed
    if keys[pygame.K_a]:
        player_x -= speed
    if keys[pygame.K_d]:
        player_x += speed

    # Kamera folgt Spieler → Offset berechnen
    camera_x = player_x - WIDTH // 2
    camera_y = player_y - HEIGHT // 2

    # Bildschirm füllen
    screen.fill(WHITE)

    # Weltobjekte zeichnen mit Kamera-Offset
    for obj in world_objects:
        pygame.draw.rect(screen, GREEN,
                         (obj.x - camera_x, obj.y - camera_y, obj.width, obj.height))

    # Spieler zeichnen (immer mittig)
    pygame.draw.rect(screen, BLUE,
                     (WIDTH // 2, HEIGHT // 2, player_w, player_h))

    pygame.display.flip()
    clock.tick(60)
