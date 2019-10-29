from enemies import *
from items import *
from background import Background
from pygame.sprite import Group
from level import Level
import pygame


class Level11(Level):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        # self.screen = screen
        # self.screen_rect = screen.get_rect()
        # self.settings = settings
        # self.background = Background(screen, settings, 'Images/Backgrounds/1-1-bg.png')
        # self.bg_img = self.background.image
        # self.blocks = Group()
        # self.items = Group()
        # self.enemies = Group()
        #
        # self.initialize_blocks()

    def initialize_blocks(self):
        upper_y = 160
        lower_y = 304

        coin = Coin(self.screen, self.settings)
        magic_mushroom = MagicMushroom(self.screen, self.settings)
        fire_flower = FireFlower(self.screen, self.settings)

        # First grouping
        self.create_item_block(coin, 570, lower_y)  # coin
        self.create_item_block(coin, 786, upper_y)  # coin

        self.create_brick_block(714, lower_y)
        self.create_item_block(magic_mushroom, 750, lower_y)  # magic mushroom
        self.create_brick_block(786, lower_y)
        self.create_item_block(coin, 822, lower_y) # coin
        self.create_brick_block(858, lower_y)

        self.create_brick_block(2750, lower_y)
        self.create_item_block(fire_flower, 2786, lower_y)  # FIRE FLOWER
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
        self.create_item_block(coin, 3357, upper_y)  # coin

        self.create_brick_block(3357, lower_y)

        self.create_brick_block(3571, lower_y)
        self.create_brick_block(3607, lower_y)

        self.create_item_block(coin, 3785, lower_y) # coin
        self.create_item_block(coin, 3892, lower_y) # coin
        self.create_item_block(coin, 3999, lower_y) # coin
        self.create_item_block(fire_flower, 3892, upper_y) # fire flower

        self.create_brick_block(4214, lower_y)

        self.create_brick_block(4321, upper_y)
        self.create_brick_block(4357, upper_y)
        self.create_brick_block(4393, upper_y)

        self.create_brick_block(4571, upper_y)
        self.create_item_block(coin, 4607, upper_y) # coin
        self.create_item_block(coin, 4643, upper_y) # coin
        self.create_brick_block(4679, upper_y)

        self.create_brick_block(4607, lower_y)
        self.create_brick_block(4643, lower_y)

        self.create_brick_block(5999, lower_y)
        self.create_brick_block(6035, lower_y)
        self.create_item_block(coin, 6071, lower_y) # coin
        self.create_brick_block(6107, lower_y)

        self.create_up_hill(4, 4, 4785)
        self.create_down_hill(4, 4, 4999)
        self.create_up_hill(5, 4, 5285)
        self.create_down_hill(4, 4, 5535)
        self.create_up_hill(9, 8, 6463)