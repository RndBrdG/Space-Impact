import configparser


class ConfigParser:
    """
    Class responsible for reading and storing information in config.ini file
    """

    def __init__(self, url):
        """
        Constructor of the class. Stores every section in different variables
        :param url:
        """
        config = configparser.ConfigParser()
        config.read(url)

        self.game_config = GameConfig(config['GameVariables'])


class GameConfig:
    """
    Class responsible for storing the information available in section GameVariables of config.ini
    """

    def __init__(self, game_section):
        """
        Constructor of the class
        :param game_section: GameVariable section
        """

        self.title = game_section['Title']
        self.width = int(game_section['Width'])
        self.height = int(game_section['Height'])
        self.sound_volume = float(game_section['Sound_Volume'])
        self.difficulty = int(game_section['Difficulty'])

