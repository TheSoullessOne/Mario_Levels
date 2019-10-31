from block import *


class Settings:
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 500
        self.bg_color = (156, 219, 255)

        self.max_jump_height = 250
        self.init_jmp_speed = float(0.8)
        self.max_jmp_speed = 1
        self.move_speed = float(0.9)
        self.init_gravity = float(0.3)
        self.max_gravity = 10
        self.player_friction = -0.15

        self.enemy_move_speed = 5
        self.enemy_anim_rate = 150
