import pygame


class Bonus:

    def __init__(self, position_x, position_y, bonus_type, bonus, duration, image):
        self.x = position_x
        self.y = position_y
        self.type = bonus_type
        self.bonus = bonus
        self.duration = duration
        self.image = pygame.image.load(image)
        self.time = 0

    def decrement_position(self, level):
        self.x -= 0.5 + level * 0.2

    def increment_position(self, level):
        self.x += 1.5 + level * 0.2
