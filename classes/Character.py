from abc import ABC


class Character(ABC):
    """
    Abstract class that will be the foundation for enemy and player classes
    """

    def __init__(self, initial_position, health):
        """
        Constructor of the class
        :param initial_position: Tuple with x and y position
        :param health: Amount of health points the character will have
        """
        self.position_X, self.position_Y = initial_position
        self.hp = health

    def change_character_position(self, x_axis, y_axis):
        """
        Function to be called to modify player's position
        :param x_axis: Amount of units to be added to player's x position
        :param y_axis: Amount of units to be added to player's y position
        """

        self.position_X += x_axis
        self.position_Y += y_axis

    def take_damage(self, amount):
        """
        Function that reduces player's health as it takes damage
        :param amount:
        :return:
        """

        self.health -= amount
