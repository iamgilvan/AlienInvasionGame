import sys

import pygame

from Ship.bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    # Watching the keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Response a press key"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add him to bullets group
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, bullets):
    # reset the screen color
    screen.fill(ai_settings.bg_color)
    # redesign the all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # keep visible the last screen
    pygame.display.flip()


def update_bullets(bullets):
    """ Update the bullets position and remove old bullets."""
    # Update the bullets position
    bullets.update()
    # cleaning extra bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)