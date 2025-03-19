import pygame as pg
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOV_SPEED = 5
FONT_SIZE = 14

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
    
    def collides(self, other):
        return self.rect.colliderect(other.rect)

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
all_sprs = pg.sprite.Group()

spr1 = Sprite(pg.Color("dodgerblue"), 20, 30)
spr1.rect.x, spr1.rect.y = random.randint(0, SCREEN_WIDTH - spr1.rect.width) ,random.randint(0, SCREEN_HEIGHT - spr1.rect.height)
all_sprs.add(spr1)
enemies = []
for _ in range(0, 7):
    enemies.append(Sprite(pg.Color("red"), 20, 30))
    enemies[-1].rect.x, enemies[-1].rect.y = random.randint(0, SCREEN_WIDTH - enemies[-1].rect.width), random.randint(0, SCREEN_HEIGHT - enemies[-1].rect.height)
    all_sprs.add(enemies[-1])

running, won = True, False
clock = pg.time.Clock()

score = 0

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    keys = pg.key.get_pressed()
    x = (keys[pg.K_RIGHT] - keys[pg.K_LEFT]) * MOV_SPEED
    y = (keys[pg.K_DOWN] - keys[pg.K_UP]) * MOV_SPEED
    spr1.move(x, y)
    for enemy in enemies:
        if spr1.collides(enemy):
            all_sprs.remove(enemy)
            score = 7 - len(all_sprs) + 1

    screen.fill(pg.Color("black"))
    all_sprs.draw(screen)
    text = font.render(f"Score: {score}", True, pg.Color("white"))
    screen.blit(text, (0, 0))
    pg.display.flip()
    clock.tick(90)


pg.quit()