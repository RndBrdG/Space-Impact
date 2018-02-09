import pygame


class Background(pygame.sprite.Sprite):
    """
    Class responsible for representing a tile
    """

    def __init__(self, x, y, width_size, height_size, sprite_url):
        """
        Constructor of the class
        :param x:  Starting position of this tile in the x axis
        :param y: Starting position of this tile in the x axis
        :param width_size: Width size of the sprite
        :param height_size: Height size of the sprite
        :param sprite_url: Url of the image to be used
        """

        # Initialise Sprite related variables
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite_url).convert()
        self.image = pygame.transform.scale(self.image, (int(width_size), int(height_size)))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

