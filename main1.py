import pygame
import sys
import config

pygame.init()
screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
pygame.display.set_caption(config.TITLE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(config.WHITE) 



    thickness = 15
    for x_offset in range(0, 300, 50):
        pygame.draw.line(screen, config.HOT_PINK, [75 + x_offset, 300], [440 + x_offset, 525], thickness)
        x_offset = x_offset + 20
    
pygame.display.flip()

pygame.quit()
sys.exit()