import pygame
import time
import sys
pygame.init()

screen = pygame.display.set_mode((400, 400))

while True:
    # 1 check for user input (key press, mouse clicks,joystick)
    print("---- Checking for Events! ----")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("thanks for playing")
            sys.exit()
        # want to find out user released a key
        if event.type == pygame.KEYUP:
            screen.fill((0, 0, 255))
        if event.type == pygame.MOUSEMOTION:
            screen.fill((255, 255, 0))

    print("---- DONE Checking ----")

    pygame.display.flip()
    time.sleep(1)
