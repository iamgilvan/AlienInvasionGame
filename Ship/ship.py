import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """ Initialize and define the initial position to spaceship"""
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the spaceship image and get your react
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new spaceship in screen bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Store a decimal value to the center the spaceship
        self.center = float(self.rect.centerx)
        # flag to move
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the spaceship position"""
        # Update the spaceship center position
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Updated the object
        self.rect.centerx = self.center

    def blitme(self):
        """ Draws the spaceship in your actual position"""
        self.screen.blit(self.image, self.rect)

