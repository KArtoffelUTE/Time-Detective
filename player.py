import pygame
from pathlib import Path

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

        forward_dir = Path(__file__).parent / "assets" / "DetectiveFromTheFutur" / "Forward"
        self.forward_frames = []
        for i in range(1, 7):
            img_path = forward_dir / f"Forward_{i:02}.png"
            image = pygame.image.load(str(img_path)).convert_alpha()
            image = pygame.transform.scale(image, (128, 128))
            self.forward_frames.append(image)
        
        backward_dir = Path(__file__).parent / "assets" / "DetectiveFromTheFutur" / "Backward"
        self.backward_frames = []
        for i in range(1, 7):
            img_path = backward_dir / f"Backward_{i:02}.png"
            image = pygame.image.load(str(img_path)).convert_alpha()
            image = pygame.transform.scale(image, (128, 128))
            self.backward_frames.append(image)       

        self.frame_index = 0
        self.image = self.idle_frames[self.frame_index]

        # Eigene Hitbox definieren (kleiner als Bild)
        self.rect = pygame.Rect(0, 0, 32, 50)
        self.rect.center = (x, y)

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
        forward = False
        backward = False
        dx, dy = 0, 0

        if keys[pygame.K_w]:
            dy = -self.speed
            moved = True
            forward = True
        if keys[pygame.K_s]:
            dy = self.speed
            moved = True
            backward = True
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
                elif forward:
                    self.frame_index = (self.frame_index +1) % len(self.forward_frames)
                    frame = self.forward_frames[self.frame_index]
                elif backward:
                    self.frame_index = (self.frame_index +1) % len(self.backward_frames)
                    frame = self.backward_frames[self.frame_index]
                self.image = frame
                