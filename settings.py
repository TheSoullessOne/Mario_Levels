import threading

from block import *
import time
from threading import Timer


class Settings:
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 500
        self.bg_color = (107, 140, 255)
        self.game_active = False
        self.pause = True

        self.MOVE_SPEED = float(0.9)
        self.PAN_SPEED = 4
        self.PLAYER_FRICTION = -0.2
        self.PLAYER_GRAVITY = 0.5

        self.enemy_move_speed = 1
        self.enemy_anim_rate = 150
        self.score = 0
        self.coin_count = 0
        self.lives = 3
        self.timer = 360
        self.thread_timer = Timer(1, self.update_time)
        self.thread_timer.start()
        self.world_level = "1-1"

    def update_time(self):
        print(time.ctime())
        self.timer -= 1
        self.thread_timer = Timer(1, self.update_time)
        self.thread_timer.start()

    def is_paused(self):
        return self.pause