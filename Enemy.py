import pygame

class Enemy:

    def __init__(self, position_x, position_y, speed):
        self.position_X = position_x
        self.position_Y = position_y
        self.speed = speed
        self.health = 500
        self.image = pygame.image.load("enemy_ship.png")

    def decrement_position_X(self):
        self.position_X += 5*self.speed

    def increment_position_Y(self):
        self.position_Y += 5*self.speed

    def hit(self):
        self.health -= 150