import sys
import pygame

from bullets import Player_Laser


def check_keyDown(event, ai_settings, screen, player, projectiles):
    """Reactions to Key presses"""
    if event.key == pygame.K_UP:
        player.moving_up = True
    elif event.key == pygame.K_DOWN:
        player.moving_down = True
    elif event.key == pygame.K_SPACE:
        player.moving_right = True
        player.not_moving = False
    elif event.key == pygame.K_v:
        # Create a new laser and add it to the projectiles group
        if len(projectiles) < ai_settings.laser_limit:
            new_laser = Player_Laser(ai_settings, screen, player)
            projectiles.add(new_laser)


def check_keyUp(event, player):
    """Reactions to Key Releases"""
    if event.key == pygame.K_UP:
        player.moving_up = False
    elif event.key == pygame.K_DOWN:
        player.moving_down = False
    elif event.key == pygame.K_SPACE:
        player.moving_right = False
        player.not_moving = True


def check_player_events(ai_settings, screen, player, projectiles):
    """Keyboard and mouse watcher. Will Repsond to inputs"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keyDown(event, ai_settings, screen, player, projectiles)
        elif event.type == pygame.KEYUP:
            check_keyUp(event, player)  


def update_projectiles(projectiles):
    """Update position of projectiles from player"""
    # Update projectile positions
    projectiles.update()

     # Remove off screen projectiles from memory
    for laser in projectiles.copy():
        if laser.rect.right >= 1500:
            projectiles.remove(laser)
        print(len(projectiles))


def update_screen(conductor_settings, screen, star_killer, projectiles):
    """Redraw the screen during each pass"""
    screen.fill(conductor_settings.bg_color)
    # Redraw all projectiles behind enemy ships
    for laser in projectiles.sprites():
        laser.draw_laser()
    star_killer.blitspri(screen, (star_killer.index % star_killer.totalCellCount), star_killer.rect)

    # Make the most recently drawn screen visible
    pygame.display.flip()
