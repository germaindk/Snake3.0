import pygame
import sys
import random
import os

pygame.init()
screen_X = 900
screen_Y = 600
screen = pygame.display.set_mode((screen_X,screen_Y))
pygame.display.set_caption('SN Snake')

RED = (255, 0, 0)
BLEU = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BLACK = (0,0,0)	
WHITE = (255,255,255)
GREEN = (0, 255, 0)

Lenght_of_snake =1 
score_font = pygame.font.SysFont("Comic",35)
font_style = pygame.font.SysFont("Arial",20)


#Definition du message de fin 
def message(mess,color): 
	msg = font_style.render(mess,True,color)
	screen.blit(msg, [screen_X /2, screen_Y/2])


		
#def main 			
def main():

	CLOCK = pygame.time.Clock()
	snake_pos=[200,70]
	snake_body=[[200,70] , [190 , 70] , [180,70]]

	egg_pos=[0,0]
	egg_spawn = True
	#direction du serpent au départ
	direction = 'right'
	#score
	score=0
	CLOCK = pygame.time.Clock()


	while 1:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			keys = pygame.key.get_pressed()
			#touches 
			if (keys[pygame.K_UP]) and direction != 'down':
				direction = 'up'
			if (keys[pygame.K_DOWN]) and direction != 'up':
				direction = 'down'
			if (keys[pygame.K_RIGHT]) and direction != 'left':
				direction = 'right'
			if (keys[pygame.K_LEFT]) and direction != 'right':
				direction = 'left'
		screen.fill((238,160,14))

		#déssiner le serpent
		for square in snake_body:
			pygame.draw.rect(screen ,(60, 128, 43), (square[0],square[1],10,10))

		# mouvement + vittesse 
		if direction == 'right':
			snake_pos[0] += 10
		elif direction == 'left':
			snake_pos[0] -= 10
		elif direction == 'up':
			snake_pos[1] -= 10
		elif direction == 'down':
			snake_pos[1] += 10

		#Colision serpent/bordure
		if snake_pos[0] <=0 or snake_pos[0] >= screen_X:
			screen.fill("RED")
			message("Perdu appuyer sur R jouer et Q pour quiter", BLACK) 
			
			pygame.display.update()
			if (keys[pygame.K_r]):
				main()
			if (keys[pygame.K_q]):
				pygame.quit()
				sys.exit()
			
		if snake_pos[1] <=0 or snake_pos[1] >= screen_Y:
			screen.fill("RED")
			message("Perdu appuyer sur R jouer et Q pour quiter", BLACK) 
			if (keys[pygame.K_r]):
				main()
			if (keys[pygame.K_q]):
				pygame.quit()
				sys.exit()
			pygame.display.update()
		
		#Colision serpent/serpent
		for square in snake_body[1:]:
			if pygame.Rect(square[0],square[1],10,10).colliderect(pygame.Rect(snake_pos[0],snake_pos[1],10,10)):
				screen.fill("RED")
				message("Perdu appuyer sur R jouer et Q pour quiter", BLACK)
				if (keys[pygame.K_r]):
					main()
				if (keys[pygame.K_q]):
					pygame.quit()
					sys.exit()
				pygame.display.update()
				
				

		if egg_spawn:	
			# choisire la posision de l’œuf
			egg_pos = [random.randrange(40,screen_X-40), random.randrange(40,screen_Y-40)]
			#desactiver le spawn les œuf
			egg_spawn = False
			# Dessiner l'oeuf
		pygame.draw.rect(screen ,(255,255,255),(egg_pos[0],egg_pos[1],10,10))
		#Collision serpent oeuf
		if pygame.Rect(snake_pos[0],snake_pos[1],10,10).colliderect(pygame.Rect(egg_pos[0],egg_pos[1],10,10)):
			egg_spawn = True
			score = 0
			score += 10
		else:
			#Garder la taille du serpent en fonction des oeufs manger
			snake_body.pop(0)


		#aficher le score
		font = pygame.font.SysFont('comicsans',40)
		score_font = font.render(f'{score}' , True , (255,255,255))
		font_pos = score_font.get_rect(center=(screen_X//2-40 , 30))
		screen.blit(score_font , font_pos)

		snake_body.append(list(snake_pos))
		pygame.display.update()
		CLOCK.tick(25)
	



main()
