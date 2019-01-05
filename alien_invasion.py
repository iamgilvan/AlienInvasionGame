import sys
import pygame

from Settings.settings import Settings


def run_game():
    # Initialize the game and create an object to the screen
    pygame.init()
    ai_settings = Settings()
    # Screen dimension
    screen = pygame.display.set_mode((ai_settings.screen_wigth, ai_settings.screen_height))
    # screen title
    pygame.display.set_caption("Alien Invasion")

    # Define the background color on the rgb format
    pg_color = ai_settings.bg_color

    # Start the main loop of the game
    while True:
        # Watching the keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # reset the screen color
        screen.fill(pg_color)

        # keep visible the last screen
        pygame.display.flip()


run_game()