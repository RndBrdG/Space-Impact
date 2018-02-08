import pygame
from Class.Character import Character


class Enemy(Character):
    """
    Class that holds all the information about the enemy objects
    """

    def __init__(self, initial_position, hp):
        """
        Constructor
        :param initial_position: Initial position
        :param hp: Amount of health points this character will start with
        """
        super().__init__(initial_position, hp, "images/enemy_ship.png")

    def update(self, delta):
        """
        Update Function that takes into consideration time lapsed.
        :param delta: Time elapsed. It is turned into negative, since enemies will travel in opposite ways
        """
        self.change_character_position(100 * delta, 0 * delta)
