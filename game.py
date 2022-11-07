import pygame
import sys

TILE_SIZE = 64
WINDOW_SIZE = 15 * TILE_SIZE
pygame.init()

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
water = pygame.image.load("assets/water_tile.png")
water_rect = water.get_rect()
screen_rect = screen.get_rect()

# add an island
island_tr = pygame.image.load("assets/island_tr.png")
island_tl = pygame.image.load("assets/island_tl.png")
island_br = pygame.image.load("assets/island_br.png")
island_bl = pygame.image.load("assets/island_bl.png")
# add a ship
ship = pygame.image.load("assets/ship.png")

num_tiles = screen_rect.width // water_rect.width


def draw_background():
    # screen is square so same number of tiles in row and col
    for y in range(num_tiles):
        for x in range(num_tiles):
            screen.blit(water, (x * water_rect.width, y * water_rect.height))

    screen.blit(island_tl, (450, 450))
    screen.blit(island_tr, (450 + 64, 450))
    screen.blit(island_bl, (450, 450 + 64))
    screen.blit(island_br, (450 + 64, 450 + 64))


coordinate = (0, 0)

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

    # draw the screen
    draw_background()
    ship_rect = ship.get_rect()
    ship_rect.center = coordinate
    screen.blit(ship, ship_rect)
    pygame.display.flip()
