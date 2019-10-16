import pygame
from pygame.sprite import Sprite


class Block(Sprite):
    def __init__(self, screen, settings):
        super(Block, self).__init__()
        self.screen = screen
        self.settings = settings
        self.width = 10
        self.height = self.width
        self.moving_up = False
        self.moving_down = False
        self.image = pygame.image.load('Images/Block.png')
        self.rect = self.image.get_rect()
        self.center = self.rect.centerx

    def blit_me(self, screen):
        screen.blit(self.image, self.rect)
        pass

    def update(self):
        if self.moving_up:
            self.center += 1
        elif self.moving_down:
            self.center -= 1


class ItemBlock(Block):
    def __init__(self, item, screen, settings):
        super().__init__(screen, settings)
        self.image = pygame.image.load('Images/ItemBlock.png')
        self.item = item
        self.activated = False


class UsedBlock(Block):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.image = pygame.image.load('Images/UsedBlock.png')


