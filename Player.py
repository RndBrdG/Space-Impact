import pygame

class Player:

    def __init__(self):
        self.points = 0
        self.health = 850
        self.position_X = 10
        self.position_Y = 0
        self.image = pygame.image.load("ship.png")
        self.shots = []
        self.enemies = []

    def increment_position_Y(self):
        self.position_Y += 5

    def decrement_position_Y(self):
        self.position_Y -= 5

    def increment_position_X(self):
        self.position_X += 5

    def decrement_position_X(self):
        self.position_X -= 5