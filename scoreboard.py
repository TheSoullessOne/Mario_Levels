import pygame.font
import time
# from pygame.sprite import Group


class Scoreboard:
    """A Class to report scoring information"""
    def __init__(self, settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        #  Font for scoring information
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #  Prepare the initial score image
        self.prep_score()
        self.prep_timer()
        self.prep_lives()

    def prep_score(self):
        """Turn the score into a rendered image"""
        score_str = "{:,}".format(self.settings.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #  Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.settings.screen_width / 2
        self.score_rect.top = self.screen_rect.top

    def show_score(self, screen):
        screen.blit(self.score_image, self.score_rect)
        timer_str = "{:,}".format(self.settings.timer)
        self.timer_image = self.font.render(timer_str, True, self.text_color, self.settings.bg_color)
        screen.blit(self.timer_image, self.timer_rect)
        screen.blit(self.mario_image, self.image_rect)
        screen.blit(self.x_image, self.x_rect)
        lives_str = "{:,}".format(self.settings.lives)
        self.lives_image = self.font.render(lives_str, True, self.text_color, self.settings.bg_color)
        screen.blit(self.lives_image, self.lives_rect)

    def prep_timer(self):
        timer_str = "{:,}".format(self.settings.timer)
        self.timer_image = self.font.render(timer_str, True, self.text_color, self.settings.bg_color)

        #  Display the score at the top right of the screen
        self.timer_rect = self.timer_image.get_rect()
        self.timer_rect.left = self.screen_rect.left
        self.timer_rect.top = self.screen_rect.top

    def prep_lives(self):
        """Turn level into a rendered image"""
        self.mario_image = pygame.image.load("Images/Mario-Movement/smol/smol-mario-look-right.png")

        #  Position the level below the score
        self.image_rect = self.mario_image.get_rect()
        self.image_rect.right = self.screen_rect.right - 50
        self.image_rect.top = self.screen_rect.top

        lives_str = " {:,}".format(self.settings.lives)
        self.lives_image = self.font.render(lives_str, True, self.text_color, self.settings.bg_color)
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.right = self.screen_rect.right
        self.lives_rect.top = self.screen_rect.top + 5

        x_str = "x"
        self.x_image = self.font.render(x_str, True, self.text_color, self.settings.bg_color)
        self.x_rect = self.x_image.get_rect()
        self.x_rect.right = self.lives_rect.left
        self.x_rect.top = self.screen_rect.top + 5



