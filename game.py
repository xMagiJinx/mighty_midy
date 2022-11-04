import pygame
import sys

TILE_SIZE = 64
pygame.init()

screen = pygame.display.set_mode(
    (15*TILE_SIZE, 15*TILE_SIZE))
print(screen.get_rect())
water = pygame.image.load("assets/water_tile.png")
water_rect = water.get_rect()
screen_rect = screen.get_rect()

num_tiles = screen_rect.width // water_rect.width
print(f"We need {num_tiles} water tiles")

for y in range(num_tiles):
    for x in range(num_tiles):
        screen.blit(water, (x*water_rect.width,y*water_rect.height))

while True:
    # 1 check for user input (key press, mouse clicks,joystick)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    pygame.display.flip()
