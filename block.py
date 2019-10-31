import pygame
from pygame.sprite import Sprite
from timer import Timer


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

        anim_frames = ['Images/Blocks/ItemBlock-1.png', 'Images/Blocks/ItemBlock-2.png',
                       'Images/Blocks/ItemBlock-3.png']
        self.animation = Timer(anim_frames, 150)

        self.item = item
        self.activated = False

    def blit_me(self, screen):
        self.image = pygame.image.load(self.animation.image_rect())
        screen.blit(self.image, self.rect)


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


class TreeBlock(Block):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Blocks/tree-block.png')


class LeftTreeTop(Block):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Blocks/tree-top-left.png')


class MidTreeTop(Block):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Blocks/tree-top-mid.png')


class RightTreeTop(Block):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Blocks/tree-top-right.png')


class FloorBlock(Block):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Blocks/FloorBlockNew.png')