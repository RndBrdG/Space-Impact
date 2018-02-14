import pygame


class Camera:
    """
    Class responsible for handling camera
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

        return target.rect.move(self.location.topleft)

    def update(self, player_location):
        """
        Updates camera location to match player's location
        :param player_location: Player Location
        :return:
        """

        self.location = self.complex_camera(player_location)

    def complex_camera(self, object_location):
        """
        Function to change camera movement.
        Based on https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame/14357169#14357169
        :param object_location: Object's location
        :return:
        """
        l, t, _, _ = object_location
        _, _, w, h = self.location
        l, t, _, _ = -l + self.location.width/2, -t + self.location.height/2, w, h

        l = min(0, l)  # stop scrolling at the left edge
        l = max(-(self.location.width - self.location.width), l)  # stop scrolling at the right edge
        t = max(-(self.location.height - self.location.height), t)  # stop scrolling at the bottom
        t = min(0, t)  # stop scrolling at the top
        return pygame.Rect(l, t, w, h)
