import pygame
import sys

# Pygame initialisieren
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Time Detective - Rechteck bewegen")

# Farben
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Rechteck (x, y, breite, höhe)
rect_x, rect_y = 100, 100
rect_width, rect_height = 50, 50
speed = 5

# Clock für FPS
clock = pygame.time.Clock()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Tasteneingaben
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        rect_y -= speed
    if keys[pygame.K_s]:
        rect_y += speed
    if keys[pygame.K_a]:
        rect_x -= speed
    if keys[pygame.K_d]:
        rect_x += speed

    # Bildschirm füllen
    screen.fill(WHITE)

    # Rechteck zeichnen
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    # Update
    pygame.display.flip()
    clock.tick(60)  # 60 FPS
