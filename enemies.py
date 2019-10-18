import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, screen, settings):
        super(Enemy, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.center = self.rect.centerx

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        pass


