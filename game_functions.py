import pygame
import sys


def update_screen(screen, settings, mario, current_level):
    screen.blit(current_level.background.image, current_level.background.rect)
    current_level.blit_level()
    mario.slow_blit(screen)

    #print(mario.centerx, mario.centery)

    pygame.display.flip()


def check_events(screen, settings, mario, background):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_key_down(event, screen, settings, mario, background)
        if event.type == pygame.KEYUP:
            check_key_up(event, screen, settings, mario, background)


def check_key_up(event, screen, settings, mario, background):
    if event.key == pygame.K_RIGHT:
        # if mario.rect.right < settings.screen_width / 2:
        #     mario.moving_right = True
        # else:
        mario.moving_right = False
        #     background.rect.left -= settings.move_speed
    if event.key == pygame.K_LEFT:
        mario.moving_left = False
    if event.key == pygame.K_SPACE:
        mario.jumping = False
        mario.falling = True


def check_key_down(event, screen, settings, mario, background):
    if event.key == pygame.K_RIGHT:
        # if mario.rect.right < settings.screen_width / 2:
        mario.moving_right = True
        # else:
        #     mario.moving_right = False
        #     background.rect.left -= settings.move_speed
    if event.key == pygame.K_LEFT:
        mario.moving_left = True
    if event.key == pygame.K_SPACE and not mario.falling:
        mario.falling = False
        mario.jumping = True
        mario.starting_jump = mario.rect.bottom
    if event.key == pygame.K_p and mario.mario_size < 2:     # TESTING PURPOSES. Increases mario size
        mario.mario_size += 1
        mario.change_mario_size()
    if event.key == pygame.K_o and mario.mario_size > 0:    # TESTING PURPOSES. Decreases mario size
        mario.mario_size -= 1
        mario.change_mario_size()


def check_mario_block_collisions(screen, settings, mario, blocks):
    was_moving_right = mario.moving_right
    was_moving_left = mario.moving_left
    collide_left = collide_right = collide_bottom = collide_top = False
    for block in blocks:
        collision = pygame.sprite.collide_rect(mario, block)
        # print(collision)
        if collision:
            mario.has_collided = True
            if not collide_left and not collide_bottom and not collide_top and \
                    mario.jumping and not mario.on_block and mario.rect.right >= block.rect.left and was_moving_right:
                print('hit left side of block')
                mario.cannot_move_right = True
                mario.on_block = False
                collide_right = True
            elif not collide_right and not collide_bottom and not collide_top and\
                    mario.jumping and not mario.on_block and mario.rect.left <= block.rect.right and was_moving_left:
                print('hit right side of block')
                mario.cannot_move_left = True
                mario.on_block = False
                collide_left = True
            elif not collide_right and not collide_left and not collide_bottom and\
                    not mario.jumping and mario.falling and not mario.on_block and mario.rect.bottom - block.rect.top == 1:  # \
                print("on top of block")
                print(block.rect.top)
                print(mario.rect.bottom)
                mario.on_block = True
                mario.falling = False
                mario.rect.bottom = block.rect.top
                collide_top = True
            elif not collide_left and not collide_right and not collide_top and\
                    mario.jumping and not mario.on_block and mario.rect.top - block.rect.bottom == 1:
                print('hit head')
                mario.on_block = False
                mario.jumping = False
                mario.falling = True
                collide_bottom = True

        # print(str(collision) + ' ' + str(mario.has_collided) + ' ' + str(mario.on_block) + ' ' + str(mario.jumping))
        if not collision and mario.has_collided and not mario.on_block and not mario.jumping:
            collide_top = collide_bottom = collide_left = collide_right = False
            # if mario.has_collided and not mario.on_block and not mario.jumping:
            mario.falling = True
            mario.has_collided = False


def update_all(screen, blocks, mobs, background):
    for block in blocks:
        block.rect.left -= 2.0
    background.rect.left -= 2.0
