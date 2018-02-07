import pygame


class Shot:
    """
    Class that holds all the information related to the shots present in the scene
    """

    def __init__(self, position_x, position_y, level):
        """
        Constructor of the class
        :param position_x: Initial X position
        :param position_y: Initial Y position
        :param level: Player's level
        """

        self.position_X = position_x
        self.position_Y = position_y
        self.level = level
        self.damage = 50
        self.image = pygame.image.load("images/friendly_beam.png")

    def change_shot_position(self, x_axis, y_axis):
        """
        Function that changes shots position by x_axis, y_axis amount
        :param x_axis: amount of units to move shot in x axis
        :param y_axis: amount of units to move shot in y axis
        """

        self.position_X += x_axis * self.level
        self.position_Y += y_axis * self.level
