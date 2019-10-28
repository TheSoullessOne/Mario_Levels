import pygame
from pygame.sprite import Sprite


class Background(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        screen_rect = screen.get_rect()

        self.image = pygame.image.load('Images/Backgrounds/1-1-bg.png')
        self.rect = self.image.get_rect()
        self.rect.left = screen.get_rect().left
        self.rect.top = screen.get_rect().top
