import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((0,0,0))
pygame.display.set_caption("Draw and Save")

drawing = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        if event.type == pygame.MOUSEMOTION and drawing:
            pygame.draw.circle(screen, (255, 255, 255), event.pos, 10)

    pygame.display.flip()

    if pygame.key.get_pressed()[pygame.K_s]:  # Press 'S' to save
        pygame.image.save(screen, "drawing.png")