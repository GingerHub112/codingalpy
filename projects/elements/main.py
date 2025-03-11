import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)
pygame.display.set_caption("My first game screen")

text = pygame.font.Font(None, 36).render("Hello, World!", True, pygame.Color("black"))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

ticks = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    display.fill((255, 255, 255))
    display.blit(text, text_rect)
    pygame.draw.rect(display, (0, 125, 255), pygame.Rect(30, 30, 60, 60))

    pygame.display.flip()
    ticks.tick(30)
