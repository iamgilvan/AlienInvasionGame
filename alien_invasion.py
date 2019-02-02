import pygame
from pygame.sprite import Group

from Settings.settings import Settings
from Ship.ship import Ship
from Game_Functions import  game_functions as gf


def run_game():
    # Initialize the game and create an object to the screen
    pygame.init()
    ai_settings = Settings()
    # Screen dimension
    screen = pygame.display.set_mode((ai_settings.screen_wigth, ai_settings.screen_height))
    # screen title
    pygame.display.set_caption("Alien Invasion")
    # creating a spaceship
    ship = Ship(ai_settings, screen)
    # Create a group in which will be stored the bullets
    bullets = Group()

    # Start the main loop of the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()