from enemies import *
from items import *
from block import *
from environment import *
from Levels.level import Level


class Level1_1(Level):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.initialize_blocks()
        self.initialize_pipes()
        self.initialize_enemies()

        self.flag_pole.rect.x = 7052
        self.flag_pole.rect.y = 71

    def initialize_blocks(self):
        upper_y = 160
        lower_y = 304

        # First grouping
        self.create_item_block(self.create_coin(), 570, lower_y)  # coin
        self.create_item_block(self.create_coin(), 786, upper_y)  # coin

        self.create_brick_block(714, lower_y)
        self.create_item_block(self.create_magic_mushroom(), 750, lower_y)  # magic mushroom
        self.create_brick_block(786, lower_y)
        self.create_item_block(self.create_coin(), 822, lower_y) # coin
        self.create_brick_block(858, lower_y)

        self.create_brick_block(2750, lower_y)
        self.create_item_block(self.create_fire_flower(), 2786, lower_y)  # FIRE FLOWER
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
        self.create_item_block(self.create_coin(), 3357, upper_y)  # coin

        self.create_brick_block(3357, lower_y)

        self.create_brick_block(3571, lower_y)
        self.create_brick_block(3607, lower_y)

        self.create_item_block(self.create_coin(), 3785, lower_y) # coin
        self.create_item_block(self.create_coin(), 3892, lower_y) # coin
        self.create_item_block(self.create_coin(), 3999, lower_y) # coin
        self.create_item_block(self.create_fire_flower(), 3892, upper_y) # fire flower

        self.create_brick_block(4214, lower_y)

        self.create_brick_block(4321, upper_y)
        self.create_brick_block(4357, upper_y)
        self.create_brick_block(4393, upper_y)

        self.create_brick_block(4571, upper_y)
        self.create_item_block(self.create_coin(), 4607, upper_y) # coin
        self.create_item_block(self.create_coin(), 4643, upper_y) # coin
        self.create_brick_block(4679, upper_y)

        self.create_brick_block(4607, lower_y)
        self.create_brick_block(4643, lower_y)

        self.create_brick_block(5999, lower_y)
        self.create_brick_block(6035, lower_y)
        self.create_item_block(self.create_coin(), 6071, lower_y) # coin
        self.create_brick_block(6107, lower_y)

        self.create_up_hill(4, 4, 4785)
        self.create_down_hill(4, 4, 4999)
        self.create_up_hill(5, 4, 5285)
        self.create_down_hill(4, 4, 5535)
        self.create_up_hill(9, 8, 6463)

        self.create_floor(2430, 445)
        self.create_floor(2430, 480)
        for i in range(70):
            self.create_floor(i * 35, 445)
            self.create_floor(i * 35, 480)

        self.create_floor(3037, 445)
        self.create_floor(3037, 480)
        for i in range(15):
            self.create_floor(i * 35 + 2535, 445)
            self.create_floor(i * 35 + 2535, 480)

        self.create_floor(5430, 445)
        self.create_floor(5430, 480)
        for i in range(65):
            self.create_floor(i * 35 + 3176, 445)
            self.create_floor(i * 35 + 3176, 480)

        for i in range(50):
            self.create_floor(i * 35 + 5535, 445)
            self.create_floor(i * 35 + 5535, 480)

    def initialize_pipes(self):
        self.create_pipe(1000, 374)
        self.create_pipe(1357, 338, 'm')
        self.create_pipe(1642, 303, 'l')
        self.create_pipe(2035, 303, 'l')  # entrance to bonus room
        self.create_pipe(5821, 374)  # exit to bonus room
        self.create_pipe(6392, 374)

    def initialize_enemies(self):
        self.create_little_goomba(799, 398)

    def create_little_goomba(self, x, y):
        goomba = LittleGoomba(self.screen, self.settings, x, y)
        self.enemies.add(goomba)

    def create_item_block(self, item, x, y):
        ib = ItemBlock(item, self.screen, self.settings, x, y)
        self.blocks.add(ib)
        self.items.add(item)

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

    def create_pipe(self, x, y, size='s'):
        # s = small, m = medium, l = large
        if size == 's':
            pipe = GreenSmallPipe(self.screen, self.settings, x, y)
            # self.draw_flag(72, 72, x, y)
        elif size == 'm':
            pipe = GreenMedPipe(self.screen, self.settings, x, y)
            # self.draw_flag(72, 108, x, y)
        elif size == 'l':
            pipe = GreenTallPipe(self.screen, self.settings, x, y)
            # self.draw_flag(72, 144, x, y)
        self.pipes.add(pipe)

    def create_floor(self, x, y):
        block = FloorBlock(self.screen, self.settings, x, y)
        self.blocks.add(block)

    def create_coin(self):
        coin = Coin(self.screen, self.settings, 0, 0)
        self.items.add(coin)
        return coin

    def create_magic_mushroom(self):
        magic_mushroom = MagicMushroom(self.screen, self.settings, 0, 0)
        self.items.add(magic_mushroom)
        return magic_mushroom

    def create_fire_flower(self):
        fire_flower = FireFlower(self.screen, self.settings, 0, 0)
        self.items.add(fire_flower)
        return fire_flower