from Class.Player import *
from Config.ConfigParser import ConfigParser
from Explosions import *


class Game:
    """
    Class responsible for managing the game itself and Pygame objects
    """

    def __init__(self):
        """
        Constructor of the class. Reads and parses configuration files as well as initiates game objects
        """

        # Read configuration file
        config = ConfigParser('./Config/config.ini')

        # Create Pygame related objects
        pygame.init()
        self.screen = pygame.display.set_mode((config.game_config.width, config.game_config.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(config.game_config.title)

        # Create Sprite containers
        self.enemies_sprites = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group

        # Create Player object
        self.player = Player((0, 0), 100)

    def game_loop(self):

        while True:

            delta = self.clock.tick(60) / 1000

            if self.player.retrieve_health_information() <= 0:
                break
            self.player.update(delta)
            self.screen.blit(self.player.image, self.player.rect)

            pygame.display.flip()
        pygame.quit()
