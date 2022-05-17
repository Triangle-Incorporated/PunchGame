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
	destGui()
	running = True

	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Punch Game!")
	background = pygame.image.load("resource/mortal.png")

	# Main game loop
	while running :
		checkInputs()
		screen.fill((255, 255, 255))
		screen.blit(background, (0, 0))
		clock.tick(24)

		for event in pygame.event.get() :
			
			if event.type == pygame.QUIT :
				running = False

		pygame.display.update()

	# Close game loop
	trackEvents = False
	pygame.display.set_mode((1,1))
	initGui()

