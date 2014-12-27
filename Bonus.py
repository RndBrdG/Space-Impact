import pygame


class Bonus:

    def __init__(self, positionX, positionY, bonus_type, bonus, duration, image):
        self.x = positionX
        self.y = positionY
        self.type = bonus_type
        self.bonus = bonus
        self.duration = duration
        self.image = pygame.image.load(image)