import pygame
from pygame.sprite import Sprite
from timer import Timer


class Item(Sprite):
    def __init__(self, screen, settings, x, y):
        super(Item, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('Images/Items/starman-1.png')
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.width
        self.center = self.rect.centerx

        self.rect.x = x
        self.rect.y = y

        self.start_y = 0
        self.moving_up = False
        self.moving_down = False

        self.opened = False
        self.picked_up = False
        self.points = 0
        self.rarity = None  # 0(Very Common) - 2(Rare)

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def is_opened(self):
        self.opened = True
        self.start_y = self.rect.y
        self.moving_up = True

    def update(self):
        if self.moving_up:
            if self.rect.y > self.start_y - 36:
                self.rect.y -= 1
            else:
                self.moving_up = False


class Coin(Item):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        anim_frames = ['Images/Items/coin-1.png', 'Images/Items/coin-2.png', 'Images/Items/coin-3.png']
        self.image = pygame.image.load(anim_frames[0])
        self.animation = Timer(anim_frames, 150)
        self.points = 200
        self.rarity = 0

    def is_opened(self):
        self.opened = True
        self.start_y = self.rect.y
        self.moving_up = True

    def update(self):
        if self.moving_up:
            if self.rect.y > self.start_y - 36 * 3:
                self.rect.y -= 4
            else:
                self.moving_up = False
                self.moving_down = True
        elif self.moving_down:
            if self.rect.y < self.start_y:
                self.rect.y += 4
            else:
                self.moving_down = False

    def blit_me(self):
        self.image = pygame.image.load(self.animation.image_rect())
        self.screen.blit(self.image, self.rect)


class MagicMushroom(Item):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Items/magic-mushroom.png')
        self.points = 1000
        self.rarity = 1


class FireFlower(Item):

    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        anim_frames = ['Images/Items/fire-flower-1.png', 'Images/Items/fire-flower-2.png',
                       'Images/Items/fire-flower-3.png', 'Images/Items/fire-flower-4.png']
        self.image = pygame.image.load(anim_frames[0])
        self.animation = Timer(anim_frames, 150)
        self.points = 1000
        self.rarity = 1

    def blit_me(self):
        self.image = pygame.image.load(self.animation.image_rect())
        self.screen.blit(self.image, self.rect)


class Starman(Item):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        anim_frames = ['Images/Items/starman-1.png', 'Images/Items/starman-3.png',
                       'Images/Items/starman-3.png', 'Images/Items/starman-4.png']
        self.image = pygame.image.load(anim_frames[0])
        self.animation = Timer(anim_frames, 150)
        self.points = 1000
        self.rarity = 2

    def blit_me(self):
        self.image = pygame.image.load(self.animation.image_rect())
        self.screen.blit(self.image, self.rect)


class OneUpMushroom(Item):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load()
        self.points = 0
        self.rarity = 2
