class Settings():
    """A class to store all the settings of Alien Invasion"""
    def __init__(self):
        """Initializing the settings"""
        # Screen settings
        self.screen_wigth  = 740
        self.screen_height = 600
        # Define the background color on the rgb format
        self.bg_color      = (230, 230, 230)
        # Settings to the spaceship
        self.ship_speed_factor = 1.5
        # Configurações dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60