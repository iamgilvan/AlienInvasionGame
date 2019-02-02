import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ this class manage bullets"""
    def __init__(self, ai_settings, screen, ship):

        """" Create the bullet object in the spaceship position."""
        super(Bullet, self).__init__()
        self.screen = screen
        # Create the rectangle to the bullet at (0, 0) and , then, define the correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Store the bullet position as a decimal value
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """ Move the bullet to screen top."""

        # Update the decimal position of bullet
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the bullet on screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)