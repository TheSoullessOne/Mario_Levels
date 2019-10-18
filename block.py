import pygame
from pygame.sprite import Sprite


class Block(Sprite):
    def __init__(self, screen, settings):
        super(Block, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('Images/Blocks/Block.png')
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.width
        self.center = self.rect.centerx

        self.moving_up = False
        self.moving_down = False

    def blit_me(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_up:
            self.center += 1
        elif self.moving_down:
            self.center -= 1


class ItemBlock(Block):
    def __init__(self, item, screen, settings):
        super().__init__(screen, settings)
        self.image = pygame.image.load('Images/Blocks/ItemBlock.png')
        self.item = item
        self.activated = False


class UsedBlock(Block):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.image = pygame.image.load('Images/Blocks/UsedBlock.png')


