from pygame import Color

class Settings():
    """Storage for all settings of Star Killer"""

    def __init__(self):
        """Initialize game settings"""
        # Screen Settings
        self.screen_width = 1500
        self.screen_heigth = 700
        self.bg_color = Color("#1B1B1B")