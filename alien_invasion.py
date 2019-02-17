import pygame
from pygame.sprite import Group

from Settings.settings import Settings
from Ship.ship import Ship
from Game_Functions import  game_functions as gf
from Stats.game_stats import GameStats


def run_game():
    # Initialize the game and create an object to the screen
    pygame.init()
    ai_settings = Settings()
    # Screen dimension
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # screen title
    pygame.display.set_caption("Alien Invasion")

    # Creates an instance to store game statistics
    stats = GameStats(ai_settings)

    # creating a spaceship
    ship = Ship(ai_settings, screen)
    # Create a group in which will be stored the bullets
    bullets = Group()
    aliens = Group()

    # Creating the aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop of the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()