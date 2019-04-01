import pygame

class Ship():
    def __init__(self, player_settings, screen):
        """Initialize the ship and it's starting position"""
        self.screen = screen
        self.settings = player_settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/space_ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

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

    def update(self):
        """Update the ship's postion based on the movement flag"""
        # Update the player's center value, not the rectangle
        if self.moving_up and self.rect.top > 0: 
            self.center -= self.settings.ship_speed_factor
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.settings.ship_speed_factor

        if self.moving_right and self.rect.right < 500 :
            self.centerX += self.settings.ship_speed_factor
            self.settings.ship_speed_factor = 2

        if self.not_moving and self.rect.left > 0:
            self.centerX -= 1
            self.settings.ship_speed_factor = 1.5


        self.rect.centery = self.center
        self.rect.left = self.centerX

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)