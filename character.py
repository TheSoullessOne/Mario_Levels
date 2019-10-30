from pygame.sprite import Sprite
import pygame
from game_functions import update_all


class Character(Sprite):
    def __init__(self, screen, settings):
        super(Character, self).__init__()
        self.screen = screen
        self.settings = settings

        self.mario_size = 0     # 0 = smol mario, 1 = normal mario, 2 = fire boi
        self.image = pygame.image.load('Images/Mario-Movement/smol/smol-mario-look-right.png')
        self.image_left = pygame.image.load('Images/Mario-Movement/smol/smol-mario-look-left.png')
        self.image_walking_right = pygame.image.load('Images/Mario-Movement/smol/smol-mario-walk-right.png')
        self.image_walking_left = pygame.image.load('Images/Mario-Movement/smol/smol-mario-walk-left.png')
        self.image_jump_right = pygame.image.load('Images/Mario-Movement/smol/smol-mario-jump-right.png')
        self.image_jump_left = pygame.image.load('Images/Mario-Movement/smol/smol-mario-jump-left.png')
        self.width = 32     # Image width
        self.height = 32    # Image height
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect_bottom = self.rect.bottom

        self.small_to_large_right = pygame.image.load('Images/Mario-Movement/smol/smol-tolarge-right.png')
        self.small_to_large_left = pygame.image.load('Images/Mario-Movement/smol/smol-tolarge-left.png')

        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.side_facing = True     # True is right, false is left
        self.on_block = False
        self.has_collided = False
        self.starting_jump = 0
        self.rect.centerx = self.settings.screen_width / 2      # Starting Mario at center of screen
        self.rect.bottom = self.settings.screen_height          # Starting Mario at bottom of screen
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.y_bot = float(self.rect.bottom)

        self.cImage = 0     # Displaying which image in sheet is being displayed
        self.slowDown = 0   # Used to slow down blitting process to smooth animations
        self.default_slow = 30
        self.falling = True   # Check for positive downward y-velocity after jumping
        self.init_jmp = self.settings.jmp_speed
        self.cannot_move_left = False
        self.cannot_move_right = False

    def change_mario_size(self, next_size):
        if next_size == 0 and self.mario_size > 0:
            if self.side_facing:
                self.screen.blit(self.small_to_large_right, self.rect)
            elif not self.side_facing:
                self.screen.blit(self.small_to_large_left, self.rect)

            self.image = pygame.image.load('Images/Mario-Movement/smol/smol-mario-look-right.png')
            self.image_left = pygame.image.load('Images/Mario-Movement/smol/smol-mario-look-left.png')
            self.image_walking_right = pygame.image.load('Images/Mario-Movement/smol/smol-mario-walk-right.png')
            self.image_walking_left = pygame.image.load('Images/Mario-Movement/smol/smol-mario-walk-left.png')
            self.image_jump_right = pygame.image.load('Images/Mario-Movement/smol/smol-mario-jump-right.png')
            self.image_jump_left = pygame.image.load('Images/Mario-Movement/smol/smol-mario-jump-left.png')
            self.update_rect()
        elif self.mario_size == 1:
            self.image = pygame.image.load('Images/Mario-Movement/normal/mario-look-right.png')
            self.image_left = pygame.image.load('Images/Mario-Movement/normal/mario-look-left.png')
            self.image_walking_right = pygame.image.load('Images/Mario-Movement/normal/mario-walk-right.png')
            self.image_walking_left = pygame.image.load('Images/Mario-Movement/normal/mario-walk-left.png')
            self.image_jump_right = pygame.image.load('Images/Mario-Movement/normal/mario-jump-right.png')
            self.image_jump_left = pygame.image.load('Images/Mario-Movement/normal/mario-jump-left.png')
            self.height = 64
            self.update_rect()
        elif self.mario_size == 2:
            self.image = pygame.image.load('Images/Mario-Movement/spicy/fire-mario-look-right.png')
            self.image_left = pygame.image.load('Images/Mario-Movement/spicy/fire-mario-look-left.png')
            self.image_walking_right = pygame.image.load('Images/Mario-Movement/spicy/fire-mario-walk-right.png')
            self.image_walking_left = pygame.image.load('Images/Mario-Movement/spicy/fire-mario-walk-left.png')
            self.image_jump_right = pygame.image.load('Images/Mario-Movement/spicy/fire-mario-jump-right.png')
            self.image_jump_left = pygame.image.load('Images/Mario-Movement/spicy/fire-mario-jump-left.png')
            self.height = 64
            self.update_rect()

    def update_rect(self):
        """Updating rect after change in mario size"""
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect_bottom = self.rect.bottom

    def blit_me(self, screen):
        if self.jumping or self.falling:
            self.on_block = False
            if self.side_facing:
                screen.blit(self.image_jump_right, self.rect)
            elif not self.side_facing:
                screen.blit(self.image_jump_left, self.rect)
        elif self.side_facing and not self.moving_right and not self.moving_left:
            screen.blit(self.image, self.rect)
        elif not self.side_facing and not self.moving_right and not self.moving_left:
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

    def update(self, screen, blocks, mobs, background):
        if self.moving_left and self.rect.left >= 0 and not self.cannot_move_left:
            self.centerx -= 2.0
            self.side_facing = False
        if self.moving_right and self.rect.right <= self.settings.screen_width and not self.cannot_move_right:
            if self.rect.right >= self.settings.screen_width / 2:
                update_all(screen, blocks, mobs, background)
                # background.rect.left -= 2.0
            else:
                self.centerx += 2.0
            self.side_facing = True
        if self.jumping and not self.falling and \
                self.y_bot >= self.settings.screen_height - self.settings.max_jump_height:
            self.on_block = False
            self.init_jmp -= float(0.0016)
            self.y_bot -= float(self.init_jmp)
        if self.y_bot <= self.settings.screen_height - self.settings.max_jump_height:
            self.falling = True
        if self.falling:  # and self.rect.bottom <= self.settings.screen_height:
            # Later change to collision on ground terrain ^^^
            if self.y_bot >= self.settings.screen_height:
                self.falling = False
                self.init_jmp = self.settings.jmp_speed
            else:
                self.init_jmp += float(0.0016)
                self.y_bot += self.init_jmp

        self.rect.centerx = self.centerx
        self.rect.bottom = self.y_bot
        self.cannot_move_right = self.cannot_move_left = False


