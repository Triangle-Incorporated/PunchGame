# Handle Game

import pygame
from display import initGui, destGui

print("Game logic works")

# Array to store io events
ioevents = []
trackEvents = True

# Window size
width = 800
height = 450

pygame.init()
clock = pygame.time.Clock()

from handleio import checkInputs, ledOutput

def gameLoop() :
	""" The main game loop! """
	global ioevents
	destGui()
	running = True
	p1Health = 100
	
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Punch Game!")
	background = pygame.image.load("resource/mortal.png")

	# Main game loop
	while running :
		checkInputs()
		print(ioevents)
		ioevents = []
		ledOutput(p1Health)
		screen.fill((255, 255, 255))
		screen.blit(background, (0, 0))
		clock.tick(24)

		for event in pygame.event.get() :
			
			if event.type == pygame.QUIT :
				running = False
#/////// THIS CODE IS FOR USING PYGAME WITHOUT A CONTROLLER /////////
#////////////// TEMPORARY FOR USE ON REPLIT /////////////////////////
			is_action = False
			button_buff = []
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_LEFT :
					ioevents.append("lleft")
				elif event.key == pygame.K_RIGHT :
					ioevents.append("lright")
				elif event.key == pygame.K_SPACE :
					is_action = True

			elif event.type == pygame.KEYUP :
				ioevents.append("nop")

		if is_action :
			keys = pygame.key.get_pressed()
			if keys[pygame.K_UP] :
				ioevents.append("upb")
			elif keys[pygame.K_DOWN] :
				ioevents.append("downb")
			else :
				ioevents.append("ntrlb")
#////////////// TEMPORARY FOR USE ON REPLIT /////////////////////////

		# Handle events

		pygame.display.update()

	# Close game loop
	trackEvents = False
	pygame.display.set_mode((1,1))
	initGui()

