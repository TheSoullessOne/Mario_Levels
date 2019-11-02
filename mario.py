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

    start_text = []

    start_image = pygame.image.load("Images/Misc/Starting-Screen.png")
    start_image_rect = start_image.get_rect()
    start_image_rect.top = screen.get_rect().top + 75
    start_image_rect.left = screen.get_rect().left + 75

    start_image_2 = pygame.image.load("Images/Misc/Starting-Screen-2.png")
    start_image_2_rect = start_image_2.get_rect()
    start_image_2_rect.top = start_image_rect.bottom
    start_image_2_rect.centerx = start_image_rect.centerx

    start_image_3 = pygame.image.load("Images/Misc/Starting-Screen-3.png")
    start_image_3_rect = start_image_3.get_rect()
    start_image_3_rect.top = start_image_2_rect.bottom
    start_image_3_rect.centerx = start_image_2_rect.centerx

    start_text_4 = TextBox(settings, screen)
    start_text_4.update_font("Font/super_mario_bros.ttf", 18)
    start_text_4.update_text("Press space to start!")
    start_text_4.text_rect.left = settings.screen_width / 2
    start_text_4.text_rect.centery = settings.screen_height / 2

    start_text.append([start_image, start_image_rect])
    start_text.append([start_image_2, start_image_2_rect])
    start_text.append([start_image_3, start_image_3_rect])
    start_text.append(start_text_4)

    while True:
        clock.tick(60)
        mario.update(settings, screen, current_level, mario, blocks, pipes, items, current_level.enemies)
        gf.update_screen(screen, settings, mario, current_level, sb, start_text)

        gf.check_events(screen, settings, mario, current_level.background)


run_game()
