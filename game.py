import pygame
import sys
from ship import Ship
from island import Island

# NEW: import serial library, install pyserial first
import serial
########################
TILE_SIZE = 64
WINDOW_SIZE = 15 * TILE_SIZE
pygame.init()

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
water = pygame.image.load("assets/water_tile.png")
water_rect = water.get_rect()
screen_rect = screen.get_rect()

# add an island to the center of the screen
island = Island(screen_rect.center)

# add a ship
ship = Ship()  # ship is now an object that *has* a surface
ship2 = Ship()

game_objects = pygame.sprite.Group()
game_objects.add(island, ship, ship2)

num_tiles = screen_rect.width // water_rect.width

# same size as the screen
background = pygame.surface.Surface((screen_rect.width,
                                     screen_rect.height))
# screen is square so same number of tiles in row and col
for y in range(num_tiles):
    for x in range(num_tiles):
        background.blit(water, (x * water_rect.width, y * water_rect.height))

# NEW: add serial connection to PICO that will vary between devices
pico = serial.Serial("COM13")
####################################

coordinate = (0, 0)

clock = pygame.time.Clock()
while True:

    ###############################################
    #  NEW: check serial for new ship coordinate
    pico.write("\n".encode())

    x1, y1, x2, y2 = pico.readline().strip().decode().split(',')
    if (x1, y1) != ('-1', '-1'):
        x_coord = int(int(x1) / 316 * WINDOW_SIZE)
        y_coord = int(int(y1) / 208 * WINDOW_SIZE)
        coordinate = x_coord, y_coord

    if (x2, y2) != ('-2', '-2'):
        x2_coord = int(int(x2) / 316 * WINDOW_SIZE)
        y2_coord = int(int(y2) / 208 * WINDOW_SIZE)
        coordinate2 = x2_coord, y2_coord
    ############################################### 


    # check for user input (key press, mouse clicks,joystick)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("BOOM!")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        if event.type == pygame.QUIT:
            sys.exit()

    # update game objects
    ship.move(coordinate)
    game_objects.update()
    collision = pygame.sprite.collide_rect(ship, island)
    if collision:
        ship.health = ship.health - 1
        # print(f"Collision: ship health={ship.health}!!")

    ship2.move(coordinate2)
    game_objects.update()

    # draw the screen
    screen.blit(background, (0, 0))
    game_objects.draw(screen)
    pygame.display.flip()
    clock.tick(60)
