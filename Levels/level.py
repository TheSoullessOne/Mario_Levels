from block import *
from background import Background
from environment import *
from pygame.sprite import Group
import pygame


class Level:
    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.background = Background(screen, settings, 'Images/Backgrounds/1-1-bg.png')
        self.bg_img = self.background.image
        self.blocks = Group()
        self.items = Group()
        self.enemies = Group()
        self.pipes = Group()
        self.flag_pole = FlagPole(screen, settings, 0, 0)

    def initialize_blocks(self): pass
    def initialize_enemies(self): pass
    def initialize_items(self): pass
    def initialize_pipes(self): pass

    def create_item_block(self, item, x, y): pass
    def create_brick_block(self, x, y): pass
    def create_block(self, x, y): pass
    def create_up_hill(self, w, h, x_start): pass
    def create_down_hill(self, w, h, x_start): pass
    def create_pipe(self, x, y, type='s'): pass
    def create_corner_pipe(self, x, y, type='s'): pass

    def blit_level(self):
        for pipe in self.pipes:
            pipe.blit_me()

        for block in self.blocks:
            block.blit_me(self.screen)

        for enemy in self.enemies:
            enemy.blit_me()

        self.flag_pole.blit_me()

    # For testing only
    def draw_flag(self, w, h, x, y):
        b1 = pygame.rect.Rect(x, y, w, h)
        pygame.draw.rect(self.bg_img, (255, 0, 255), b1)