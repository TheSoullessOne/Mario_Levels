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
        self.create_tree_trunk(2, 2, 678, self.settings.screen_height + 18)

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
            for column in range(w):
                # self.create_tree_block(start_x,start_y)
                self.draw_flag(color, start_x, start_y)

    def create_tree_top(self, w, h, start_x, start_y):
        h += 36
        start_x -= 36

        self.create_left_tree_top(start_x, start_y)
        for column in range(w): pass
