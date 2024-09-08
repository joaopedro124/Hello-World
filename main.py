import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            break
    tela.fill((255,255,0))
    pygame.display.flip()

