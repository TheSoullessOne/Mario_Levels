import pygame
from timer import Timer
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, screen, settings, x, y):
        super(Enemy, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('Images/Enemies/KoopaParatroopa/red-left-1.png')
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery
        self.spawn_x = x
        self.spawn_y = y
        self.rect.x = x
        self.rect.y = y

        # Turns on their motion if they are in viewfinder
        self.on_screen = False

    # def blit_me(self):
    #     if self.rect.left < self.settings.screen_width + 5 and not self.on_screen:
    #         self.on_screen = True
    #     if self.on_screen:
    #         self.screen.blit(self.image, self.rect)

    def update(self, mario): pass

    def hit(self): pass

    def set_image(self): pass

    def collide(self, blocks, pipes): pass

    def update_rect(self, x, y):
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery
        self.spawn_x = x
        self.spawn_y = y
        self.rect.x = x
        self.rect.y = y


class KoopaParatroopa(Enemy):
    def __init__(self, screen, settings, color, x, y):
        super().__init__(screen, settings, x, y)
        self.color = color
        self.image = self.set_image()
        self.update_rect(x, y)

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self, mario):
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
    def __init__(self, screen, settings, color, x, y):
        super().__init__(screen, settings, x, y)
        self.color = color
        self.image = self.set_image()
        self.update_rect(x, y)
        self.green_frames_left = ['Images/Enemies/KoopaTroopa/green-left-1.png',
                                  'Images/Enemies/Koopatroopa/green-left-2.png']
        self.green_frames_right = ['Images/Enemies/KoopaTroopa/green-right-1.png',
                                   'Images/Enemies/Koopatroopa/green-right-2.png']
        self.red_frames_left = ['Images/Enemies/KoopaTroopa/red-left-1.png',
                                'Images/Enemies/Koopatroopa/red-left-2.png']
        self.red_frames_right = ['Images/Enemies/KoopaTroopa/red-right-1.png',
                                 'Images/Enemies/Koopatroopa/red-right-2.png']
        self.green_left_animation = Timer(self.green_frames_left, 150)
        self.green_right_animation = Timer(self.green_frames_right, 150)
        self.red_left_animation = Timer(self.red_frames_left, 150)
        self.red_right_animation = Timer(self.red_frames_right, 150)
        self.moving_left = True
        self.moving_right = False

    def update(self, mario):
        if self.on_screen:
            if self.moving_left:
                self.rect.x -= 1
            elif self.moving_right:
                self.rect.x += 1
            if self.rect.x < mario.rect.x:
                self.moving_right = True
                self.moving_left = False
            elif self.rect.x > mario.rect.x:
                self.moving_left = True
                self.moving_right = False

    def set_image(self):
        if self.color == 'red':
            return pygame.image.load('Images/Enemies/KoopaTroopa/red-left-1.png')
        elif self.color == 'green':
            return pygame.image.load('Images/Enemies/Koopatroopa/green-left-1.png')

    def stomped(self):
        self.image = pygame.image.load()

    def blit_me(self):
        if self.rect.left < self.settings.screen_width + 5 and not self.on_screen:
            self.on_screen = True
        if self.on_screen:
            if self.color == 'green':
                if self.moving_left:
                    self.image = pygame.image.load(self.green_left_animation.image_rect())
                elif self.moving_right:
                    self.image = pygame.image.load(self.green_right_animation.image_rect())
            elif self.color == 'red':
                if self.moving_left:
                    self.image = pygame.image.load(self.red_left_animation.image_rect())
                elif self.moving_right:
                    self.image = pygame.image.load(self.red_right_animation.image_rect())
            self.screen.blit(self.image, self.rect)

    def collide(self, blocks, pipes):
        for block in blocks:
            collision = pygame.sprite.collide_rect(self, block)
            if collision:
                if self.rect.left == block.rect.right and self.rect.bottom == block.rect.bottom:
                    self.moving_left = False
                    self.moving_right = True
                elif self.rect.right == block.rect.left and self.rect.bottom == block.rect.bottom:
                    self.moving_right = False
                    self.moving_left = True

        for pipe in pipes:
            collision_pipe = pygame.sprite.collide_rect(self, pipe)
            if collision_pipe:
                if self.rect.left <= pipe.rect.right and self.rect.bottom >= pipe.rect.bottom:
                    self.moving_left = False
                    self.moving_right = True
                elif self.rect.right >= pipe.rect.left and self.rect.bottom >= pipe.rect.bottom:
                    self.moving_right = False
                    self.moving_left = True


class LittleGoomba(Enemy):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        move_frames = ['Images/Enemies/LittleGoomba/goomba-1.png', 'Images/Enemies/LittleGoomba/goomba-2.png']
        self.movement = Timer(move_frames, settings.enemy_anim_rate)
        self.image = pygame.image.load('Images/Enemies/LittleGoomba/goomba-1.png')
        self.update_rect(x, y)
        self.animation = Timer(move_frames, 150)

        self.moving_left = True
        self.moving_right = False

    def update(self, mario):
        if self.on_screen:
            if self.moving_left:
                self.rect.x -= self.settings.enemy_move_speed
            elif self.moving_right:
                self.rect.x += self.settings.enemy_move_speed

    def stomped(self): pass

    def blit_me(self):
        if self.rect.left < self.settings.screen_width + 5 and not self.on_screen:
            self.on_screen = True
        if self.on_screen:
            self.image = pygame.image.load(self.animation.image_rect())
            self.screen.blit(self.image, self.rect)

    def collide(self, blocks, pipes):
        coll = pygame.sprite.spritecollide(self, blocks, False)
        if coll:
            print('collided')
        for block in blocks:
            collision = self.rect.colliderect(block)
            if collision:
                print('collision')
                if self.rect.left <= block.rect.right and self.moving_left:
                    self.moving_left = False
                    self.moving_right = True
                elif self.rect.right >= block.rect.left and self.moving_right:
                    self.moving_right = False
                    self.moving_left = True
            else:
                self.rect.y += 0.5

        for pipe in pipes:
            collision_pipe = pygame.sprite.collide_rect(self, pipe)
            if collision_pipe:
                if self.rect.left <= pipe.rect.right and self.moving_left:
                    self.moving_left = False
                    self.moving_right = True
                elif self.rect.right >= (pipe.rect.left - 10) and self.moving_right:
                    self.moving_right = False
                    self.moving_left = True


class PiranhaPlant(Enemy):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Enemies/PiranhaPlant/green-1.png')

        self.near_mario = True
        self.moving_up = False
        self.moving_down = False

    def update(self, mario): pass

    def collide(self, blocks, pipes):
        pass


class Podoboo(Enemy):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load()

        # Add movements

    def update(self, mario): pass

    def collide(self, blocks, pipes): pass


class CheepCheep(Enemy):
    def __init__(self, screen, settings, color, x, y):
        super().__init__(screen, settings, x, y)
        self.color = color
        self.image = self.set_image()

    def update(self, mario): pass

    def collide(self, blocks, pipes): pass

    def set_image(self):
        if self.color == 'red':
            return pygame.image.load('Images/Enemies/CheepCheep/red-left-1.png')
        elif self.color == 'green':
            return pygame.image.load('Images/Enemies/CheepCheep/green-left-1.png')
        elif self.color == 'gray':
            return pygame.image.load('Images/Enemies/CheepCheep/gray-left-1.png')


class FireBar(Enemy):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = None

    def update(self, mario): pass

    def collide(self, blocks, pipes): pass


class Bloober(Enemy):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('Images/Enemies/Bloober/bloober-1.png')

    def update(self, mario): pass

    def collide(self, blocks, pipes): pass
    # tracks mario's x movements but continues swimming animation
