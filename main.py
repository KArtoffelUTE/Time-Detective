import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Time Detective")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit()

