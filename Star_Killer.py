#!/usr/bin/env python3

import sys
import pygame

from settings import Settings
from ship import Ship


def run_game():
    # Initalize pygame, defined settings, and the screen
    pygame.init
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_heigth)
    ) 
    pygame.display.set_caption("Star Killer")

    # Make PC Ship
    star_killer = Ship(screen)

    # Game loop
    while True:

        #Keyboard and mouse watcher
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        star_killer.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()