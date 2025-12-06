import pygame, sys
from pathlib import Path

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Time Detective")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Idle-Frames laden
        idle_dir = Path(__file__).parent / "assets" / "DetectiveFromTheFutur" / "Idle"
        self.idle_frames = []
        for i in range(1, 9):  # Idle_01 bis Idle_08
            img_path = idle_dir / f"Idle_{i:02}.png"
            image = pygame.image.load(str(img_path)).convert_alpha()
            image = pygame.transform.scale(image, (128, 128))
            self.idle_frames.append(image)
            
        # Run-Frames laden
        run_dir = Path(__file__).parent / "assets" / "DetectiveFromTheFutur" / "Run"
        self.run_frames = []
        for i in range(1, 9):
            img_path = run_dir / f"Run_{i:02}.png"
            image = pygame.image.load(str(img_path)).convert_alpha()
            image = pygame.transform.scale(image, (128, 128))
            self.run_frames.append(image)

        self.frame_index = 0
        self.image = self.idle_frames[self.frame_index]

        # Eigene Hitbox definieren (kleiner als Bild)
        self.rect = pygame.Rect(0, 0, 32, 50)
        self.rect.center = (x, y+100)

        self.speed = 5

        # Timer für Animation
        self.animation_timer = 0
        self.animation_speed = 150  # Millisekunden pro Frame

    def check_collision(self, new_rect, obstacles):
        for obj in obstacles:
            if new_rect.colliderect(obj):
                return True
        return False

    def update(self, keys, obstacles):
        moved = False
        left = False  # Flag für Linksbewegung
        dx, dy = 0, 0

        if keys[pygame.K_w]:
            dy = -self.speed
            moved = True
        if keys[pygame.K_s]:
            dy = self.speed
            moved = True
        if keys[pygame.K_a]:
            dx = -self.speed
            moved = True
            left = True
        if keys[pygame.K_d]:
            dx = self.speed
            moved = True
        
        new_rect = self.rect.move(dx, dy)
        if not self.check_collision(new_rect, obstacles):
            self.rect = new_rect

        if not moved:
        # Idle-Animation
            self.animation_speed = 150
            now = pygame.time.get_ticks()
            if now - self.animation_timer > self.animation_speed:
                self.animation_timer = now
                self.frame_index = (self.frame_index + 1) % len(self.idle_frames)
                self.image = self.idle_frames[self.frame_index]
        else:
            # Run-Animation
            self.animation_speed = 50
            now = pygame.time.get_ticks()
            if now - self.animation_timer > self.animation_speed:
                self.animation_timer = now
                self.frame_index = (self.frame_index + 1) % len(self.run_frames)
                frame = self.run_frames[self.frame_index]
                if left:
                    frame = pygame.transform.flip(frame, True, False)
                self.image = frame

world_objects = [
    pygame.Rect(100, 100, 100, 100),
    pygame.Rect(600, 400, 150, 150),
    pygame.Rect(1000, 200, 200, 200)
]

player = Player(400, 300)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player.update(keys, world_objects)

    # Kamera folgt Spieler
    camera_x = player.rect.x - WIDTH // 2
    camera_y = player.rect.y - HEIGHT // 2

    screen.fill(WHITE)

    for obj in world_objects:
        pygame.draw.rect(screen, GREEN,
                         (obj.x - camera_x, obj.y - camera_y, obj.width, obj.height))

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
