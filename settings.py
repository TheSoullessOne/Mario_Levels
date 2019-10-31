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

        self.max_jump_height = 250
        self.init_jmp_speed = 4
        self.max_jmp_speed = 1
        self.move_speed = 10.0
        self.init_gravity = float(0.03)
        self.max_gravity = 3

        self.enemy_move_speed = 5
        self.enemy_anim_rate = 150
        self.score = 0
        self.lives = 3
        self.timer = 360
        self.thread_timer = Timer(1, self.update_time)
        self.thread_timer.start()

    def update_time(self):
        print(time.ctime())
        self.timer -= 1
        self.thread_timer = Timer(1, self.update_time)
        self.thread_timer.start()
