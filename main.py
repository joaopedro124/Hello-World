import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            break
    pygame.display.flip()

