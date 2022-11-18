import pygame
from pygame.sprite import Sprite


class Island(Sprite):

    def __init__(self, position):
        super().__init__()
        self.image = pygame.surface.Surface((128, 128))
        self.image.blit(pygame.image.load("assets/water_tile.png"),
                        (0, 0))
        self.image.blit(pygame.image.load("assets/island_tl.png"),
                        (0, 0))

        self.image.blit(pygame.image.load("assets/water_tile.png"),
                        (64, 0))
        self.image.blit(pygame.image.load("assets/island_tr.png"),
                        (64, 0))

        self.image.blit(pygame.image.load("assets/water_tile.png"),
                        (0, 64))
        self.image.blit(pygame.image.load("assets/island_bl.png"),
                        (0, 64))

        self.image.blit(pygame.image.load("assets/water_tile.png"),
                        (64, 64))
        self.image.blit(pygame.image.load("assets/island_br.png"),
                        (64, 64))
        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw(self, surface):
        surface.blit(self.image, self.rect)
