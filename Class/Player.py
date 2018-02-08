import pygame
from Class.Character import Character


class Player(Character):
    """
    Player class holds information about the player
    """

    def __init__(self, initial_position, health):
        """
        Constructor of the class
        """
        super().__init__(initial_position, health)
        self.points = 0
        self.image = pygame.image.load("images/ship.png")
        self.double_guns = False
        self.shots = []
        self.enemies = []
        self.enemies_shots = []
