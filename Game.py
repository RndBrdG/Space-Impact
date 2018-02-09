from Class.Characters.Player import *
from Class.Levels.Background import Background
from Class.Levels.Level import Level
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
        self.config = ConfigParser('./Config/config.ini')

        # Create Pygame related objects
        pygame.init()
        self.screen = pygame.display.set_mode((self.config.game_config.width, self.config.game_config.height),
                                              pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.config.game_config.title)

        # Create Sprite containers
        self.enemies_sprites = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group
        self.background_sprites = pygame.sprite.Group()

        # Create Player object
        self.player = Player((0, 0), 100)

        # Load initial level
        self.load_level(1)

    def load_level(self, level=1):
        """
        Class responsible for loading a specific level passed as argument.
        :param level: Desired level or 1 by default
        """

        level_loaded = Level(level).map_parsed

        # calculating size of level
        y_axis_length = len(level_loaded)
        x_axis_length = len(level_loaded[0])

        # calculating size of background sprites
        b_sprite_width = self.config.game_config.width / x_axis_length
        b_sprite_height = self.config.game_config.height / y_axis_length

        for y in range(y_axis_length):
            for x in range(x_axis_length):
                if level_loaded[y][x] == '.':
                    self.background_sprites.add(Background(b_sprite_width * x, b_sprite_height * y,
                                                           b_sprite_width, b_sprite_height,
                                                           './images/background.png'))

    def game_loop(self):

        while True:

            delta = self.clock.tick(60) / 1000

            if self.player.retrieve_health_information() <= 0:
                break

            self.enemies_sprites.update(delta)
            self.player.update(delta)
            self.screen.blit(self.player.image, self.player.rect)
            self.background_sprites.draw(self.screen)
            self.enemies_sprites.draw(self.screen)

            pygame.display.flip()
        pygame.quit()
