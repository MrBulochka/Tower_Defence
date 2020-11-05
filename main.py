import pygame as pg
import random

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
        color = random.choice([GREEN, WHITE, RED, BLUE])
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
        self.speed = 2
        self.damage = 1  # Fixme
        self.cooldown = 5  # Fixme

    def update(self):
        self.rect.x += self.speed  # Fixme
        self.rect.y += self.speed  # Fixme
        if (self.rect.centerx > W or self.rect.centerx < 0)\
        or (self.rect.centery > H or self.rect.centery < 0):
            self.kill()


class Mob(pg.sprite.Sprite):
    def __init__(self, x, y, level):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x  # Fixme
        self.rect.centery = y  # Fixme
        self.speed = 0.5  # Fixme
        self.hp = 10  # Fixme

    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed


all_sprites = pg.sprite.Group()
towers = pg.sprite.Group()
shells = pg.sprite.Group()

# target = pg.Surface(10, 10)
cooldown = 10  # Fixme
counter = 0  # Fixme

fire = False
status = 'running'
while status == 'running':
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                tower = Tower(GREEN)
                all_sprites.add(tower)
                towers.add(tower)
                fire = True

        elif event.type == pg.QUIT:
            status = 'quit'

    # Обновление
    if fire and counter % cooldown == 0:  # Fixme
        all_sprites.update()
    shells.update()
    counter += 1  # Fixme
    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pg.display.flip()

if status == 'quit':
    pg.quit()
