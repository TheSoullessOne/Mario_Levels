from pygame.sprite import Sprite
import pygame


class Character(Sprite):
    def __init__(self, screen, settings):
        super(Character, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('Images/Basic_Sprite.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.starting_jump = 0
        self.rect.centerx = self.settings.screen_width / 2
        self.rect.bottom = self.settings.screen_height
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery

    def blit_me(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_left and self.rect.left >= 0:
            self.centerx -= 0.5
        if self.moving_right and self.rect.right <= self.settings.screen_width:
            self.centerx += 0.5
        if self.jumping and self.can_jump():
            self.centery -= 1

        self.rect.centerx = self.centerx

    def can_jump(self):
        return self.rect.bottom > (self.starting_jump - self.settings.max_jump_height)
