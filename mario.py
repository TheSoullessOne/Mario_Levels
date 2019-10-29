import pygame
import game_functions as gf
from settings import Settings
from character import Character
from block import *
from background import Background
from level1_1 import Level1_1
from pygame.sprite import Group

settings = Settings()


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Mario")

    current_level = Level1_1(screen, settings)

    # background = Background(screen, settings)
    mario = Character(screen, settings)

    blocks = current_level.blocks
    mobs = Group()

    while True:
        mario.update(screen, blocks, mobs, current_level.background)
        # gf.update_all(screen, settings, mario, blocks, mobs, backgorund)
        gf.check_events(screen, settings, mario, current_level.background)
        gf.update_screen(screen, settings, mario, current_level)
        gf.check_mario_block_collisions(screen, settings, mario, blocks)


run_game()
