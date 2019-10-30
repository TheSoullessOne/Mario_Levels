from enemies import *
from items import *
from block import *
from background import Background
from Levels.level import Level


class Level1_3(Level):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.background = Background(screen, settings, 'Images/Backgrounds/1-3-bg.png')
        self.bg_img = self.background.image
        self.initialize_blocks()

    def initialize_blocks(self):
        self.create_tree(2, 2, 678, 446)
        self.create_tree(6, 5, 893, 340)
        self.create_tree(3, 3, 964, 195)
        self.create_tree(1, 2, 1178, 447)
        self.create_tree(3, 6, 1286, 304)
        self.create_tree(5, 10, 1465, 161)
        self.create_tree(2, 1, 1821, 482)
        self.create_tree(3, 1, 2143, 482)
        self.create_tree(2, 7, 2175, 197)
        self.create_tree(3, 1, 2357, 482)
        self.create_tree(1, 5, 2535, 339)
        self.create_tree(4, 8, 2750, 232)
        self.create_tree(2, 3, 3535, 411)
        self.create_tree(6, 7, 3750, 268)
        self.create_tree(1, 1, 4071, 482)
        self.create_tree(2, 5, 4178, 340)
        self.create_tree(2, 5, 4392, 340)

        self.create_block_column(4928, 410, 4)
        self.create_block_column(4964, 410, 4)
        self.create_block_column(5000, 410, 6)
        self.create_block_column(5036, 410, 6)
        self.create_block_column(5072, 410, 8)
        self.create_block_column(5108, 410, 8)

    def create_block_column(self, x, start_y, height, type='block'):
        for i in range(height):
            self.create_block(x, start_y)
            start_y -= 36

    def create_tree_block(self, x, y):
        block = TreeBlock(self.screen, self.settings, x, y)
        self.blocks.add(block)

    def create_left_tree_top(self, x, y):
        block = LeftTreeTop(self.screen, self.settings, x, y)
        self.blocks.add(block)

    def create_mid_tree_top(self, x, y):
        block = MidTreeTop(self.screen, self.settings, x, y)
        self.blocks.add(block)

    def create_right_tree_top(self, x, y):
        block = RightTreeTop(self.screen, self.settings, x, y)
        self.blocks.add(block)

    def create_tree_trunk(self, w, h, start_x, start_y):
        color = (255, 0, 255)
        for row in range(h):
            current_x = start_x
            for column in range(w):
                self.create_tree_block(current_x,start_y)
                current_x += 36
            start_y += 36

    def create_tree_top(self, w, h, start_x, start_y):
        color = (255, 0, 255)
        start_y -= 36
        current_x = start_x - 36

        self.create_left_tree_top(current_x, start_y)
        current_x += 36
        for column in range(w):
            self.create_mid_tree_top(current_x, start_y)
            current_x += 36
        self.create_right_tree_top(current_x, start_y)

    def create_tree(self, w, h, start_x, start_y):
        self.create_tree_trunk(w, h, start_x, start_y)
        self.create_tree_top(w, h, start_x, start_y)