import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)
pygame.display.set_caption("Hello, Penguin")

background = pygame.transform.scale(
    pygame.image.load("background.png").convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

penguin = pygame.transform.scale(
    pygame.image.load("penguin.png").convert_alpha(),
    (200, 200)
)
penguin_rect = penguin.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-30))

egg = pygame.transform.scale(
    pygame.image.load("egg.png").convert_alpha(),
    (300, 400)
)
egg_rect = egg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

text = pygame.font.Font(None, 36).render("Hello, Penguin!", True, pygame.Color("black"))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

ticks = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    display.blit(background, (0,0))
    display.blit(egg, egg_rect)
    display.blit(penguin, penguin_rect)
    display.blit(text, text_rect)

    pygame.display.flip()
    ticks.tick(30)
