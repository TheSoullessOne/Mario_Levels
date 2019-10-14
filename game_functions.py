import pygame
import sys


def update_screen(screen, settings, mario):
    screen.fill(settings.bg_color)
    mario.blit_me(screen)

    pygame.display.flip()


def check_events(screen, settings, mario):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_key_down(event, screen, settings, mario)
        if event.type == pygame.KEYUP:
            check_key_up(event, screen, settings, mario)


def check_key_up(event, screen, settings, mario):
    if event.key == pygame.K_RIGHT:
        mario.moving_right = False
    elif event.key == pygame.K_LEFT:
        mario.moving_left = False


def check_key_down(event, screen, settings, mario):
    if event.key == pygame.K_RIGHT:
        mario.moving_right = True
    elif event.key == pygame.K_LEFT:
        mario.moving_left = True


