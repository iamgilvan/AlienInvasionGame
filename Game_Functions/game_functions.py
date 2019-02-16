import sys

import pygame

from Alien.alien import Alien
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


def fire_bulltes(ai_settings, screen, ship, bullets):
    """ Shoot a new bullet if not is max number allowed."""
    # Create a new bullet and add him to bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Response a press key"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bulltes(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def update_screen(ai_settings, screen, ship, aliens, bullets):
    # reset the screen color
    screen.fill(ai_settings.bg_color)
    # redesign the all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
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


def create_fleet(ai_settings, screen, ship,  aliens):
    """ Creating the aliens."""
    # Create an alien and calc the number of aliens in one line
    # The spacing between the aliens is equal to the width of an alien
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the first aliens line
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_rows(ai_settings, ship_height, alien_height):
        """ Set the line number available to alien on screen."""
        available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = int(available_space_y / (2 * alien_height))
        return number_rows


def get_number_aliens_x(ai_settings, alien_width):
    """ Set the number line of aliens available in one line."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # Create an alien and set yours prosition on screen
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.rect.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def change_fleet_direction(ai_settings, aliens):
    """It makes the whole fleet down and changes its direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens):
    """ Checks if the fleet is on one of the edges and then updates the positions of all the aliens in the fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

def check_fleet_edges(ai_settings, aliens):
    """Responds appropriately if any alien has reached a border."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break