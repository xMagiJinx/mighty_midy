import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 400))

while True:
    # 1 check for user input (key press, mouse clicks,joystick)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("thanks for playing")
            sys.exit()
        # change the background if a key is
        # pressed or released
        if event.type == pygame.KEYUP:
            screen.fill((0, 0, 255))
        if event.type == pygame.KEYDOWN:
            screen.fill((255, 255, 0))

    pygame.display.flip()
