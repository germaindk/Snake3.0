import pygame
import color

pygame.init()
screen = pygame.display.set_mode((1800, 720))
running = True


screen.fill(color.GREEN)
pygame.display.update()

snake = pygame.image.load("ball.png")
running = True

while running:
    screen.blit(snake, (0,0))
    pygame.display.flip()




while True:
    for event in pygame.event.get():
        print(event)

