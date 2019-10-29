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
        w, h = 36, 36
        item_block_color = (255, 0, 255)  # hot pink
        default_block_color = (0, 255, 255)  # teal

        self.create_item_block(None, 570, 305)
        self.create_item_block(None, 750, 305)
        self.create_item_block(None, 785, 160)
        self.create_item_block(None, 822, 305)
        self.create_brick_block(714, 305)
        self.create_brick_block(785, 305)
        self.create_brick_block(855, 305)


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