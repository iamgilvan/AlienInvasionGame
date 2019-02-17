class Settings():
    """A class to store all the settings of Alien Invasion"""
    def __init__(self):
        """Initializing the settings"""
        # Screen settings
        self.screen_width = 740
        self.screen_height = 600
        # Define the background color on the rgb format
        self.bg_color = (230, 230, 230)
        # Settings to the spaceship
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        # Settings the bullets
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5
        # Settings the aliens
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet direction equal 1 represents the right and -1 represents the left
        self.fleet_direction = 1