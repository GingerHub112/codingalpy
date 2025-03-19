import pygame
import random

pygame.init()

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

def change_bg():
    global bg_color
    bg_color = random.choice([colors["blue"], colors["dark_blue"], colors["light_blue"]])

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Game")
bg_color = colors["blue"]
screen.fill(bg_color)
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                pygame.event.post(pygame.event.Event(BG_COLOR_CHANGE_EVENT))
        elif event.type == pygame.QUIT:
            running = False
        elif event.type == BG_COLOR_CHANGE_EVENT:
            change_bg()
        
    
    screen.fill(bg_color)
    pygame.display.flip()
    clock.tick(240)

pygame.quit()