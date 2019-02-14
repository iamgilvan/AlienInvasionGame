import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ Uma classe que representa um único alienígena da frota."""

    def __init__(self, ai_settings, screen):
        """ Initialize the alien and set your initial position """
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        # Load the alien image and set your rectangle attribute
        self.image = pygame.image.load('Images/alien.bmp')
        self.rect = self.image.get_rect()
        # Initialize each new alien near the top left in screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the correct position of alien
        self.x = float(self.rect.x)

    def blitme(self):
        """ Draws the alien in your current position"""
        self.screen.blit(self.image, self.rect)