from block import *
from background import Background
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

        self.initialize_blocks()

    def initialize_blocks(self): pass
    def initialize_enemies(self): pass

    def create_item_block(self, item, x, y):
        ib = ItemBlock(item, self.bg_img, self.settings, x, y)
        self.blocks.add(ib)

    def create_brick_block(self, x, y):
        block = BrickBlock(self.screen, self.settings, x, y)
        self.blocks.add(block)

    def create_block(self, x, y):
        block = Block(self.screen, self.settings, x, y)
        self.blocks.add(block)

    def create_up_hill(self, w, h, x_start):
        y_current = 410
        for row in range(h):
            x_current = x_start
            for column in range(w):
                self.create_block(x_current, y_current)
                x_current += 36
            w -= 1
            x_start += 36
            y_current -= 36

    def create_down_hill(self, w, h, x_start):
        y_current = 410
        for row in range(h):
            x_current = x_start
            for column in range(w):
                self.create_block(x_current, y_current)
                x_current += 36
            w -= 1
            y_current -= 36

    def blit_level(self):
        for block in self.blocks:
            block.blit_me(self.screen)

    def initialize_items(self): pass

    def initialize_enemies(self): pass

    # For testing only
    def draw_flag(self, color, x, y):
        w, h = 36, 36
        b1 = pygame.rect.Rect(x, y, w, h)
        pygame.draw.rect(self.bg_img, color, b1)