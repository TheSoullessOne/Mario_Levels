from enemies import *
from items import *
from background import Background
from Levels.level import Level


class Level1_2(Level):
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.background = Background(screen, settings, 'Images/Backgrounds/1-2-bg.png')

    def initialize_blocks(self): pass