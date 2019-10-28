import pygame
import sys


def update_screen(screen, settings, mario, block, used_block, background):
    # screen.fill(settings.bg_color)
    screen.blit(background.image, background.rect)
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
        mario.falling = False
        mario.jumping = True
        mario.starting_jump = mario.rect.bottom
    if event.key == pygame.K_p and mario.mario_size < 3:     # TESTING PURPOSES. Increases mario size
        mario.mario_size += 1
        mario.change_mario_size()
    if event.key == pygame.K_o and mario.mario_size > 0:    # TESTING PURPOSES. Decreases mario size
        mario.mario_size -= 1
        mario.change_mario_size()


def check_mario_block_collisions(screen, settings, mario, blocks):
    was_moving_right = mario.moving_right
    was_moving_left = mario.moving_left
    for block in blocks:
        collision = pygame.sprite.collide_rect(mario, block)
        # print(collision)
        if collision:
            if not mario.on_block and mario.rect.right >= block.rect.left and was_moving_right:
                print('hit left side of block')
                mario.cannot_move_right = True
                mario.on_block = False
            elif not mario.on_block and mario.rect.left <= block.rect.right and was_moving_left:
                print('hit right side of block')
                mario.cannot_move_left = True
                mario.on_block = False
            elif not mario.jumping and mario.falling and not mario.on_block and mario.rect.bottom >= block.rect.top:  # \
                # and (mario.rect.left <= block.rect.right or mario.rect.right >= block.rect.left):
                print("on top of block")
                print(block.rect.top)
                print(mario.rect.bottom)
                mario.on_block = True
                mario.falling = False
                mario.rect.bottom = block.rect.top
            elif mario.jumping and not mario.on_block and mario.rect.top <= block.rect.bottom:
                print('hit head')
                mario.on_block = False
                mario.jumping = False
                mario.falling = True

        # if collision == 0:
            # mario.falling = True
            # if mario.on_block and mario.jumping:
            #     print('trying to jump')
            #     # mario.on_block = False
            #     mario.jumping = True
        # if not collision and mario.y_bot <= mario.settings.screen_height:
        #     mario.falling = True
