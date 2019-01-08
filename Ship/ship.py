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
        # flag to move
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the spaceship position"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """ Draws the spaceship in your actual position"""
        self.screen.blit(self.image, self.rect)

