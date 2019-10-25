import pygame
from pygame.sprite import Sprite


class Item(Sprite):
    def __init__(self, screen, settings):
        super(Item, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.width
        self.center = self.rect.centerx

        self.moving_up = False
        self.moving_down = False

        self.points = 0
        self.rarity = None # 0(Very Common) - 2(Rare)

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_up:
            self.center += 1
        elif self.moving_down:
            self.center -= 1


class Coin(Item):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.image = pygame.image.load('Images/Items/coin-1.png')
        self.points = 200
        self.rarity = 0


class MagicMushroom(Item):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.image = pygame.image.load('Images/Items/magic-mushroom.png')
        self.points = 1000
        self.rarity = 1


class FireFlower(Item):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.image = pygame.image.load('Images/Items/fire-flower.png')
        self.points = 1000
        self.rarity = 1


class Starman(Item):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.image = pygame.image.load('Images/Items/starman-1.png')
        self.points = 1000
        self.rarity = 2


class OneUpMushroom(Item):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.image = pygame.image.load()
        self.points = 0
        self.rarity = 2