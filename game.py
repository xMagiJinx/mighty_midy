import pygame
import sys

TILE_SIZE = 64
WINDOW_SIZE = 15 * TILE_SIZE
pygame.init()

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
water = pygame.image.load("assets/water_tile.png")
water_rect = water.get_rect()
screen_rect = screen.get_rect()

num_tiles = screen_rect.width // water_rect.width

# screen is square so same number of tiles in row and col
for y in range(num_tiles):
    for x in range(num_tiles):
        screen.blit(water, (x * water_rect.width, y * water_rect.height))

while True:
    # 1 check for user input (key press, mouse clicks,joystick)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
