import pygame
from Player import *
from Shot import *
from Enemy import *
from pygame.locals import *

import random

class App:
    def __init__(self):
        self._running = True
        self._window = None
        self.size = self.weight, self.height = 840, 400
        self.player = Player()
        self.framePerSecond = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self._window = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Space Invaders','Spine Runtime')
        self._window.fill((0, 0, 0))
        self._running = True
        pygame.key.set_repeat(1, 1)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                self.player.increment_position_Y()
            elif event.key == K_UP:
                self.player.decrement_position_Y()
            elif event.key == K_LEFT:
                self.player.decrement_position_X()
            elif event.key == K_RIGHT:
                self.player.increment_position_X()
            elif event.key == K_SPACE:
                self.player.shots.append(Shot(self.player.position_X, self.player.position_Y, 1))

    def on_render(self):
        pygame.display.flip()

    def check_colisions(self):
        # First we check if there is any battleship touching ours

        for (index, enemy) in enumerate(self.player.enemies):
            if enemy.position_Y == self.player.position_Y:
                print("R")
            if enemy.position_Y <= self.player.position_Y + 50 & enemy.position_Y >= self.player.position_Y:
                self.player.health -= enemy.health
                print("SUICIDE")
                self.player.enemies.pop(index)
                continue

            for (index,shotsFired) in enumerate(self.player.shots):
                if shotsFired.position_X == enemy.position_X & shotsFired.position_Y > enemy.position_Y & \
                        shotsFired.position_Y + 8 < enemy.position_Y+50:
                    print("Shots fired")
                    enemy.hit()
                    self.player.shots.pop(index)
                    continue



    def draw(self):
        self._window.fill((0,0,0))
        for (index, shot_obj) in enumerate(self.player.shots):
            self._window.blit(shot_obj.image, (shot_obj.position_X, shot_obj.position_Y))
            shot_obj.increment_position_X()
            if shot_obj.position_X > self.weight:
                self.player.shots.pop(index)
        for (index, enemy) in enumerate(self.player.enemies):
            self._window.blit(enemy.image, (enemy.position_X, enemy.position_Y))
            enemy.decrement_position_X()
            if enemy.position_X <= 0:
                self.player.enemies.pop(index)

    def generate_random_enemies(self):
        number_of_enemies = random.randint(0,5)
        position_Y = random.randint(0, self.height)
        while number_of_enemies > 0:
            self.player.enemies.append(Enemy(self.weight - 50*number_of_enemies, position_Y, -1))
            number_of_enemies -= 1

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            self.draw()
            print("Health", self.player.health)
            if len(self.player.enemies) == 0:
                self.generate_random_enemies()
            self.check_colisions()
            self._window.blit(self.player.image,(self.player.position_X,self.player.position_Y))
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
            self.framePerSecond.tick(30)
        pygame.quit()
