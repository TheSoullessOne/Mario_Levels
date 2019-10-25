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
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update(self): pass
    def hit(self): pass


class KoopaParatroopa(Enemy):
    def __init__(self, screen, settings, color):
        super().__init__(screen, settings)
        self.image = pygame.image.load()
        self.color = color

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up:
            self.centerx += 1
        elif self.moving_down:
            self.centerx += 1
        elif self.moving_left:
            self.centery -= 1
        elif self.moving_right:
            self.centery += 1


class KoopaTroopa(Enemy):
    def __init__(self, screen, settings, color):
        super().__init__(screen, settings)
        self.image = pygame.image.load()
        self.color = color

        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_left:
            self.centery -= 1
        elif self.moving_right:
            self.centery += 1

    def stomped(self):
        self.image = pygame.image.load()


class LittleGoomba(Enemy):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.image = pygame.image.load()

        self.moving_left = False
        self.moving_right = False

    def update(self): pass
    def stomped(self): pass


class PiranhaPlant(Enemy):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.image = pygame.image.load()

        self.near_mario = True
        self.moving_up = False
        self.moving_down = False

    def update(self): pass


class Podoboo(Enemy):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.image = pygame.image.load()

        # Add movements

    def update(self): pass


class CheepCheep(Enemy):
    def __init__(self, screen, settings, color):
        super().__init__(screen, settings)
        self.image = pygame.image.load()
        self.color = color

    def update(self): pass

# Fire-Bar
# Bloober
