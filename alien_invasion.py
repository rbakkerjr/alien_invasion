import sys
import pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """ Initialize the game and create the game resources"""
        pygame.init()
        self.settings = Settings()

        # Setup the game window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible
            pygame.display.flip()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

if __name__ == '__main__':
    # Make a game instance and then run the game
    ai = AlienInvasion()
    ai.run_game()
