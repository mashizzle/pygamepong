import pygame
import random

pygame.init()

display_width = 800
display_height = 600



gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Ultra Pong')
clock = pygame.time.Clock()


black = (0,0,0)
white = (255,255,255)

def bat(x,y,w,h):
	pygame.draw.rect(gameDisplay, black,(x,y,w,h))

def ball(x,y,r):
	pygame.draw.circle(gameDisplay, black,(x,y),r)



def gameLoop():
	bat1x = 10
	bat1y = 200

	bat1w = 10
	bat1h = 200

	bat2x = 780
	bat2y =200

	bat2w = 10
	bat2h = 200

	ballx = 400
	bally = 300
	ballr = 10
	ballSpeed = 0

	y1_change = 0
	y2_change = 0

	bx_change = 0
	by_change = 0
	bSpeed_change = 0
	ballStart = random.randint(1,2)

	p1_score = 0
	p2_score = 0


	gameLoopFinished = False

	while not gameLoopFinished:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		# control for bats
		keys = pygame.key.get_pressed()

		if keys[pygame.K_w] and bat1y > 0:
			y1_change = -3
		if keys[pygame.K_s] and bat1y+bat1h < 600:
			y1_change = 3
		if keys[pygame.K_o] and bat2y > 0:
			y2_change = -3
		if keys[pygame.K_k] and bat2y+bat2h < 600:
			y2_change = 3

		

		bat1y+=y1_change
		bat2y+=y2_change

		# commences ball movement
		if keys[pygame.K_SPACE]:
			if ballStart == 1:
				bx_change = -1
			else:
				bx_change = 1

		ballx+=bx_change

		# controls the ball bouncing of the bats
		if ballx-ballr < bat1x+bat1w:
			if bally >= bat1y and bally <= bat1y+bat1h:
				if bally >= bat1y and bally <= bat1y+(bat1h/2):
					by_change = -2
					bx_change = 1
				else:
					by_change = 2
					bx_change = 1

		ballx+=bx_change
		bally+=by_change

		# ball bouncing of bat
		if ballx+ballr > bat2x+bat2w:
			if bally >= bat2y and bally <= bat2y+bat2h:
				if bally >= bat2y and bally <= bat2y+(bat2h/2):
					by_change = -2
					bx_change = -1
				else:
					by_change = 2
					bx_change = -1

		ballx+=bx_change
		bally+=by_change 

		# when the ball hits the boundaries
		if bally-ballr <= 0 or bally+ballr >= display_height:
			by_change = by_change*-1
		elif ballx-ballr <= 0 or ballx+ballr >= display_width:
			gameLoop()
			#p2_score++
		#elif ballx+ballr > display_width:
			#p1_score++
                        
		


			


		gameDisplay.fill(white)

		bat(bat1x,bat1y,bat1w,bat1h)
		bat(bat2x,bat2y,bat2w,bat2h)
		ball(ballx,bally,ballr)
		
		
		y1_change = 0
		y2_change = 0

		pygame.display.update()
		pygame.display.flip()



gameLoop()

pygame.quit()
quit()
