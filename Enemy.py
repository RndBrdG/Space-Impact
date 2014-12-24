import pygame

class Enemy:

    def __init__(self, position_x, position_y, speed, img_length, img_width):
        self.position_X = position_x
        self.position_Y = position_y
        self.speed = speed
        self.img_length = img_length
        self.img_width = img_width
        self.health = 1500
        self.movement = 'UP'
        self.image = pygame.image.load("enemy_ship.png")

    def decrement_position_X(self):
        self.position_X -= 2

    def increment_position_Y(self):
        self.position_Y += 2

    def decrement_position_Y(self):
        self.position_Y -= 2

    def hit(self, damage):
        self.health -= damage
