import pygame
import sys
import random
import color

pygame.init()
WIN_X = 800
WIN_Y = 600
screen = pygame.display.set_mode((WIN_X,WIN_Y))
pygame.display.set_caption('SN Snake')

def main():

	CLOCK = pygame.time.Clock()
	snake_pos=[200,70]
	snake_body=[[200,70] , [190 , 70] , [180,70]]

	egg_pos=[0,0]
	egg_spawn = True
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
			pygame.draw.rect(screen ,(0, 255, 0), (square[0],square[1],10,10))

		# mouvement
		if direction == 'right':
			snake_pos[0] += 10
		elif direction == 'left':
			snake_pos[0] -= 10
		elif direction == 'up':
			snake_pos[1] -= 10
		elif direction == 'down':
			snake_pos[1] += 10


		if snake_pos[0] <=0 or snake_pos[0] >= WIN_X:
			sys.exit()
		if snake_pos[1] <=0 or snake_pos[1] >= WIN_Y:
			sys.exit()

		for square in snake_body[1:]:
			if pygame.Rect(square[0],square[1],10,10).colliderect(pygame.Rect(snake_pos[0],snake_pos[1],10,10)):
				print("perdu")
				pygame.display.quit
				

		if egg_spawn:
			# choisire la posision de l’œuf
			egg_pos = [random.randrange(40,WIN_X-40), random.randrange(40,WIN_Y-40)]
			#desactiver le spawn les œuf
			egg_spawn = False
			# fair apraraitre l’œuf
		pygame.draw.rect(screen ,(255,255,0),(egg_pos[0],egg_pos[1],10,10))
		#detecter si le serpent touche la l'euf
		if pygame.Rect(snake_pos[0],snake_pos[1],10,10).colliderect(pygame.Rect(egg_pos[0],egg_pos[1],10,10)):
			egg_spawn = True
			score += 10
		else:
			#agrandire la taille du serpent
			snake_body.pop(0)


		#aficher le score
		font = pygame.font.SysFont('comicsans',40)
		score_font = font.render(f'{score}' , True , (255,255,255))
		font_pos = score_font.get_rect(center=(WIN_X//2-40 , 30))
		screen.blit(score_font , font_pos)

		snake_body.append(list(snake_pos))
		pygame.display.update()
		CLOCK.tick(25)

main()
