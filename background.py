import pygame
from pygame.sprite import Sprite


class Background(Sprite):
    def __init__(self, screen, settings, image):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left = screen.get_rect().left
        self.rect.top = screen.get_rect().top

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.left -= 1
        # Change speed to default movement speed of mario from settings

    def initialize_bg(self):
        self.rect.left = self.screen_rect.left
        self.rect.top = self.screen_rect.top
