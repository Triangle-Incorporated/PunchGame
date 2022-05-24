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

class Player(pygame.sprite.Sprite) :
    """ Player class """
    
    def __init__(self, health, file_path) :
        print("New player")
        super().__init__()
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect()
        
        self.health = health
        self.vel_x = 0

    def update(self) :
        """ Change sprite's position """
        pygame.sprite.Sprite.update(self)
        self.rect.move(self.vel_x, 0)

    def draw(self, screen) :
        """ Draw the sprite """
        screen.blit(self.image, self.rect)        
    
    def punch(self, other):
        """ THERE'S A REASON IT'S CALLED PUNCHGAME """
        if self.rect.x >= other.rect.x and self.rect.x <= other.rect.x + 30:
            other.health -= 10
            
def gameLoop() :
    """ The main game loop! """
    global ioevents
    destGui()
    running = True
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Punch Game!")
    background = pygame.image.load("resource/mortal.png")
    player = Player(100, "resource/whiterectangle.png")
    enemy = Player(90, "resource/whiterectangle.png")
    enemy.punch(    player)

    # Main game loop
    while running :
        checkInputs()
        ioevents = []
        ledOutput(player.health)
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        clock.tick(24)

        # replit only:
        is_action = False
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
            print(keys)
            if keys[pygame.K_UP] :
                ioevents.append("upb")
                print("up")
            elif keys[pygame.K_DOWN] :
                ioevents.append("downb")
                print("down")
            else :
                ioevents.append("ntrlb")
#////////////// TEMPORARY FOR USE ON REPLIT /////////////////////////

        # Handle events
        for event in ioevents :
            print(event)
            if event == "lleft" :
                player.vel_x = -5
            elif event == "lright" :
                print("right")
                player.vel_x = -10 
            elif event == "sleft" :
                player.vel_x = 5
            elif event == "lleft" :
                player.vel_x = 10
            else :
                continue
                
        player.update()
        enemy.update()
        player.draw(screen)
        enemy.draw(screen)
        
        pygame.display.update()

    # Close game loop
    trackEvents = False
    pygame.display.set_mode((1,1))
    initGui()

