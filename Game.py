from Class.Player import *
from Config.ConfigParser import ConfigParser
from Explosions import *


class Game:

    def __init__(self):

        # Read configuration file
        config = ConfigParser('./Config/config.ini')

        # Create Pygame related objects
        pygame.init()
        self.screen = pygame.display.set_mode((config.game_config.width, config.game_config.height))
        pygame.display.set_caption(config.game_config.title)

        self.player = Player((0, 0), 100)
        self.framePerSecond = pygame.time.Clock()

    def on_init(self):
        pass

    def on_event(self, event):
        pass

    def on_render(self):
        pass

    def check_collisions(self):
        pass

    def draw(self):
        pass

    def generate_random_bonus(self):
        pass

    def on_execute(self):

        self.on_init()

        while True:
            if self.player.retrieve_health_information() <= 0:
                break

            self.check_collisions()
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
            self.framePerSecond.tick(60)
        pygame.quit()
