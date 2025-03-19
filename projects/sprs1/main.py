import pygame as pg
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOV_SPEED = 5
FONT_SIZE = 72

pg.init()

font = pg.font.SysFont("Arial", FONT_SIZE)

class Sprite(pg.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pg.Surface([width, height])
        self.image.fill(pg.Color("dodgerblue"))
        pg.draw.rect(self.image, color, pg.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, x, y):
        self.rect.x = max(
            min(self.rect.x + x, SCREEN_WIDTH - self.rect.width),
            0
        )
        self.rect.y = max(
            min(self.rect.y + y, SCREEN_HEIGHT - self.rect.height),
            0
        )

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
all_sprs = pg.sprite.Group()

spr1 = Sprite(pg.Color("dodgerblue"), 20, 30)
spr1.rect.x, spr1.rect.y = random.randint(0, SCREEN_WIDTH - spr1.rect.width) ,random.randint(0, SCREEN_HEIGHT - spr1.rect.height)
all_sprs.add(spr1)

spr2 = Sprite(pg.Color("red"), 20, 30)
spr2.rect.x, spr2.rect.y = random.randint(0, SCREEN_WIDTH - spr2.rect.width), random.randint(0, SCREEN_HEIGHT - spr2.rect.height)
all_sprs.add(spr2)

running, won = True, False
clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    if not won:
        keys = pg.key.get_pressed()
        x = (keys[pg.K_RIGHT] - keys[pg.K_LEFT]) * MOV_SPEED
        y = (keys[pg.K_DOWN] - keys[pg.K_UP]) * MOV_SPEED
        spr1.move(x, y)

        screen.fill(pg.Color("black"))
        all_sprs.draw(screen)
        pg.display.flip()
        clock.tick(90)

pg.quit()