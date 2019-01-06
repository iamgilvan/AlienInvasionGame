import sys

import pygame


def check_Events():
    # Watching the keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    # reset the screen color
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # keep visible the last screen
    pygame.display.flip()