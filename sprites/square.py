import pygame
import random

pygame.init()

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BG_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

colors = {
    "blue": pygame.Color("blue"),
    "light_blue": pygame.Color("lightblue"),
    "dark_blue": pygame.Color("darkblue"),
    "yellow": pygame.Color("yellow"),
    "magenta": pygame.Color("magenta"),
    "orange": pygame.Color("orange"),
    "white": pygame.Color("white"),
}

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.v = [random.choice([-1, 1]), random.choice([-1, 1])]
    
    def update(self):
        self.rect.move_ip(self.v)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.v[0] = -(self.v[0])
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.v[1] = -(self.v[1])
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BG_COLOR_CHANGE_EVENT))
    def change_color(self):
            self.image.fill(random.choice([colors["yellow"], colors["magenta"], colors["orange"], colors["white"]]))

def change_bg():
    global bg_color
    bg_color = random.choice([colors["blue"], colors["dark_blue"], colors["light_blue"]])

all_sprs_list = pygame.sprite.Group()
sp1 = Sprite(colors["white"], 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
all_sprs_list.add(sp1)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Game")
bg_color = colors["blue"]
screen.fill(bg_color)
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type == BG_COLOR_CHANGE_EVENT:
            change_bg()

    all_sprs_list.update()
    screen.fill(bg_color)
    all_sprs_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)

pygame.quit()