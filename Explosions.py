import pygame


class Explosions:

    def __init__(self, position_x, position_y):
        self.position_X = position_x
        self.position_Y = position_y
        self.image = pygame.image.load("explosions.png")