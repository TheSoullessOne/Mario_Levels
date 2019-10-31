from pygame.sprite import Sprite
import pygame
from game_functions import update_all
vec = pygame.math.Vector2


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
        self.sprite_delay = 0

        # Physics variables
        self.pos = (80, 400)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.moving_right = False
        self.moving_left = False

        self.side_facing = True     # True is right, false is left
        self.on_block = False

        self.changing_to_big = False
        self.changing_to_smol = False

        self.y_bot = float(self.rect.bottom)
        self.start_jmp = self.y_bot
        self.start_jmp_bool = False

        self.cImage = 0     # Displaying which image in sheet is being displayed
        self.slowDown = 0   # Used to slow down blitting process to smooth animations
        self.default_slow = 50
        self.falling = False   # Check for positive downward y-velocity after jumping

        self.cannot_move_left = False
        self.cannot_move_right = False

    def change_mario_size(self):
        if self.mario_size == 0 and not self.changing_to_smol:
            self.image = pygame.image.load('Images/Mario-Movement/smol/smol-mario-look-right.png')
            self.image_left = pygame.image.load('Images/Mario-Movement/smol/smol-mario-look-left.png')
            self.image_walking_right = pygame.image.load('Images/Mario-Movement/smol/smol-mario-walk-right.png')
            self.image_walking_left = pygame.image.load('Images/Mario-Movement/smol/smol-mario-walk-left.png')
            self.image_jump_right = pygame.image.load('Images/Mario-Movement/smol/smol-mario-jump-right.png')
            self.image_jump_left = pygame.image.load('Images/Mario-Movement/smol/smol-mario-jump-left.png')
            self.update_rect()
        elif self.mario_size == 1 and not self.changing_to_big:
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

    def smol_to_big(self):
        if self.side_facing:
            self.image = pygame.image.load('Images/Mario-Movement/smol/smol-tolarge-right.png')
        else:
            self.image = pygame.image.load('Images/Mario-Movement/smol/smol-tolarge-left.png')
        self.sprite_delay += 1
        self.update_rect()
        if self.sprite_delay >= 4:
            self.changing_to_big = False
            self.sprite_delay = 0
            self.change_mario_size()
        self.blit_me(self.screen)
        self.update_rect()

    def big_to_smol(self):
        if self.side_facing:
            self.image = pygame.image.load('Images/Mario-Movement/smol/smol-tolarge-right.png')
        else:
            self.image = pygame.image.load('Images/Mario-Movement/smol/smol-tolarge-left.png')
        self.sprite_delay += 1
        if self.sprite_delay >= 4:
            self.changing_to_smol = False
            self.sprite_delay = 0
            self.change_mario_size()
        self.blit_me(self.screen)
        self.update_rect()

    def update_rect(self):
        """Updating rect after change in mario size"""
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.centerx = self.pos.x
        self.centery = self.pos.y

    def blit_me(self, screen):
        if not self.on_block:
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

    def mario_jumping(self):
        if self.on_block:
            self.vel.y = -15
            self.pos.y -= 1
            self.rect.midbottom = self.pos

    def mario_walking(self, screen, current_level):
        self.acc = vec(0, self.settings.PLAYER_GRAVITY)

        keys = pygame.key.get_pressed()

        if self.rect.left >= 0 and not self.cannot_move_left:
            if keys[pygame.K_LEFT]:
                self.acc.x = -self.settings.MOVE_SPEED
                self.side_facing = False
                self.moving_left = True
            else:
                self.moving_left = False
        if self.rect.right <= self.settings.screen_width and not self.cannot_move_right:
            if self.rect.right >= self.settings.screen_width / 2:
                update_all(screen, current_level, self.settings)
            else:
                if keys[pygame.K_RIGHT]:
                    self.acc.x = self.settings.MOVE_SPEED
                    self.side_facing = True
                    self.moving_right = True
                else:
                    self.moving_right = False

        self.acc.x += self.vel.x * self.settings.PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.centerx = self.pos.x
        self.centery = self.pos.y

    def check_on_block(self, mario, platforms):
        hits = pygame.sprite.spritecollide(mario, platforms, False)

        if hits:
            self.pos.y = hits[0].rect.top + 1
            self.on_block = True
            self.vel.y = 0
        else:
            self.on_block = False

        self.rect.midbottom = self.pos

    def update(self, screen, current_level, mario, platforms):
        self.check_on_block(mario, platforms)
        self.mario_walking(screen, current_level)
        if self.changing_to_big:
            self.smol_to_big()
        elif self.changing_to_smol:
            self.big_to_smol()
        #platforms.update()

        self.cannot_move_right = self.cannot_move_left = False


class Platform(pygame.sprite.Sprite):
    RED = (255, 0, 0)

    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(Platform.RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
