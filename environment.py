import pygame
from pygame.sprite import Sprite
from timer import Timer


class Environment(Sprite):
    def __init__(self, screen, settings, x, y):
        super(Environment, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('Images/Environment/green-short-pipe.png')
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.center = self.rect.centerx

        self.rect.x = x
        self.rect.y = y

    def blit_me(self):
        self.screen.blit(self.image, self.rect)


class GreenSmallPipe(Environment):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Environment/green-short-pipe.png')


class GreenMedPipe(Environment):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Environment/green-med-pipe.png')


class GreenTallPipe(Environment):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Environment/green-tall-pipe.png')


class GreenShortCornerPipe(Environment):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Environment/green-short-corner-pipe.png')


class GreenTallCornerPipe(Environment):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Environment/green-tall-corner-pipe.png')

# =====================================================================================
class SilverSmallPipe(Environment):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Environment/silver-short-pipe.png')


class SilverMedPipe(Environment):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Environment/silver-med-pipe.png')


class SilverTallPipe(Environment):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Environment/silver-tall-pipe.png')


class SilverShortCornerPipe(Environment):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Environment/silver-short-corner-pipe.png')


class SilverTallCornerPipe(Environment):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Environment/silver-tall-corner-pipe.png')


class FlagPole(Environment):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        drop_frames = ['Images/Environment/flag-pole-1.png', 'Images/Environment/flag-pole-2.png',
                       'Images/Environment/flag-pole-3.png', 'Images/Environment/flag-pole-4.png',
                       'Images/Environment/flag-pole-5.png']
        self.image = pygame.image.load(drop_frames[0])
        self.drop_animation = Timer(drop_frames, 150)
        self.activated = False

    def blit_me(self):
        if self.activated:
            self.image = pygame.image.load(self.drop_animation.image_rect())
        self.screen.blit(self.image, self.rect)