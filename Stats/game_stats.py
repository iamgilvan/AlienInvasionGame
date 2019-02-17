class GameStats():
    """Stores statistical data of the Alien Invasion."""
    def __init__(self, ai_settings):
        """Initializes statistical data."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Starts the Alien Invasion in an active state
        self.game_active = True


    def reset_stats(self):
        """Initializes statistical data that may change during the game."""
        self.ships_left = self.ai_settings.ship_limit