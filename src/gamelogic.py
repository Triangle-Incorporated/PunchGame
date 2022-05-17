# Handle Game

import pygame
from display import initGui, destGui

print("Game logic works")

# Array to store io events
ioevents = []
trackEvents = True

from handleio import checkInputs, ledOutput

def gameLoop() :
	""" The main game loop! """
	pygame.init()
	destGui()
	
	screen = pygame.display.set_mode((800, 508))
	pygame.display.set_caption("Punch Game!")
	background = pygame.image.load("resource/mortalKombat.webp")
	
	running = True

	# Main game loop
	while running :
		checkInputs()
		screen.fill("white")
		screen.blit(background, (0, 0))
		


		pygame.display.update()

	# Close game loop
	initGui()
	trackEvents = False
