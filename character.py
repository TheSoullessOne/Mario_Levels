from pygame.sprite import Sprite
import pygame
from game_functions import update_all
vec = pygame.math.Vector2
from timer import Timer


class Character(Sprite):
    def __init__(self, screen, settings):
        super(Character, self).__init__()
        self.screen = screen
        self.settings = settings

        self.mario_size = 0     # 0 = smol mario, 1 = normal mario, 2 = fire boi

        self.image = pygame.image.load('Images/Mario-Movement/smol/mario-right.png')
        self.image_left = pygame.image.load('Images/Mario-Movement/smol/mario-left.png')
        self.left_walk_frames = ['Images/Mario-Movement/smol/mario-walk-left-1.png',
                                 'Images/Mario-Movement/smol/mario-walk-left-2.png',
                                 'Images/Mario-Movement/smol/mario-walk-left-3.png']
        self.right_walk_frames = ['Images/Mario-Movement/smol/mario-walk-right-1.png',
                                  'Images/Mario-Movement/smol/mario-walk-right-2.png',
                                  'Images/Mario-Movement/smol/mario-walk-right-3.png']
        self.grow_right_frames = ['Images/Mario-Movement/smol/mario-right.png',
                                  'Images/Mario-Movement/smol/smol-tolarge-right.png',
                                  'Images/Mario-Movement/normal/mario-right.png']
        self.grow_left_frames = ['Images/Mario-Movement/smol/mario-left.png',
                                 'Images/Mario-Movement/smol/smol-tolarge-left.png',
                                 'Images/Mario-Movement/normal/mario-left.png']
        self.change_size = None
        self.walk_left_anim = Timer(self.left_walk_frames, 150)
        self.walk_right_anim = Timer(self.right_walk_frames, 150)
        self.size_change_anim = None
        self.image_walking_right = pygame.image.load(self.walk_right_anim.image_rect())
        self.image_walking_left = pygame.image.load(self.walk_left_anim.image_rect())
        self.image_jump_right = pygame.image.load('Images/Mario-Movement/smol/mario-jump-right.png')
        self.image_jump_left = pygame.image.load('Images/Mario-Movement/smol/mario-jump-left.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect_bottom = self.rect.bottom
        self.sprite_delay = 0

        self.width = self.rect.width     # Image width
        self.height = self.rect.height    # Image height

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

        self.right_facing = True     # True is right, false is left
        self.on_block = False
        self.on_pipe = False
        self.can_jump = True

        self.starting_jump = 0
        self.rect.centerx = self.settings.screen_width / 2      # Starting Mario at center of screen
        self.rect.bottom = self.settings.screen_height - 100          # Starting Mario at bottom of screen
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.changing_to_big = False
        self.changing_to_smol = False

        self.y_bot = float(self.rect.bottom)
        self.start_jmp = self.y_bot
        self.start_jmp_bool = False

        self.falling = False   # Check for positive downward y-velocity after jumping

        self.cannot_move_left = False
        self.cannot_move_right = False

    def change_mario_size(self):
        if self.mario_size == 0 and not self.changing_to_smol:
            self.left_walk_frames = ['Images/Mario-Movement/smol/mario-walk-left-1.png',
                                     'Images/Mario-Movement/smol/mario-walk-left-2.png',
                                     'Images/Mario-Movement/smol/mario-walk-left-3.png']
            self.right_walk_frames = ['Images/Mario-Movement/smol/mario-walk-right-1.png',
                                      'Images/Mario-Movement/smol/mario-walk-right-2.png',
                                      'Images/Mario-Movement/smol/mario-walk-right-3.png']
            self.walk_left_anim = Timer(self.left_walk_frames, 150)
            self.walk_right_anim = Timer(self.right_walk_frames, 150)

            self.image = pygame.image.load('Images/Mario-Movement/smol/mario-right.png')
            self.image_left = pygame.image.load('Images/Mario-Movement/smol/mario-left.png')
            self.image_walking_right = pygame.image.load(self.walk_right_anim.image_rect())
            self.image_walking_left = pygame.image.load(self.walk_left_anim.image_rect())
            self.image_jump_right = pygame.image.load('Images/Mario-Movement/smol/mario-jump-right.png')
            self.image_jump_left = pygame.image.load('Images/Mario-Movement/smol/mario-jump-left.png')
            self.update_rect()
        elif self.mario_size == 1 and not self.changing_to_big:
            self.left_walk_frames = ['Images/Mario-Movement/normal/mario-walk-left-1.png',
                                     'Images/Mario-Movement/normal/mario-walk-left-2.png',
                                     'Images/Mario-Movement/normal/mario-walk-left-3.png']
            self.right_walk_frames = ['Images/Mario-Movement/normal/mario-walk-right-1.png',
                                      'Images/Mario-Movement/normal/mario-walk-right-2.png',
                                      'Images/Mario-Movement/normal/mario-walk-right-3.png']
            self.walk_left_anim = Timer(self.left_walk_frames, 150)
            self.walk_right_anim = Timer(self.right_walk_frames, 150)

            self.image = pygame.image.load('Images/Mario-Movement/normal/mario-right.png')
            self.image_left = pygame.image.load('Images/Mario-Movement/normal/mario-left.png')
            self.image_walking_right = pygame.image.load(self.walk_left_anim.image_rect())
            self.image_walking_left = pygame.image.load(self.walk_left_anim.image_rect())
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
        if self.right_facing:
            self.change_size = Timer(self.grow_right_frames, 150, loop_once=True)
            self.image = pygame.image.load(self.change_size.image_rect())
        else:
            self.change_size = Timer(self.grow_left_frames, 150, loop_once=True)
            self.image = pygame.image.load(self.change_size.image_rect())
        self.sprite_delay += 1
        self.update_rect()
        if self.sprite_delay >= 4:
            self.changing_to_big = False
            self.sprite_delay = 0
            self.change_mario_size()
        self.blit_me(self.screen)
        self.mario_size = 1
        self.update_rect()

    def big_to_smol(self):
        if self.right_facing:
            shrink_frames = self.grow_right_frames
            shrink_frames.reverse()
            self.change_size = Timer(shrink_frames, 60, loop_once=True)
            self.image = pygame.image.load(self.change_size.image_rect())
        else:
            shrink_frames = self.grow_left_frames
            shrink_frames.reverse()
            self.change_size = Timer(shrink_frames, 60, loop_once=True)
            self.image = pygame.image.load(self.change_size.image_rect())
        self.sprite_delay += 1
        if self.sprite_delay >= 4:
            self.changing_to_smol = False
            self.sprite_delay = 0
            self.change_mario_size()
        self.blit_me(self.screen)
        self.mario_size = 0
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
                if self.right_facing:  # jumping right
                    screen.blit(self.image_jump_right, self.rect)
                elif not self.right_facing:  # jumping left
                    screen.blit(self.image_jump_left, self.rect)
            elif self.right_facing and not self.moving_right and not self.moving_left:
                screen.blit(self.image, self.rect)  # looking right
            elif not self.right_facing and not self.moving_right and not self.moving_left:
                screen.blit(self.image_left, self.rect)  # looking left
            elif self.moving_right:
                # walking right animation
                self.image_walking_right = pygame.image.load(self.walk_right_anim.image_rect())
                screen.blit(self.image_walking_right, self.rect)
            elif self.moving_left:
                # walking left animation
                self.image_walking_left = pygame.image.load(self.walk_left_anim.image_rect())
                screen.blit(self.image_walking_left, self.rect)
        else:
            screen.blit(self.image, self.rect)

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
                self.right_facing = False
                self.moving_left = True
            else:
                self.moving_left = False
        if self.rect.right <= self.settings.screen_width and not self.cannot_move_right:
            if self.rect.right > self.settings.screen_width / 2 and keys[pygame.K_RIGHT]:
                update_all(screen, current_level, self.settings)
            else:
                if keys[pygame.K_RIGHT]:
                    self.acc.x = self.settings.MOVE_SPEED
                    self.right_facing = True
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

        if hits and not self.mario_dead and \
            hits[0].rect.centery <= mario.rect.top <= hits[0].rect.bottom and \
            hits[0].rect.left <= mario.rect.centerx <= hits[0].rect.right:
            self.pos.y = hits[0].rect.bottom + self.height + 1
            self.vel.y = 0
            self.acc.y = 0

            hits[0].hit_block()
            for block in platforms:
                collide = self.rect.colliderect(block)
                if collide and self.mario_size >= 1:
                    if str(block.__str__()).__contains__("BrickBlock"):
                        platforms.remove(block)
            if hits[0].item is not None:
                if str(hits[0].item.__str__()).__contains__("Coin"):
                    if not hits[0].item.picked_up:
                        self.settings.score += hits[0].item.points
                        self.settings.coin_count += 1
                    if self.settings.coin_count >= 100:
                        self.settings.lives += 1
                        self.settings.coin_count -= 100
        elif hits and not self.mario_dead and \
             hits[0].rect.left <= mario.rect.right <= hits[0].rect.centerx and \
            (hits[0].rect.top <= mario.rect.bottom or hits[0].rect.bottom >= mario.rect.top):
            print('hit left')
            self.pos.x = hits[0].rect.left - 17
        # elif hits and not self.mario_dead and \
        #     hits[0].rect.right >= mario.rect.left >= hits[0].rect.centerx and \
        #     (hits[0].rect.top <= mario.rect.bottom or hits[0].rect.bottom >= mario.rect.top):
        #     self.pos.x = hits[0].rect.right
        if hits and not self.mario_dead and \
                hits[0].rect.top <= mario.rect.bottom <= hits[0].rect.centery and \
                (hits[0].rect.left <= mario.rect.right or hits[0].rect.right >= mario.rect.left):
            # elif hits and not self.mario_dead:
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

    def check_with_items(self, mario, items, settings):
        for item in items:
            collision = self.rect.colliderect(item)
            if collision:
                if str(item.__str__()).__contains__("MagicMushroom"):
                    item.picked_up = True
                    # self.big_to_smol()
                    settings.score += item.points
                    item.kill()
                elif str(item.__str__()).__contains__("OneUpMushroom"):
                    item.picked_up = True
                    settings.lives += 1
                    item.kill()
                elif str(item.__str__()).__contains__("FireFlower"):
                    item.picked_up = True
                    settings.score += item.points
                    # self.to_spicy()
                elif str(item.__str__()).__contains__("Coin"):
                    item.picked_up = True
                    settings.score += item.points
                    item.kill()

    def check_with_enemies(self, enemies):
        for enemy in enemies:
            collision = pygame.sprite.collide_rect(self, enemy)
            if collision:
                if (enemy.rect.left < self.rect.right or self.rect.left < enemy.rect.right) and \
                        enemy.rect.centery >= self.rect.bottom >= enemy.rect.top:
                    print('hit?')
                    enemies.remove(enemy)
                else: #  death animation
                    self.settings.lives -= 1

    def update(self, settings, screen, current_level, mario, blocks, pipes, items, enemies):
        self.check_on_block(mario, blocks)
        self.check_with_pipes(mario, pipes)
        self.check_with_items(mario, items, settings)
        self.check_with_enemies(enemies)
        if not mario.cant_move:
            self.mario_walking(screen, current_level)
        if self.mario_dead:
            self.cant_move = True
            self.mario_death()
        if self.changing_to_big:
            self.smol_to_big()
        elif self.changing_to_smol:
            self.big_to_smol()

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
