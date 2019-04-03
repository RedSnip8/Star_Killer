import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, player_settings, screen, filename, cols = 8, rows = 8):
            """Initialize the ship and it's starting position"""
            self.screen = screen
            self.settings = player_settings

            # Load the ship image and set a square 64 pixle rectangle
            self.sheet = pygame.image.load(filename).convert_alpha()
            self.rect = pygame.Rect(0,0, 64, 64)
            
            # Assign variables for the spritesheet list builder
            self.cols = cols
            self.rows = rows
            self.totalCellCount = cols * rows
            
            self.sheetrect = self.sheet.get_rect()
            w = self.cellWidth = self.sheetrect.width / cols
            h = self.cellHeight = self.sheetrect.height / rows
            self.screen_rect = screen.get_rect()
            
            # Spritesheet list builder. puts a grid on the sprite sheet. Using the deifned index
            # for each cell, it allows a callable range of images to be blitted later
            self.cells = list([
                (index % cols * w, int(index / cols) * h, w, h) for index in range(self.totalCellCount)
                ])

            self.index = 0

            # Start the new ship at the left center of the screen
            self.rect.centery = self.screen_rect.centery
            self.rect.left = self.screen_rect.centerx - (200)
            # Store a deciaml value for the player's center
            self.center = float(self.rect.centery)
            self.centerX = float(self.rect.left)

            # Movement Flag
            self.moving_up = False
            self.moving_down = False
            self.moving_right = False
            self.not_moving = True


    def blitspri(self, surface, cellIndex, player):
        """Use index to draw the ship sprites at its current location."""
        surface.blit(self.sheet, player, self.cells[cellIndex])

    def update(self):
        """Update the ship's postion based on the movement flag"""
        # Update the player's center value, not the rectangle
        if self.moving_up and self.rect.top > 0: 
            self.center -= self.settings.ship_speed_factor
            self.index = 16
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.settings.ship_speed_factor
            self.index = 32

        if self.moving_right and self.rect.right < 500 :
            self.centerX += self.settings.ship_speed_factor
            self.settings.ship_speed_factor = 2
            self.index = 8

        if self.not_moving and self.rect.left > 0:
            self.centerX -= 1
            self.settings.ship_speed_factor = 1.5
            self.index = 0


        self.rect.centery = self.center
        self.rect.left = self.centerX