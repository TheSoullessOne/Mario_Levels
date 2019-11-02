import pygame.font
import time
from textbox import TextBox


class Scoreboard:
    """A Class to report scoring information"""
    def __init__(self, settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        #  Font for scoring information
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)

        #  Prepare the initial score image
        self.prep_score()
        self.prep_timer()
        self.prep_lives()
        self.prep_world()
        self.prep_coins()

    def prep_score(self):
        """Turn the score into a rendered image"""
        self.score_text = TextBox(self.settings, self.screen)
        self.score_text.update_text("SCORE")
        self.score_text.text_rect.top = self.screen_rect.top + 5
        self.score_text.text_rect.left = self.screen_rect.left + 50
        self.score_str = "{:,}".format(self.settings.score)
        self.score_image = self.font.render(self.score_str, True, self.text_color, self.settings.bg_color)

        #  Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.score_text.text_rect.centerx
        self.score_rect.top = self.score_text.text_rect.bottom

    def show_score(self, screen, settings):
        self.score_text.draw(screen)
        score_str = "{:,}".format(self.settings.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        screen.blit(self.score_image, self.score_rect)

        self.timer_text.draw(screen)
        timer_str = "{:,}".format(self.settings.timer)
        self.timer_image = self.font.render(timer_str, True, self.text_color, self.settings.bg_color)
        screen.blit(self.timer_image, self.timer_rect)

        self.lives_text.draw(screen)
        lives_str = "{:,}".format(self.settings.lives)
        self.lives_image = self.font.render(lives_str, True, self.text_color, self.settings.bg_color)
        screen.blit(self.lives_image, self.lives_rect)

        self.world_text.draw(screen)
        # world_str = " {:,}".format(self.settings.world_level)
        self.world_image = self.font.render(self.settings.world_level, True, self.text_color, self.settings.bg_color)
        screen.blit(self.world_image, self.world_rect)

        self.coin_text.draw(screen)
        coin_str = " {:,}".format(settings.coin_count)
        self.coin_image = self.font.render(coin_str, True, self.text_color, self.settings.bg_color)
        screen.blit(self.coin_image, self.coin_rect)

    def prep_timer(self):
        timer_str = "{:,}".format(self.settings.timer)
        self.timer_image = self.font.render(timer_str, True, self.text_color, self.settings.bg_color)

        self.timer_text = TextBox(self.settings, self.screen)
        self.timer_text.update_text("TIMER")
        self.timer_text.text_rect.centerx = self.score_text.text_rect.centerx + 175
        self.timer_text.text_rect.top = self.screen_rect.top + 5

        #  Display the score at the top right of the screen
        self.timer_rect = self.timer_image.get_rect()
        self.timer_rect.centerx = self.score_text.text_rect.centerx + 175
        self.timer_rect.top = self.timer_text.text_rect.bottom

    def prep_lives(self):
        """Turn level into a rendered image"""
        self.lives_text = TextBox(self.settings, self.screen)
        self.lives_text.update_text("LIVES")
        self.lives_text.text_rect.right = self.settings.screen_width - 50
        self.lives_text.text_rect.top = self.screen_rect.top + 5

        lives_str = " {:,}".format(self.settings.lives)
        self.lives_image = self.font.render(lives_str, True, self.text_color, self.settings.bg_color)
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.centerx = self.lives_text.text_rect.centerx
        self.lives_rect.top = self.lives_text.text_rect.bottom

    def prep_world(self):
        self.world_text = TextBox(self.settings, self.screen)
        self.world_text.update_text("WORLD")
        self.world_text.text_rect.centerx = self.settings.screen_width / 2
        self.world_text.text_rect.top = self.screen_rect.top + 5

        # world_str = " {:,}".format(self.settings.world_level)
        self.world_image = self.font.render(self.settings.world_level, True, self.text_color, self.settings.bg_color)
        self.world_rect = self.world_image.get_rect()
        self.world_rect.centerx = self.world_text.text_rect.centerx
        self.world_rect.top = self.world_text.text_rect.bottom

    def prep_coins(self):
        self.coin_text = TextBox(self.settings, self.screen)
        self.coin_text.update_text("COINS")
        self.coin_text.text_rect.centerx = self.lives_rect.centerx - 175
        self.coin_text.text_rect.top = self.screen_rect.top + 5

        coin_str = " {:,}".format(self.settings.coin_count)
        self.coin_image = self.font.render(coin_str, True, self.text_color, self.settings.bg_color)
        self.coin_rect = self.coin_image.get_rect()
        self.coin_rect.centerx = self.coin_text.text_rect.centerx
        self.coin_rect.top = self.coin_text.text_rect.bottom



