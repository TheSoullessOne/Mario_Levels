from pygame.sprite import Sprite
import pygame


class Character(Sprite):
    def __init__(self, screen, settings):
        super(Character, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('Images/Mario-Movement/mario-look-right.png')
        self.image_left = pygame.image.load('Images/Mario-Movement/mario-look-left.png')
        self.image_walking_right = pygame.image.load('Images/Mario-Movement/mario-walk-right.png')
        self.image_walking_left = pygame.image.load('Images/Mario-Movement/mario-walk-left.png')
        self.width = 32     # Image width
        self.height = 64    # Image height
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect_bottom = self.rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.side_facing = True     # True is right, false is left
        self.starting_jump = 0
        self.rect.centerx = self.settings.screen_width / 2      # Starting Mario at center of screen
        self.rect.bottom = self.settings.screen_height          # Starting Mario at bottom of screen
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.cImage = 0     # Displaying which image in sheet is being displayed
        self.slowDown = 0   # Used to slow down blitting process to smooth animations
        self.default_slow = 300
        self.falling = False    # Check for positive downward y-velocity after jumping

    def blit_me(self, screen):
        if not self.moving_right and not self.moving_left:  # Displaying non-moving sprite
            if self.side_facing:
                screen.blit(self.image, self.rect)
            elif not self.side_facing:
                screen.blit(self.image_left, self.rect)
        elif self.moving_right:
            screen.blit(self.image_walking_right, self.rect, (self.cImage * self.width, 0, self.width, self.height))
        elif self.moving_left:
            screen.blit(self.image_walking_left, self.rect, (self.cImage * self.width, 0, self.width, self.height))

    def slow_blit(self, screen):
        """Slowing down blit process so animations are not too quick"""
        if self.slowDown >= self.default_slow:
            self.slowDown = 0
        else:
            self.slowDown += 1

        if 0 <= self.slowDown < (self.default_slow / 3):
            self.cImage = 0
        elif (self.default_slow / 3) <= self.slowDown < (self.default_slow / 2):
            self.cImage = 1
        elif (self.default_slow / 2) <= self.slowDown < self.default_slow:
            self.cImage = 2
        self.blit_me(screen)

    def update(self):
        if self.moving_left and self.rect.left >= 0:
            self.centerx -= 0.5
            self.side_facing = False
        if self.moving_right and self.rect.right <= self.settings.screen_width:
            self.centerx += 0.5
            self.side_facing = True

        if self.jumping and not self.falling and \
                self.rect.bottom >= self.settings.screen_height - self.settings.max_jump_height:
            self.rect.bottom -= 0.1
        if self.rect.bottom <= self.settings.screen_height - self.settings.max_jump_height:
            self.falling = True
        if self.falling:
            # Later change to collision on ground terrain ^^^
            self.rect.bottom += 1
            if self.rect.bottom >= self.settings.screen_height:
                self.falling = False

        self.rect.centerx = self.centerx

