from abc import ABC, abstractmethod

import pygame


class Character(ABC, pygame.sprite.Sprite):
    """
    Abstract class that will be the foundation for enemy and player Classes
    """

    def __init__(self, initial_position, health, sprite_url):
        """
        Constructor of the class
        :param initial_position: Tuple with x and y position
        :param health: Amount of health points the character will have
        :param sprite_url: Url for the sprite file
        """

        # Initialise Sprite related variables
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite_url).convert()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = initial_position

        # Initialise character variables
        self.hp = health

    def change_character_position(self, x_axis, y_axis):
        """
        Function to be called to modify player's position
        :param x_axis: Amount of units to be added to player's x position
        :param y_axis: Amount of units to be added to player's y position
        """
        self.rect.move_ip(x_axis * 5, y_axis * 5)

    def take_damage(self, amount):
        """
        Function that reduces player's health as it takes damage
        :param amount: Amount of damage the character will take
        """

        self.hp -= amount

    def retrieve_health_information(self):
        """
        Retrieves the health information about this character
        :return: health variable
        """

        return self.hp

    @abstractmethod
    def update(self, delta):
        """
        Function that every child class has to implement
        """
        pass
