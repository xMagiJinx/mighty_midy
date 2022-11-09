import pygame
import sys
from ship import Ship
from island import Island

TILE_SIZE = 64
WINDOW_SIZE = 15 * TILE_SIZE
pygame.init()

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
water = pygame.image.load("assets/water_tile.png")
water_rect = water.get_rect()
screen_rect = screen.get_rect()

# add an island
island = Island()
island.move((450, 450))
# add a ship
ship = Ship()  # ship is now an object that *has* a surface

num_tiles = screen_rect.width // water_rect.width


def draw_background():
    # screen is square so same number of tiles in row and col
    for y in range(num_tiles):
        for x in range(num_tiles):
            screen.blit(water, (x * water_rect.width, y * water_rect.height))


coordinate = (0, 0)

clock = pygame.time.Clock()
while True:

    # 1 check for user input (key press, mouse clicks,joystick)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            coordinate = pygame.mouse.get_pos()
            # draw a ship at the x,y coordinate of the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("BOOM!")
        if event.type == pygame.QUIT:
            sys.exit()

    # update game objects
    ship.move(coordinate)
    collision = pygame.sprite.collide_rect(ship, island)
    if collision:
        ship.health = ship.health - 1
        print(f"Collision: ship health={ship.health}!!")

    # draw the screen
    draw_background()
    island.draw(screen)
    ship.draw(screen)
    pygame.display.flip()
    clock.tick(60)
