import pygame
import sys
import random
import color

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('SN Snake')

def main():

	CLOCK = pygame.time.Clock()
	snake_pos=[200,70]
	snake_body=[[200,70],[200-10,70],[200-(2*10),70]]
	#direction du serpent au répart
	direction = 'right'
	#score
	score=0
	CLOCK = pygame.time.Clock()
	#game loop
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			keys = pygame.key.get_pressed()

			if (keys[pygame.K_w] or keys[pygame.K_UP]) and direction != 'down':
				direction = 'up'
			if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and direction != 'up':
				direction = 'down'
			if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and direction != 'left':
				direction = 'right'
			if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and direction != 'right':
				direction = 'left'
		screen.fill((0,0,0))

		#désiner le cor du serpent
		for square in snake_body:
			pygame.draw.rect(screen ,(255, 255, 0), (square[0],square[1],10,10))

		# noinspection PyUnreachableCode
		if direction == 'right':
			snake_pos[0] += 10
		elif direction == 'left':
			snake_pos[0] -= 10
		elif direction == 'up':
			snake_pos[1] -= 10
		elif direction == 'down':
			snake_pos[1] += 10



		snake_body.pop(0)
		snake_body.append(list(snake_pos))
		pygame.display.update()
		CLOCK.tick(25)

main()
