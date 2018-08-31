import pygame


class Background(pygame.sprite.Sprite):
    """
    Classes responsible for representing a tile
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
        self.block_mvm = False

    def update(self, movement):
        """
        Function created to be able to edit this object location
        :param movement: Shift of position
        """
        if (movement[0] == 0):
            movement = (-1, 0)

        if not self.block_mvm:
            self.rect.x += movement[0]
