from enemies import *
from items import *
from block import *
from background import Background
from Levels.level import Level


class Level1_2(Level):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.background = Background(screen, settings, 'Images/Backgrounds/1-2-bg.png')
        self.bg_img = self.background.image
        self.initialize_blocks()

    def initialize_blocks(self):
        self.create_block_column(3, 409, 11, 'brick')

        self.create_block_row(216, 52, 131, 'brick')

        self.create_item_block(None, 359, 303)
        self.create_item_block(None, 395, 303)
        self.create_item_block(None, 431, 303)
        self.create_item_block(None, 467, 303)
        self.create_item_block(None, 503, 303)

        self.create_block(608, 410)
        self.create_block_column(680, 410, 2)
        self.create_block_column(752, 410, 3)
        self.create_block_column(824, 410, 4)
        self.create_block_column(896, 410, 4)
        self.create_block_column(968, 410, 3)

        self.create_brick_block(1038, 266)

        self.create_block_column(1109, 410, 3)
        self.create_block_column(1181, 410, 2)

        self.create_block_column(1395, 302, 3, 'brick')
        self.create_brick_block(1431, 302)
        self.create_block_column(1467, 302, 3, 'brick')
        self.create_brick_block(1503, 230)
        self.create_brick_block(1539, 230)
        self.create_block_column(1575, 302, 3, 'brick')
        self.create_brick_block(1611, 302)
        self.create_block_column(1647, 302, 3, 'brick')

        self.create_block_column(1859, 302, 5, 'brick')
        self.create_block_column(1895, 302, 5, 'brick')
        self.create_block_column(1931, 374, 3, 'brick')
        self.create_block_column(1967, 374, 3, 'brick')
        self.create_block_column(1931, 122, 2, 'brick')
        self.create_block_column(1967, 122, 2, 'brick')

        self.create_block_row(2074, 88, 6, 'brick')
        self.create_block_row(2074, 124, 6, 'brick')
        self.create_block_row(2218, 160, 2, 'brick')
        self.create_block_row(2218, 196, 2, 'brick')
        self.create_block_row(2218, 232, 2, 'brick')
        self.create_block_row(2218, 268, 2, 'brick')
        self.create_block_row(2074, 304, 6, 'brick')

        self.create_block_row(2360, 88, 4, 'brick')
        self.create_block_row(2360, 124, 4, 'brick')
        self.create_block_column(2396, 268, 4, 'brick')
        self.create_block_row(2396, 304, 3, 'brick')
        self.create_brick_block(2468, 268)

        self.create_block_column(2573, 302, 5, 'brick')
        self.create_block_column(2609, 302, 5, 'brick')

        self.create_block_row(2716, 88, 4, 'brick')
        self.create_block_row(2716, 124, 4, 'brick')

        self.create_block_row(2716, 302, 4, 'brick')

        self.create_block_row(3001, 231, 6, 'brick')
        self.create_block_row(3001, 267, 6, 'brick')

        self.create_block_column(4358, 410, 3, 'brick')
        self.create_block_column(4394, 410, 3, 'brick')

        self.create_up_hill(5, 4, 4751)

        self.create_block_row(5180, 266, 6, 'brick')

        self.create_block_row(5751, 53, 7, 'brick')
        self.create_block_row(6073, 53, 17, 'brick')
        self.create_block_row(6073, 89, 7, 'brick')
        self.create_block_row(6073, 125, 7, 'brick')
        self.create_block_row(6073, 161, 7, 'brick')
        self.create_block_row(6073, 197, 7, 'brick')
        self.create_block_row(6073, 233, 7, 'brick')
        self.create_block_row(6073, 269, 7, 'brick')
        self.create_block_row(6073, 305, 7, 'brick')
        self.create_block_row(5713, 341, 17, 'brick')
        self.create_block_row(5713, 377, 17, 'brick')
        self.create_block_row(5713, 413, 17, 'brick')

        self.create_block_column(6787, 410, 11, 'brick')
        self.create_block_column(6823, 410, 11, 'brick')

    def create_item_block(self, item, x, y):
        block = BlueItemBlock(item, self.screen, self.settings, x, y)
        self.blocks.add(block)

    def create_brick_block(self, x, y):
        block = BlueBrickBlock(self.screen, self.settings, x, y)
        self.blocks.add(block)

    def create_block(self, x, y):
        block = BlueBlock(self.screen, self.settings, x, y)
        self.blocks.add(block)

    def create_block_column(self, x, start_y, height, type='block'):
        for i in range(height):
            if type == 'brick':
                self.create_brick_block(x, start_y)
            elif type == 'block':
                self.create_block(x, start_y)
            start_y -= 36

    def create_block_row(self, start_x, y, length, type='block'):
        for i in range(length):
            if type == 'brick':
                self.create_brick_block(start_x, y)
            elif type == 'block':
                self.create_block(start_x, y)
            start_x += 36

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