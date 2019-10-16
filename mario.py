import pygame
import game_functions as gf
from settings import Settings
from character import Character
from block import *

settings = Settings()


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Mario")

    mario = Character(screen, settings)
    block = Block(screen, settings)
    used_block = UsedBlock(screen, settings)

    while True:
        mario.update()
        gf.check_events(screen, settings, mario)
        gf.update_screen(screen, settings, mario, block, used_block)


run_game()