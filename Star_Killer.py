#!/usr/bin/env python3

import sys
import pygame

from pygame.sprite import Group
import game_functions as gmf

from settings import Settings
from ship import Ship


def run_game():
    # Initalize pygame, defined settings, and the screen
    pygame.init
    conductor_settings = Settings()
    screen = pygame.display.set_mode(
        (conductor_settings.screen_width, conductor_settings.screen_heigth)
    ) 
    pygame.display.set_caption("Star Killer")

    # Make PC Ship
    star_killer = Ship(conductor_settings, screen)
    # Make projectile storage
    projectiles = Group()


    # Game loop
    while True:
            gmf.check_player_events(conductor_settings, screen, star_killer, projectiles)
            star_killer.update()
            projectiles.update()
            gmf.update_screen(conductor_settings, screen, star_killer, projectiles)

run_game()