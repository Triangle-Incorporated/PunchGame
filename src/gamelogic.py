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
    
    # Convert attacks to damage and ranges
    damage_table = { "upb" : 12, "downb" : 8, "ntrlb" : 10 }
    range_table = { "upb" : 40, "downb" : 80, "ntrlb" : 60 }

    def __init__(self, health, img_path, is_player) :
        print("New player")
        super().__init__()
        self.image = pygame.image.load(img_path) # turn into a list of textures for animations
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(600 if is_player else 100, 240) # Set y to 250 to put character on the bottom of the screen
        
        self.health = health
        self.vel_x = 0

    def update(self) :
        """ Change sprite's position """
        pygame.sprite.Sprite.update(self)
        self.rect = self.rect.move(self.vel_x, 0)

    def draw(self, screen) :
        """ Draw the sprite """
        screen.blit(self.image, self.rect)        
    
    def punch(self, other, type):
        """ THERE'S A REASON IT'S CALLED PUNCHGAME """
        
        # Easy collision detection
        if self.rect.colliderect(other.rect) :
            other.health -= 10
            return

        # Hard collision detection
        direction = 1 if self.vel_x > 0 else -1
        xpos = self.rect.x if direction == -1 else self.rect.x + self.rect.width





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
    player = Player(100, "resource/whiterectangle.png", True)
    enemy = Player(90, "resource/whiterectangle.png", False)

    # Main game loop
    while running :
        checkInputs()
        ioevents = []
        ledOutput(player.health)
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        clock.tick(24)

        is_action = False # replit only
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
        for event in ioevents :
            if event == "sright" :
                player.vel_x = 10
            elif event == "lright" :
                player.vel_x = 15
            elif event == "sleft" :
                player.vel_x = -10
            elif event == "lleft" :
                player.vel_x = -15
            else :
                player.vel_x = 0


    
        player.update()
        enemy.update()
        player.draw(screen)
        enemy.draw(screen)
        
        pygame.display.update()

    # Close game loop
    trackEvents = False
    pygame.display.set_mode((1,1))
    print("Closing game loop")
    initGui()

