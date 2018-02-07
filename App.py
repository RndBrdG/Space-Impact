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
        self.player = Player()
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
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if self.player.position_Y + 35 < self.height - 25:
                    self.player.increment_position_y()
            elif event.key == pygame.K_UP:
                if self.player.position_Y - 5 > 0:
                    self.player.decrement_position_y()
            elif event.key == pygame.K_LEFT:
                if self.player.position_X - 5 > 0:
                    self.player.decrement_position_x()
            elif event.key == pygame.K_RIGHT:
                if self.player.position_X + 55 < self.weight:
                    self.player.increment_position_x()
            elif event.key == pygame.K_SPACE:
                if self.player.double_guns:
                    self.player.shots.append(Shot(self.player.position_X, self.player.position_Y + 45, 1))
                self.player.shots.append(Shot(self.player.position_X, self.player.position_Y, 1))
                shot_music = pygame.mixer.Sound("sounds/shot.wav")
                shot_music.set_volume(0.05)
                shot_music.play()

    def on_render(self):
        pygame.display.flip()

    def check_collisions(self):
        # First we check if there is any battleship touching ours
        for (index, enemy) in enumerate(self.player.enemies):
            if enemy.position_X < self.player.position_X + 50 and enemy.position_X + enemy.img_width > self.player.position_X and enemy.position_Y < self.player.position_Y + 50 and enemy.position_Y + enemy.img_length > self.player.position_Y:
                self.player.health -= 20 * 0.01
                enemy.health -= 30
            else:
                for (index1, shotsFired) in enumerate(self.player.shots):
                    if enemy.position_X < shotsFired.position_X + 8 and enemy.position_X + enemy.img_width > shotsFired.position_X and enemy.position_Y < shotsFired.position_Y + 8 and enemy.position_Y + enemy.img_length > shotsFired.position_Y:
                        enemy.hit(shotsFired.damage)
                        if enemy.health <= 0:
                            explosion = pygame.mixer.Sound("sounds/explosion.aiff")
                            explosion.set_volume(0.1)
                            explosion.play()
                            self.player.points += 5
                            if self.boss:
                                self.level += 1
                                self.boss = False
                                self.player.points = 0
                            self.explosions.append(Explosions(enemy.position_X, enemy.position_Y))
                            self.player.enemies.pop(index)
                        self.player.shots.pop(index1)
                        break

        for (index, shotsFired) in enumerate(self.player.enemies_shots):
            if self.player.position_X < shotsFired.position_X + 8 and self.player.position_X + 50 > shotsFired.position_X and self.player.position_Y < shotsFired.position_Y + 8 and self.player.position_Y + 50 > shotsFired.position_Y:
                self.player.hit()
                self.player.enemies_shots.pop(index)
                if self.player.health <= 0:
                    break
        for (index, bonus_item) in enumerate(self.bonus):
            if self.player.position_X < bonus_item.x + bonus_item.image.get_width() and self.player.position_X + 50 > bonus_item.x and self.player.position_Y < bonus_item.y + bonus_item.image.get_height() and self.player.position_Y + 50 > bonus_item.y:
                if bonus_item.type == "HEALTH":
                    if self.player.health + bonus_item.bonus > 100:
                        self.player.health = 100
                    else:
                        self.player.health += bonus_item.bonus
                    self.bonus.pop(index)
                elif bonus_item.type == "DOUBLE_GUNS":
                    self.player.double_guns = True

    def draw(self):
        self._window.blit(self.back1, (self.bg_one_x, 0))
        self._window.blit(self.back2, (self.bg_two_x, 0))

        self.bg_one_x -= 1 * self.level
        self.bg_two_x -= 1 * self.level

        if self.bg_one_x <= -1 * self.back1.get_width():
            self.bg_one_x = self.bg_two_x + self.back1.get_width()
        if self.bg_two_x <= -1 * self.back2.get_width():
            self.bg_two_x = self.bg_one_x + self.back2.get_width()
        pygame.draw.rect(self._window, (255, 0, 0),
                         pygame.Rect(0, self.height - 5, self.weight * self.player.health / 100, 5))
        pygame.draw.rect(self._window, (0, 255, 0), pygame.Rect(0, 0, self.weight * self.player.points / 100, 5))
        for (index, shot_obj) in enumerate(self.player.shots):
            self._window.blit(shot_obj.image, (shot_obj.position_X, shot_obj.position_Y))
            shot_obj.increment_position_x()
            if shot_obj.position_X > self.weight:
                self.player.shots.pop(index)

        for (index, shot_obj) in enumerate(self.player.enemies_shots):
            self._window.blit(shot_obj.image, (shot_obj.position_X, shot_obj.position_Y))
            shot_obj.decrement_position_x()
            if shot_obj.position_X < 0:
                self.player.enemies_shots.pop(index)

        for (index, expl_obj) in enumerate(self.explosions):
            self._window.blit(expl_obj.image, (expl_obj.position_X, expl_obj.position_Y))
            self.explosions.pop(index)

        for (index, bonus_item) in enumerate(self.bonus):
            self._window.blit(bonus_item.image, (bonus_item.x, bonus_item.y))
            if bonus_item.type == "DOUBLE_GUNS":
                if self.player.double_guns:
                    bonus_item.x = -50000
                bonus_item.increment_position(self.level)
                if bonus_item.x > self.weight - 10:
                    self.bonus.pop(index)
            else:
                bonus_item.decrement_position(self.level)
                if bonus_item.x < 10:
                    self.bonus.pop(index)

        for (index, enemy) in enumerate(self.player.enemies):
            self._window.blit(enemy.image, (enemy.position_X, enemy.position_Y))
            if self.boss == False:
                enemy.decrement_position_x(self.level)
                if enemy.position_X - 25 <= 0:
                    self.player.enemies.pop(index)
            else:
                if enemy.position_Y <= (self.height / 2 - 75):
                    enemy.increment_position_y(self.level)
                    enemy.movement = 'UP'
                elif enemy.position_Y >= (self.height / 2 + 75):
                    enemy.decrement_position_y(self.level)
                    enemy.movement = 'DOWN'
                elif enemy.movement == 'UP':
                    enemy.increment_position_y(self.level)
                elif enemy.movement == 'DOWN':
                    enemy.decrement_position_y(self.level)

    def generate_random_enemies(self):
        if self.player.points < 100:
            number_of_enemies = random.randint(0, 6)
            position_Y = random.randint(0, self.height - 70)
            while number_of_enemies > 0:
                y = random.randint(0, self.height - 50)
                self.player.enemies.append(Enemy(self.weight - 50 * number_of_enemies, y, -1, 50, 50))
                number_of_enemies -= 1
        else:
            self.player.points = 0
            self.boss = True
            if self.level == 1:
                self.player.enemies.append(Enemy(self.weight - 100, self.height / 2, -1, 76, 77))
                for enemy in self.player.enemies:
                    enemy.health = 15000
                    enemy.image = pygame.image.load("images/monster_lvl1.png")
            elif self.level == 2:
                self.player.enemies.append(Enemy(self.weight - 100, self.height / 2, -1, 69, 77))
                for enemy in self.player.enemies:
                    enemy.image = pygame.image.load("images/monster_lvl2.png")
                    enemy.health = 20000
            else:
                self.player.enemies.append(Enemy(self.weight - 100, self.height / 2, -1, 51, 67))
                for enemy in self.player.enemies:
                    enemy.image = pygame.image.load("images/monster_lvl3.png")
                    enemy.health = 50000

    def generate_random_shots(self):
        for enemy in self.player.enemies:
            if self.boss:
                i = random.randint(0, 100)
                if i < 10:
                    number_of_shots = random.randint(0, 2)
                    while number_of_shots:
                        pos_y = random.randint(enemy.position_Y - 50, enemy.position_Y + 50)
                        self.player.enemies_shots.append(Shot(enemy.position_X - 50, pos_y, self.level))
                        number_of_shots -= 1
                for beams in self.player.enemies_shots:
                    beams.image = pygame.image.load("images/enemy_beam.png")
            else:
                i = random.randint(0, 1)
                while i > 0:
                    self.player.enemies_shots.append(Shot(enemy.position_X - 50 * i, enemy.position_Y + 25, self.level))
                    i -= 1

    def generate_random_bonus(self):
        if len(self.bonus) == 0:
            i = random.randint(0, 5000)
            posx = random.randint(round(self.weight / 3), round(2 * self.weight / 3))
            posy = random.randint(50, self.height - 50)
            if i < 1:
                self.bonus.append(Bonus(posx, posy, "HEALTH", 20, -1, "images/red-potion.png"))
            elif i == 1 or i == 2:
                if not self.player.double_guns:
                    self.bonus.append(Bonus(posx, posy, "DOUBLE_GUNS", -1, 20 * 1000, "images/bomb.png"))

    def updateBonusTime(self):
        for (index, bonusActive) in enumerate(self.bonus):
            if bonusActive.type == "DOUBLE_GUNS" and self.player.double_guns:
                if bonusActive.time + self.framePerSecond.get_time() < bonusActive.duration:
                    bonusActive.time += self.framePerSecond.get_time()
                else:
                    self.bonus.pop(index)
                    self.player.double_guns = False

    def on_execute(self):
        if not self.on_init():
            self._running = False

        while self._running:
            if self.player.health <= 0:
                break

            self.check_collisions()
            self.generate_random_bonus()
            if len(self.player.enemies_shots) <= 5:
                self.generate_random_shots()
            self.draw()
            if len(self.player.enemies) == 0:
                self.generate_random_enemies()
            self._window.blit(self.player.image, (self.player.position_X, self.player.position_Y))
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
            self.updateBonusTime()
            self.framePerSecond.tick(60)
        pygame.quit()
