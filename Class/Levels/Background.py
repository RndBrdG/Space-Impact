import pygame


class Background(pygame.sprite.Sprite):
    """
    Class responsible for representing a tile
    """

    def __init__(self, x, y, sprite_url):
        """
        Constructor of the class
        :param x:  Starting position of this tile in the x axis
        :param y: Starting position of this tile in the x axis
        :param sprite_url: Url of the image to be used
        """

        # Initialise Sprite related variables
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite_url).convert()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self, movement):
        """
        Function created to be able to edit this object location
        :param movement: Shift of position
        """

        self.rect.move_ip(movement.x, movement.y)
