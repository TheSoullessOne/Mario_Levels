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

        self.mario_dead = False
        self.mario_dead_cont = False
        self.dead_bool = True
        self.dead_counter = 0
        self.cant_move = False

        # Physics variables
        self.pos = (80, 400)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.moving_right = False
        self.moving_left = False

        self.side_facing = True     # True is right, false is left
        self.on_block = False
        self.on_pipe = False
        self.can_jump = True
# <<<<<<< HEAD
        self.starting_jump = 0
        self.rect.centerx = self.settings.screen_width / 2      # Starting Mario at center of screen
        self.rect.bottom = self.settings.screen_height - 100          # Starting Mario at bottom of screen
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
# =======

        self.changing_to_big = False
        self.changing_to_smol = False

# >>>>>>> cb2335c878c9a1e6874e2031c412ce6d25c73f5a
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
        if self.mario_size == 2:
            print('ran')
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
        temp_x = self.rect.x
        temp_y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = temp_x
        self.rect.y = temp_y
        self.centerx = self.pos.x
        self.centery = self.pos.y

    def blit_me(self, screen):
        if not self.mario_dead:
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
        else:
            screen.blit(self.image, self.rect)

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
        if self.on_block and self.can_jump:
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
            if self.rect.right > self.settings.screen_width / 2 and keys[pygame.K_RIGHT]:
                update_all(screen, current_level, self.settings)
            else:
                if keys[pygame.K_RIGHT]:
                    self.acc.x = self.settings.MOVE_SPEED
                    self.side_facing = True
                    self.moving_right = True
                else:
                    self.moving_right = False
        self.place_mario()

    def place_mario(self):
        """Puts mario where he should be after he moves"""
        self.acc.x += self.vel.x * self.settings.PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.centerx = self.pos.x
        self.centery = self.pos.y

    def check_on_block(self, mario, platforms):
        hits = pygame.sprite.spritecollide(mario, platforms, False)

        if hits and not self.mario_dead and self.rect.top <= hits[0].rect.bottom and self.rect.bottom >= hits[0].rect.centery and \
                (self.rect.right >= hits[0].rect.left or self.rect.left <= hits[0].rect.right):

            self.pos.y = hits[0].rect.bottom + self.height + 1
            self.vel.y = 0
            self.acc.y = 0

            hits[0].hit_block()
        # elif block_hit and not self.mario_dead and self.rect.right >= hits[0].rect.left and not self.on_block:
        #     print('hit left')
        #     self.rect.right = hits[0].rect.left - 1
        #     self.vel.y = 0
        #     self.acc.y = 0
        elif hits and not self.mario_dead:
            self.pos.y = hits[0].rect.top + 1
            self.on_block = True
            self.vel.y = 0
            self.can_jump = True
        else:
            self.on_block = False
        self.rect.midbottom = self.pos

    def check_with_pipes(self, mario, pipes):
        hits = pygame.sprite.spritecollide(mario, pipes, False)

        for pipe in pipes:
            if self.rect.colliderect(pipe.rect):
                if pipe.rect.left - self.rect.right > 0:
                    self.rect.right = pipe.rect.left
                    self.cannot_move_right = True
                elif pipe.rect.right - self.rect.left < 0:
                    self.rect.left = pipe.rect.right
                    self.cannot_move_left = True

        if hits and not self.on_pipe and not self.mario_dead and mario.rect.left >= hits[0].rect.right and \
                mario.rect.bottom > hits[0].rect.top + 1:
            print('hit right side')
            mario.rect.left = hits[0].rect.right + 1
            mario.cannot_move_left = True

        elif hits and not self.mario_dead:
            self.pos.y = hits[0].rect.top + 1
            self.on_pipe = True
            self.vel.y = 0
            self.can_jump = True
        else:
            self.on_pipe = False

    def mario_death(self):
        if self.mario_dead and self.mario_size == 0 and not self.mario_dead_cont:
            self.vel.x = 0
            self.vel.y = 0
            self.acc.y = 0
            self.image = pygame.image.load('Images/Mario-Movement/smol/death.png')
            self.dead_counter += 1
            print(self.dead_counter)
        if self.dead_counter >= 50:
            self.acc = vec(0, self.settings.PLAYER_GRAVITY)
            self.mario_dead_cont = True
            if self.dead_bool:
                self.vel.y = -10
            self.dead_bool = False
        self.place_mario()


    def check_with_items(self, mario, items):
        for item in items:
            collision = pygame.sprite.collide_rect(mario, item)
            if collision:
                print(item.__str__())

    def update(self, screen, current_level, mario, blocks, pipes, items):
        self.check_on_block(mario, blocks)
        self.check_with_pipes(mario, pipes)
        self.check_with_items(mario, items)
        if not mario.cant_move:
            self.mario_walking(screen, current_level)
        if self.mario_dead:
            self.cant_move = True
            self.mario_death()
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
