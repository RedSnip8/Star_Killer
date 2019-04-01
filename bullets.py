import pygame
from pygame.sprite import Sprite

class Player_Laser(Sprite):

    def __init__(self, ai_settings, screen, player):
        """Creates a the base level laser weapon for the player"""
        # Sets starting position at the fron of the player ship
        super().__init__()
        self.screen = screen

        # Creates a rectangle for the laser and sets the correct position
        self.rect = pygame.Rect(0,0, ai_settings.laser_width, 
            ai_settings.laser_height)
        self.rect.centery = player.rect.centery
        self.rect.left = player.rect.right
        
        # Store the laser's positiona as as decimal value
        self.x = float(self.rect.x)

        self.color = ai_settings.laser_color
        self.speed_factor = ai_settings.laser_speed_factor

    
    def update(self):
        """Move the laser across the screen"""
        # Update the decimal postion of the bullet
        self.x += self.speed_factor
        # Update the position
        self.rect.x = self.x

    
    def draw_laser(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
