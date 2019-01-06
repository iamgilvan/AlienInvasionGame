import pygame


class Ship():

    def __init__(self, screen):
        """ Initialize and define the initial position to spaceship"""
        self.screen = screen
        """ Load the spaceship image and get your react"""
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new spaceship  in screen bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """ Draws the spaceship in your actual position"""
        self.screen.blit(self.image, self.rect)

