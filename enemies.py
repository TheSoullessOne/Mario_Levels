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

        # Turns on their motion if they are in viewfinder
        self.on_screen = False

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update(self): pass
    def hit(self): pass
    def set_image(self): pass


class KoopaParatroopa(Enemy):
    def __init__(self, screen, settings, color):
        super().__init__(screen, settings)
        self.color = color
        self.image = self.set_image()

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up:
            self.centerx += 1
        elif self.moving_down:
            self.centerx += 1
        if self.moving_left:
            self.centery -= 1
        elif self.moving_right:
            self.centery += 1

    def set_image(self):
        if self.color == 'red':
            return pygame.image.load('Images/Enemies/KoopaParatroopa/red-left-1.png')
        elif self.color == 'green':
            return pygame.image.load('Images/Enemies/KoopaParatroopa/green-left-1.png')


class KoopaTroopa(Enemy):
    def __init__(self, screen, settings, color):
        super().__init__(screen, settings)
        self.color = color
        self.image = self.set_image()

        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_left:
            self.centery -= 1
        elif self.moving_right:
            self.centery += 1

    def set_image(self):
        if self.color == 'red':
            return pygame.image.load('Images/Enemies/KoopaTroopa/red-left-1.png')
        # elif self.color == 'green':
        #     return pygame.image.load('Images/Enemies/KoopaParatroopa/green-left-1.png')

    def stomped(self):
        self.image = pygame.image.load()


class LittleGoomba(Enemy):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.image = pygame.image.load('Images/Enemies/LittleGoomba/goomba-1.png')

        self.moving_left = False
        self.moving_right = False

    def update(self): pass
    def stomped(self): pass


class PiranhaPlant(Enemy):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.image = pygame.image.load('Images/Enemies/PiranhaPlant/green-1.png')

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
        self.color = color
        self.image = self.set_image()

    def update(self): pass

    def set_image(self):
        if self.color == 'red':
            return pygame.image.load('Images/Enemies/CheepCheep/red-left-1.png')
        elif self.color == 'green':
            return pygame.image.load('Images/Enemies/CheepCheep/green-left-1.png')
        elif self.color == 'gray':
            return pygame.image.load('Images/Enemies/CheepCheep/gray-left-1.png')


class FireBar(Enemy):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.image = None

    def update(self): pass


class Bloober(Enemy):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.image = pygame.image.load('Images/Enemies/Bloober/bloober-1.png')

    def update(self): pass
    # tracks mario's x movements but continues swimming animation
