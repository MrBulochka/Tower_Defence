import pygame as pg

pg.init()
pg.mixer.init()

W = 800
H = 600
FPS = 30

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

    def shooting(self):
        shell = Shell(self.rect.centerx, self.rect.centery, self.color)
        all_sprites.add(shell)
        shells.add(shell)


class Shell(pg.sprite.Sprite):
    def __init__(self, x, y, color):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((2, 2))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 10

    def targetting(self, target=None):
        self.rect.x += self.speed
        self.rect.y += self.speed


all_sprites = pg.sprite.Group()
towers = pg.sprite.Group()
shells = pg.sprite.Group()

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
    if fire:
        towers.shooting()
        shells.targetting()
    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pg.display.flip()

if status == 'quit':
    pg.quit()
