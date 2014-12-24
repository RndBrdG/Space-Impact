import pygame

class Shot:

    def __init__(self, position_x, position_y, speed):
        self.position_X = position_x
        self.position_Y = position_y
        self.speed = speed
        self.damage = 50
        self.image = pygame.image.load("friendly_beam.png")

    def increment_position_X(self):
        self.position_X += 2*self.speed

    def decrement_position_X(self):
        self.position_X -= 2*self.speed
