import pygame


class Camera:
    """
    Classes responsible for handling camera
    """

    def __init__(self, width, height):
        """
        Constructor of the class
        :param width: Viewable width area
        :param height: Viewable height area
        """

        self.location = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        """
        Applies location changes to the other objects
        :param target:
        :return:
        """

        return target.rect.move(self.location.x, self.location.y)

    def update(self, delta):
        """
        Updates camera location to match player's location
        :param delta: Time
        :return:
        """

        self.location = delta
