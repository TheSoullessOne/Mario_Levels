from enemies import *
from items import *
from block import *
from background import Background
from pygame.sprite import Group
import pygame

class Level11:
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

    def initialize_blocks(self):
        upper_y = 160
        lower_y = 304

        # First grouping
        self.create_item_block(None, 570, lower_y)
        self.create_item_block(None, 786, upper_y)

        self.create_brick_block(714, lower_y)
        self.create_item_block(None, 750, lower_y)
        self.create_brick_block(786, lower_y)
        self.create_item_block(None, 822, lower_y)
        self.create_brick_block(858, lower_y)

        self.create_brick_block(2750, lower_y)
        self.create_item_block(None, 2786, lower_y)
        self.create_brick_block(2822, lower_y)

        self.create_brick_block(2856, upper_y)
        self.create_brick_block(2892, upper_y)
        self.create_brick_block(2928, upper_y)
        self.create_brick_block(2964, upper_y)
        self.create_brick_block(3000, upper_y)
        self.create_brick_block(3036, upper_y)
        self.create_brick_block(3072, upper_y)
        self.create_brick_block(3108, upper_y)

        self.create_brick_block(3249, upper_y)
        self.create_brick_block(3285, upper_y)
        self.create_brick_block(3321, upper_y)
        self.create_item_block(None, 3357, upper_y)

        self.create_brick_block(3357, lower_y)

        self.create_brick_block(3571, lower_y)
        self.create_brick_block(3607, lower_y)

        self.create_item_block(None, 3785, lower_y)
        self.create_item_block(None, 3892, lower_y)
        self.create_item_block(None, 3999, lower_y)
        self.create_item_block(None, 3892, upper_y)

        self.create_brick_block(4214, lower_y)

        self.create_brick_block(4321, upper_y)
        self.create_brick_block(4357, upper_y)
        self.create_brick_block(4393, upper_y)

        self.create_brick_block(4571, upper_y)
        self.create_item_block(None, 4607, upper_y)
        self.create_item_block(None, 4643, upper_y)
        self.create_brick_block(4679, upper_y)

        self.create_brick_block(4607, lower_y)
        self.create_brick_block(4643, lower_y)

        self.create_brick_block(5999, lower_y)
        self.create_brick_block(6035, lower_y)
        self.create_item_block(None, 6071, lower_y)
        self.create_brick_block(6107, lower_y)


    def create_item_block(self, item, x, y):
        ib = ItemBlock(None, self.bg_img, self.settings, x, y)
        self.blocks.add(ib)

    def create_brick_block(self, x, y):
        block = BrickBlock(self.screen, self.settings, x, y)
        self.blocks.add(block)

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
# ITEM BLOCK:
# ------------
# 590, 321
# 767, 321
# 803, 179
# 839, 321
# ------------
# 2786, 303
# 3358, 160
#
# 3785, 303
# 3892, 303
# 3999, 303
# 3892, 160
#
# 4607, 160
# 4641, 160
#
# 6072, 302
#
# BRICK BLOCK:
# ---------------
# 715, 305
# 785, 305
# 855, 305
# ----------
# 2750, 305
# 2820, 303
#
# start: 2856, 160
# end: 3107, 160
# start: 3249, 160
# end: 3322, 160
#
# 3356, 303
# 3571, 303
# 3607, 303
#
# 4213, 303
# start: 4321, 160
# end: 4392, 160
#
# 4570, 160
# 4678, 160
#
# 4606, 303
# 4643, 303
#
# 6000, 303
# 6036, 303
# 6106, 303