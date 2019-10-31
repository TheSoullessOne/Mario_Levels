from block import *


class Settings:
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 500
        self.bg_color = (156, 219, 255)

        self.MOVE_SPEED = float(0.9)
        self.PLAYER_FRICTION = -0.15
        self.PLAYER_GRAVITY = 0.5

        self.enemy_move_speed = 5
        self.enemy_anim_rate = 150
