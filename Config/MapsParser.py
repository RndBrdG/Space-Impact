import configparser


class MapsParser:
    """
    Classes responsible for parsing maps.ini
    """

    def __init__(self, file_url="./Config/maps.ini"):
        """
        Constructor of the class.
        :param file_url: Url for the configuration file
        """

        self.config = configparser.ConfigParser()
        self.config.read(file_url)

    def get_level_related_map_information(self, level):
        """
        Function that retrieves information about a specific level
        :param level: Level wanted
        :return: A tuple containing map configuration and an array containing filenames for the backgrounds
        """

        section_name = "LEVEL" + str(level)

        try:
            level = self.config[section_name]
            map_design = level["map"]
            map_background = level["background_sprite"].split(',')
        except configparser.NoSectionError:
            print('Level is not loadable. Check if level exists in provided file.')
            raise

        return map_design, map_background
