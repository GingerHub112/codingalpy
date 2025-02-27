import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My Window")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()