from Config.MapsParser import MapsParser
from Classes.Levels.Background import Background


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
        map_configuration, background_img = level_parser.get_level_related_map_information(self.level)

        self.backgrounds = self.initiate_background_images(background_img)

        self.map_parsed = map_configuration.split('\n')

    def get_map(self):
        """
        Function that retrieves parsed map
        :return: parsed map
        """
        return self.map_parsed

    def get_background_images(self):
        """
        Function to retrieve an array of background images to be used in the level display
        :return: Array of filenames
        """
        return self.background_img

    def initiate_background_images(self, background_images):
        """
        Transforms background images into Background objects
        :return: array of Background objects
        """

        background_obj = []
        x = 0

        for image in background_images:
            bck_img = Background(x, 0, image)
            background_obj.append(bck_img)
            x += bck_img.image.get_size()[0]

        return background_obj
