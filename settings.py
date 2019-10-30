from block import *


class Settings:
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 500
        self.bg_color = (156, 219, 255)

        self.max_jump_height = 250
        self.init_jmp_speed = 4
        self.max_jmp_speed = 1
        self.move_speed = 10.0
        self.init_gravity = float(0.03)
        self.max_gravity = 3
