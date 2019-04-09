import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """A class to represent a single enemy in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the enemy and set its starting postion."""
        super(Enemy, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and set a square 64 pixle rectangle
        self.sheet = pygame.image.load("images/enemy.ship.png").convert_alpha()
        self.rect = pygame.Rect(0,0, 64, 64)
        
        # Assign variables for the spritesheet list builder
        self.cols = 1
        self.rows = 8
        self.totalCellCount = 8
        
        self.sheetrect = self.sheet.get_rect()
        w = self.cellWidth = self.sheetrect.width / 1
        h = self.cellHeight = self.sheetrect.height / 8
        self.screen_rect = screen.get_rect()
        
        # Spritesheet list builder. puts a grid on the sprite sheet. Using the deifned index
        # for each cell, it allows a callable range of images to be blitted later
        self.cells = list([
            (index * w, int(index) * h, w, h) for index in range(self.totalCellCount)
            ])

        self.index = 0


        # Start each new enemy near right of the screen
        self.rect.y = self.screen_rect.centery
        self.rect.x = self.screen_rect.centerx + (400)

        #Store the enemy positions
        self.y = float(self.rect.y)
        self.X = float(self.rect.x)

    def blitspri(self, surface, cellIndex, enemy):
        """Use index to draw the ship sprites at its current location."""
        surface.blit(self.sheet, enemy, self.cells[cellIndex])