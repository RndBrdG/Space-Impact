import pygame
from classes.Character import Character


class Enemy(metaclass=Character):
    """
    Class that holds all the information about the enemy objects
    """

    def __init__(self, position_x, position_y, speed, img_length, img_width):
        """
        Constructor
        :param position_x: Initial X position
        :param position_y: Initial Y position
        :param speed: Speed at which the enemy will move
        :param img_length: Length of the sprite
        :param img_width: Width of the sprite
        """
        super((position_x, position_y), 1500)
        self.speed = speed
        self.img_length = img_length
        self.img_width = img_width
        self.movement = 'UP'
        self.image = pygame.image.load("images/enemy_ship.png")

