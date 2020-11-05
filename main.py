import pygame as pg
import random
from math import sin, cos, atan, fabs, pi

pg.init()
pg.mixer.init()

W = 800
H = 600
FPS = 60

# COLOR = (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screen = pg.display.set_mode((W, H))
screen.fill(BLACK)
pg.display.set_caption("My Game")
clock = pg.time.Clock()


class Tower(pg.sprite.Sprite):
    def __init__(self, color):
        """Конструктору необходимо передать цвет(тип) башни"""
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((20, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = event.pos[0]
        self.rect.centery = event.pos[1]
        self.color = color

    def targetting(self, target):
        pass

    def update(self):
        color = random.choice([GREEN, WHITE, RED, BLUE, YELLOW])
        shell = Shell(self.rect.centerx, self.rect.centery, color)
        all_sprites.add(shell)
        shells.add(shell)


class Shell(pg.sprite.Sprite):
    def __init__(self, x, y, color):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((5, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 10
        self.damage = 1  # Fixme
        self.cooldown = 5  # Fixme

    def update(self, target):
        """Направляет снаряд в цель"""
        alpha = Shell.angle(target.rect.centerx,
                            target.rect.centery,
                            self.rect.x,
                            self.rect.y)
        self.rect.centerx += cos(alpha) * self.speed
        self.rect.centery += sin(alpha) * self.speed
        if (self.rect.centerx > W or self.rect.centerx < 0 or
                self.rect.centery > H or self.rect.centery < 0):
            self.kill()

    @staticmethod
    def angle(x1, y1, x2, y2):
        """
        x1, y1 - координаты таргета,
        x2, y2 - координаты снаряда
        """
        if x2 - x1:
            alpha = atan(fabs((y2 - y1) / (x2 - x1)))        # Fixme
        else:
            alpha = pi/2

        if x1 < x2 and y1 > y2:
            alpha = pi - alpha
        elif x1 < x2 and y1 < y2:
            alpha = pi + alpha
        elif x1 > x2 and y1 < y2:
            alpha = -alpha
        return alpha


class Mob(pg.sprite.Sprite):
    def __init__(self, x, y, level=None):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((15, 15))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 1 + 0.1 * level
        self.hp = 10 * level

    def update(self):
        self.rect.x += self.speed
        self.rect.y += 0


all_sprites = pg.sprite.Group()
towers = pg.sprite.Group()
shells = pg.sprite.Group()

cooldown = 10  # Fixme
counter = 0  # Fixme
target = Mob(W/2, H/2)
all_sprites.add(target)

fire = False
status = 'running'
while status == 'running':
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                tower = Tower(WHITE)
                all_sprites.add(tower)
                towers.add(tower)
                fire = True

        elif event.type == pg.QUIT:
            status = 'quit'

    # Обновление
    if fire and counter % cooldown == 0:  # Fixme
        towers.update()
    shells.update(target)
    counter += 1  # Fixme
    target.rect.x += target.speed
    if target.rect.x > W or target.rect.x < 0:
        target.speed *= -1

    hits = pg.sprite.spritecollide(target, shells, True)
    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pg.display.flip()

if status == 'quit':
    pg.quit()
