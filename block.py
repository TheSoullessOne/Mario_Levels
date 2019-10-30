import pygame
from pygame.sprite import Sprite


class Block(Sprite):
    def __init__(self, screen, settings, x, y):
        super(Block, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('Images/Blocks/Block.png')
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.width
        self.center = self.rect.centerx
        self.left = self.rect.left
        self.right = self.rect.right
        self.bottom = self.rect.bottom
        self.top = self.rect.top

        self.rect.x = x
        self.rect.y = y

        self.moving_up = False
        self.moving_down = False

    def blit_me(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_up:
            self.center += 1
        elif self.moving_down:
            self.center -= 1

class BlueBlock(Block):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Blocks/Blue-Block.png')

class ItemBlock(Block):
    def __init__(self, item, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Blocks/ItemBlock-1.png')
        self.item = item
        self.activated = False


class BlueItemBlock(Block):
    def __init__(self, item, screen, settings, x, y):
        super().__init__(screen, settings, x ,y)
        self.image = pygame.image.load('Images/Blocks/Blue-ItemBlock-1.png')


class UsedBlock(Block):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Blocks/UsedBlock.png')


class BlueUsedBlock(Block):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Blocks/Blue-UsedBlock.png')


class BrickBlock(Block):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Blocks/BrickBlock.png')


class BlueBrickBlock(Block):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Blocks/Blue-BrickBlock.png')
