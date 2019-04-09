#!/usr/bin/env python3

import sys, pygame

from pygame.sprite import Group
import game_functions as gmf

from settings import Settings
from ship import Ship
from enemies import Enemy


def run_game():
    # Initalize pygame, defined settings, and the screen
    pygame.init
    conductor_settings = Settings()
    screen = pygame.display.set_mode(
        (conductor_settings.screen_width, conductor_settings.screen_heigth)
    ) 
    pygame.display.set_caption("Star Killer- Redsnip8")

    # Make PC Ship
    star_killer = Ship(conductor_settings, screen, "images/star-killer-ani.png", 8, 8)
    # Make projectile storage
    projectiles = Group()

    # Make Enemy
    enemy = Enemy(conductor_settings, screen)

    # Game loop
    while True:
        gmf.check_player_events(conductor_settings, screen, star_killer, projectiles)
        star_killer.update()
        gmf.update_projectiles(projectiles)
        gmf.update_screen(conductor_settings, screen, star_killer, enemy, projectiles)

run_game()