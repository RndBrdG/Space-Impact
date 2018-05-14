from Config.MapsParser import MapsParser


class Level:
    """
    Classes responsible for loading and storing all the information about a specific level to be played
    """

    def __init__(self, level):
        """
        Constructor of the class. It is responsible for loading the level characteristics from map.ini
        :param level: Level to be played
        """

        self.level = int(level)

        # Load information about level
        level_parser = MapsParser()
        level_configuration = level_parser.get_level_related_map_information(self.level)

        map_unparsed = level_configuration
        self.map_parsed = map_unparsed.split('\n')

    def get_map(self):
        """
        Function that retrieves parsed map
        :return: parsed map
        """
        return self.map_parsed
