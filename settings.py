from pygame import Color

class Settings():
    """Storage for all settings of Star Killer"""

    def __init__(self):
        """Initialize game settings"""
        # Screen Settings
        self.screen_width = 1500
        self.screen_heigth = 700
        self.bg_color = Color("#1B1B1B")

        # Ship Settings
        self.ship_speed_factor = 1.5

        # Laser Settings
        self.laser_speed_factor = 7
        self.laser_width = 20
        self.laser_height = 3
        self.laser_color = Color("#842bd7")
        self.laser_limit = 6