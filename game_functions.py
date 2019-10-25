import pygame
import sys


def update_screen(screen, settings, mario, block, used_block):
    screen.fill(settings.bg_color)
    mario.slow_blit(screen)

    # TESTING BLOCKS
    block.rect.center = screen.get_rect().center
    block.rect.centery += 100
    block.blit_me(screen)

    used_block.rect.center = screen.get_rect().center
    used_block.rect.centery += 100
    used_block.rect.left = block.rect.right
    used_block.blit_me(screen)

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
    if event.key == pygame.K_LEFT:
        mario.moving_left = False
    if event.key == pygame.K_SPACE:
        mario.jumping = False
        mario.falling = True


def check_key_down(event, screen, settings, mario):
    if event.key == pygame.K_RIGHT:
        mario.moving_right = True
    if event.key == pygame.K_LEFT:
        mario.moving_left = True
    if event.key == pygame.K_SPACE:
        mario.jumping = True
        mario.starting_jump = mario.rect.bottom


def check_mario_block_collisions(screen, settings, mario, blocks):
    was_moving_right = mario.moving_right
    was_moving_left = mario.moving_left
    for block in blocks:
        collision = pygame.sprite.collide_rect(mario, block)
        if collision:
            if mario.rect.right >= block.rect.left and was_moving_right:
                mario.cannot_move_right = True
            elif mario.rect.left <= block.rect.right and was_moving_left:
                mario.cannot_move_left = True
            elif mario.rect.top <= block.rect.bottom:
                mario.jumping = False
                mario.falling = True
            elif mario.rect.bottom >= block.rect.top:
                print("collide")
                # mario.on_block = True
                mario.rect.bottom = block.rect.top
