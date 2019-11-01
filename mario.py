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
from scoreboard import Scoreboard
from textbox import TextBox
from pygame import time


def run_game():
    settings = Settings()

    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Mario")
    clock = pygame.time.Clock()

    current_level = Level1_1(screen, settings)
    # current_level = Level1_2(screen, settinggit pus)
    # current_level = Level1_3(screen, settings)

    # background = Background(screen, settings)
    mario = Character(screen, settings)

    blocks = current_level.blocks
    blocks.add(current_level.floor_blocks)
    pipes = current_level.pipes
    items = current_level.items

    #  enemies = current_level.enemies

    sb = Scoreboard(settings, screen)

    starting_text = TextBox(settings, screen)
    starting_text.update_text("Welcome to Mario!")
    starting_text.text_rect.centery = screen.get_rect().centery
    starting_text.text_rect.centerx = screen.get_rect().centerx
    starting_text.update_font('arial', 80)

    starting_text_2 = TextBox(settings, screen)
    starting_text_2.update_text("Press Space to begin!")
    starting_text_2.text_rect.top = starting_text.text_rect.bottom
    starting_text_2.text_rect.centerx = screen.get_rect().centerx
    starting_text_2.update_font('arial', 80)

    start_text = [starting_text, starting_text_2]

    # allSprites = pygame.sprite.Group()
    # platforms = pygame.sprite.Group()
    # p1 = Platform(50, settings.screen_height - 40, 300, 20)
    # allSprites.add(p1)
    # platforms.add(p1)
    # p2 = Platform(50, settings.screen_height - 200, 100, 30)
    # allSprites.add(p2)
    # platforms.add(p2)

    while True:
        clock.tick(60)
        mario.update(settings, screen, current_level, mario, blocks, pipes, items)
        gf.update_screen(screen, settings, mario, current_level, sb, start_text)

        gf.check_events(screen, settings, mario, current_level.background)


run_game()
