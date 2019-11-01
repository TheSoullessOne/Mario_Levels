import pygame
import sys


def update_screen(screen, settings, mario, current_level, sb, start_text):
    screen.blit(current_level.background.image, current_level.background.rect)
    current_level.blit_level()
    if settings.game_active:
        # allSprites.draw(screen)
        mario.slow_blit(screen)
        sb.show_score(screen, settings)
    else:
        start_text[0].draw(screen)
        start_text[1].draw(screen)

    current_level.blocks.update()
    current_level.items.update()

    pygame.display.flip()


def check_events(screen, settings, mario, background):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            settings.thread_timer.cancel()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_key_down(event, screen, settings, mario, background)
        if event.type == pygame.KEYUP:
            check_key_up(event, screen, settings, mario, background)


def check_key_up(event, screen, settings, mario, background):
    if event.key == pygame.K_RIGHT:
        mario.moving_right = False
    if event.key == pygame.K_LEFT:
        mario.moving_left = False
    if event.key == pygame.K_SPACE:
        pass


def check_key_down(event, screen, settings, mario, background):
    if event.key == pygame.K_SPACE and not mario.cant_move and settings.game_active:
        mario.mario_jumping()
        mario.starting_jump = mario.rect.bottom
    elif event.key == pygame.K_SPACE and not settings.game_active:
        settings.game_active = True
        settings.timer = 360
    if event.key == pygame.K_p and mario.mario_size < 2:     # TESTING PURPOSES. Increases mario size
        mario.mario_size += 1
        print(mario.mario_size)
        if mario.mario_size == 1:
            mario.changing_to_big = True
            mario.smol_to_big()
        mario.change_mario_size()
    if event.key == pygame.K_o and mario.mario_size > 0:    # TESTING PURPOSES. Decreases mario size
        mario.mario_size -= 1
        mario.changing_to_smol = True
        mario.big_to_smol()
    if event.key == pygame.K_i and mario.mario_size == 0:
        mario.mario_dead = True

# def check_mario_block_collisions(screen, settings, mario, blocks, pipes):
    was_moving_right = mario.moving_right
    was_moving_left = mario.moving_left
#     for block in blocks:
#         block_collision = pygame.sprite.collide_rect(mario, block)
#         if block_collision:
#             if mario.rect.right >= block.rect.left and was_moving_right:
#                 # mario.cannot_move_right = True
#                 mario.rect.right = block.rect.left
#             if mario.rect.left <= block.rect.right and was_moving_left:
#                 # mario.cannot_move_left = True
#                 mario.rect.left = block.rect.left
#             if mario.rect.bottom >= block.rect.top:
#                 mario.on_block = True
#                 mario.falling = False
#                 mario.rect.bottom = block.rect.top
#             elif not mario.on_block and mario.rect.top <= block.rect.bottom:
#                 mario.jumping = False
#                 mario.falling = True
# # <<<<<<< HEAD
# #
# #         if not block_collision:
# #             mario.on_block = False
# #
# #     for pipe in pipes:
# #         pipe_collision = pygame.sprite.collide_rect(mario, pipe)
# #         if pipe_collision:
# #             print('hit pipe')
# #             if mario.rect.right >= pipe.rect.left and was_moving_right:
# #                 mario.rect.right = pipe.rect.left
# #                 mario.cannot_move_right = True
# #                 print('going right')
# #             if mario.rect.left <= pipe.rect.right and was_moving_left:
# #                 mario.rect.left = pipe.rect.right
# #                 mario.cannot_move_left = True
# #                 print('going left')
# # =======
#                 collide_bottom = True
#             if mario.jumping and mario.rect.bottom - block.rect.top > 1:
#                 mario.jumping = True
#         if not block_collision:
#             #mario.falling = True
#             collide_top = collide_bottom = collide_left = collide_right = False
# # >>>>>>> cb2335c878c9a1e6874e2031c412ce6d25c73f5a


def update_all(screen, current_level, settings):
    for block in current_level.blocks:
        block.rect.left -= settings.PAN_SPEED
    for pipe in current_level.pipes:
        pipe.rect.left -= settings.PAN_SPEED
    for item in current_level.items:
        item.rect.left -= settings.PAN_SPEED

    current_level.background.rect.left -= settings.PAN_SPEED
    current_level.flag_pole.rect.left -= settings.PAN_SPEED
