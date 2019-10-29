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

        print(len(self.blocks))
        # default blocks
        b1 = pygame.rect.Rect(714, 304, w, h)
        pygame.draw.rect(self.bg_img, default_block_color, b1)
        b2 = pygame.rect.Rect(785, 305, w, h)
        pygame.draw.rect(self.bg_img, default_block_color, b2)
        b3 = pygame.rect.Rect(855, 305, w, h)
        pygame.draw.rect(self.bg_img, default_block_color, b3)


    def create_item_block(self, item, x, y):
        ib = ItemBlock(None, self.bg_img, self.settings, x, y)
        self.blocks.add(ib)

    def blit_level(self):
        for block in self.blocks:
            block.blit_me(self.screen)


    def initialize_items(self): pass
    def initialize_enemies(self): pass

