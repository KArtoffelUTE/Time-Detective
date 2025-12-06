import pygame, sys
from pathlib import Path

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Time Detective")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Spielerklasse mit Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # relativer Pfad zum Bild
        image_path = Path(__file__).parent / "assets" / "DetectiveFromTheFutur" / "Idle" / "Idle_01.png"
        image = pygame.image.load(str(image_path)).convert_alpha()
        # Bild skalieren (z. B. auf 64x64 Pixel)
        self.image = pygame.transform.scale(image, (128, 128))
        # Rechteck für Position
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

# Spieler erstellen
player = Player(400, 300)

# Weltobjekte
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
    player.update(keys)

    # Kamera folgt Spieler → Offset berechnen
    camera_x = player.rect.x - WIDTH // 2
    camera_y = player.rect.y - HEIGHT // 2

    # Bildschirm füllen
    screen.fill(WHITE)

    # Weltobjekte zeichnen mit Kamera-Offset
    for obj in world_objects:
        pygame.draw.rect(screen, GREEN,
                         (obj.x - camera_x, obj.y - camera_y, obj.width, obj.height))

    # Spieler zeichnen (immer mittig auf dem Bildschirm)
    screen.blit(player.image, (WIDTH // 2 - player.image.get_width()//2,
                               HEIGHT // 2 - player.image.get_height()//2))

    pygame.display.flip()
    clock.tick(60)
