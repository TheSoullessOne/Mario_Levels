import sys
import pygame
import game_functions as gf
from settings import Settings
from character import Character
from character import Platform
from block import *
from background import Background
from Levels.level1_1 import Level1_1
from Levels.level1_2 import Level1_2
from Levels.level1_3 import Level1_3
from pygame.sprite import Group

settings = Settings()


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Mario")

    current_level = Level1_1(screen, settings)
    # current_level = Level1_2(screen, settinggit pus)
    # current_level = Level1_3(screen, settings)

    # background = Background(screen, settings)
    mario = Character(screen, settings)

    blocks = current_level.blocks
    mobs = Group()

    allSprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    p1 = Platform(50, settings.screen_height - 40, 300, 20)
    allSprites.add(p1)
    platforms.add(p1)
    p2 = Platform(50, settings.screen_height - 200, 100, 30)
    allSprites.add(p2)
    platforms.add(p2)

    while True:
        mario.update(screen, current_level, mario, platforms)
        # gf.update_all(screen, settings, mario, blocks, mobs, backgorund)
        gf.check_events(screen, settings, mario, current_level.background)
        gf.update_screen(screen, settings, mario, current_level, allSprites)
        gf.check_mario_block_collisions(screen, settings, mario, blocks)


run_game()
