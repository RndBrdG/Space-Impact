from classes.Player import *
from Shot import *
from classes.Enemy import *
from Bonus import *
from Explosions import *
import random


class App:
    def __init__(self):
        self._running = True
        self.back1 = pygame.image.load("images/background.png")
        self.back2 = pygame.image.load("images/background.png")
        pygame.mixer.init()
        self.backgroundMusic = pygame.mixer.Sound("sounds/bg.wav")
        self.backgroundMusic.set_volume(0.4)
        self.backgroundMusic.play()
        self.bg_one_x = 0
        self.bg_two_x = self.back2.get_width()
        self._window = None
        self.size = self.weight, self.height = 840, 440
        self.level = 1
        self.boss = False
        self.player = Player((0, 0), 100)
        self.framePerSecond = pygame.time.Clock()
        self.explosions = []
        self.bonus = []

    def on_init(self):
        pygame.init()
        self._window = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Space Impact', 'Spine Runtime')
        self._window.fill((0, 0, 0))
        self._running = True
        pygame.key.set_repeat(1, 1)

    def on_event(self, event):
        pass

    def on_render(self):
        pygame.display.flip()

    def check_collisions(self):
        pass

    def draw(self):
        pass

    def generate_random_bonus(self):
        pass

    def on_execute(self):

        while self._running:
            if self.player.retrieve_health_information() <= 0:
                break

            self.check_collisions()
            self._window.blit(self.player.image, (self.player.position_X, self.player.position_Y))
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
            self.framePerSecond.tick(60)
        pygame.quit()
