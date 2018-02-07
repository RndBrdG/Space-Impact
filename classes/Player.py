import pygame
from classes.Character import Character


class Player(metaclass=Character):
    """
    Player class holds information about the player
    """

    def __init__(self):
        """
        Constructor of the class
        """
        super((0, 10), 100)
        self.points = 0
        self.image = pygame.image.load("images/ship.png")
        self.double_guns = False
        self.shots = []
        self.enemies = []
        self.enemies_shots = []
