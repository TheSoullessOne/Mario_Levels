import pygame
import game_functions as gf
from settings import Settings
from character import Character
from block import *
from background import Background
from pygame.sprite import Group

settings = Settings()


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Mario")

    background = Background(screen, settings)
    mario = Character(screen, settings)
    block = Block(screen, settings)
    used_block = UsedBlock(screen, settings)
    blocks = Group()
    blocks.add(block)
    blocks.add(used_block)

    while True:
        mario.update(background)
        gf.check_events(screen, settings, mario, background)
        gf.update_screen(screen, settings, mario, block, used_block, background)
        gf.check_mario_block_collisions(screen, settings, mario, blocks)


run_game()
