import sys
import pygame
import game_functions as gf
from settings import Settings
from character import Character
from block import *
from background import Background
from Levels.level1_1 import Level1_1
from Levels.level1_2 import Level1_2
from Levels.level1_3 import Level1_3
from pygame.sprite import Group
from scoreboard import Scoreboard
from textbox import TextBox

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
    pipes = current_level.pipes
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

    while True:
        gf.check_events(screen, settings, mario, current_level.background)
        gf.update_screen(screen, settings, mario, current_level, sb)

        if settings.game_active:
            mario.update(screen, current_level)
            gf.check_mario_block_collisions(screen, settings, mario, blocks, pipes)
        else:
            starting_text.draw(screen)
            starting_text_2.draw(screen)
            pygame.display.flip()


run_game()
