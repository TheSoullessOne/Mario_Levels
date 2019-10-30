import pygame
from pygame.sprite import Sprite


class Pipe(Sprite):
    def __init__(self, screen, settings):
        super(Pipe, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.center = self.rect.centerx

    def blit_me(self):
        self.screen.blit(self.image, self.rect)