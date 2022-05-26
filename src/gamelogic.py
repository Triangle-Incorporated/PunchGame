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

class HealthBar() :
    """ Health bars """

    def __init__(self, health, is_right) :
        # Health bar rectangles display
        left_coord = 450 if is_right else 30
        self.outer = pygame.Rect(left_coord, 10, (3.10 * health), 25)
        self.inner = pygame.Rect(left_coord + 2, 12, (3.06 * health), 21)
        self.health = health

    def update(self, health) :
        """ Update health """
        self.health = health
        self.inner.width = 3.06 * self.health
    
    def draw(self, screen) :
        """ Draw health bar """
        pygame.draw.rect(screen, (0, 0, 0), self.outer)
        pygame.draw.rect(screen, (255, 0, 0), self.inner)


class Player(pygame.sprite.Sprite) :
    """ Player class """
    
    # Convert attacks to damage and ranges
    damage_table = { "upb" : 12, "downb" : 8, "ntrlb" : 10 }
    range_table = { "upb" : 60, "downb" : 120, "ntrlb" : 90 }
    cooldown_table = { "upb" : 10, "downb" : 6, "ntrlb" : 8 }
    texture_table = { 
                     "nml" : pygame.image.load("resource/whiterectangle.png"), 
                     "hurt" : pygame.image.load("resource/redrectangle.png"), 
                     "upb" : pygame.image.load("resource/bluerectangle.png"), 
                     "downb" : pygame.image.load("resource/greenrectangle.png"), 
                     "ntrlb" : pygame.image.load("resource/purplerectangle.png") 
                    }

    def __init__(self, health, is_right) :
        print("New player")
        super().__init__()
        
        self.image = Player.texture_table["nml"]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(600 if is_right else 100, 240) # Set y to 250 to put character on the bottom of the screen
        self.direction = -1
        self.health = health
        self.health_bar = HealthBar(health, is_right)
        self.vel_x = 0
        self.cooldown = 0

    def set_vel(self, new) :
        """ Update velocity and direction """
        self.vel_x = new
        self.direction = 1 if self.vel_x > 0 else (-1 if self.vel_x < 0 else self.direction)
        # Do nothing to direction if velocity is zero

    def set_health(self, dmg) :
        """ Update health """
        self.cooldown = 6
        self.image = Player.texture_table["hurt"]
        self.health -= dmg
    
    def update(self) :
        """ Change sprite's position """
        pygame.sprite.Sprite.update(self)
        self.rect = self.rect.move(self.vel_x, 0)
        self.health_bar.update(self.health)
        if self.cooldown > 0 :
            self.cooldown -= 1
        else :
            self.image = Player.texture_table["nml"]


    def draw(self, screen) :
        """ Draw the sprite """
        screen.blit(self.image, self.rect)
        self.health_bar.draw(screen)
    
    def punch(self, other, type):
        """ THERE'S A REASON IT'S CALLED PUNCHGAME """
        # Set punch cooldown
        if self.cooldown == 0 :
            self.cooldown = Player.cooldown_table[type]
        else :
            return
        
        # Hard collision detection
        xpos = self.rect.x if self.direction == -1 else self.rect.x + self.rect.width

        self.image = Player.texture_table[type]
        
        hurt_line = (xpos, self.rect.y + 10, xpos + Player.range_table[type] * self.direction, self.rect.y)
        if other.rect.clipline(hurt_line) :
            print("HIT!!")
            other.set_health(Player.damage_table[type])
            return
        print("MISS!")


def gameLoop() :
    """ The main game loop! """
    global ioevents
    destGui()
    running = True
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Punch Game!")
    background = pygame.image.load("resource/mortal.png")
    player = Player(100, True)
    enemy = Player(90, False)

    # Main game loop
    while running :
        ioevents = []
        checkInputs()
        ledOutput(player.health)
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        clock.tick(24)

        is_action = False # replit only
        for event in pygame.event.get() :
            
            if event.type == pygame.QUIT :
                running = False
#/////// THIS CODE IS FOR USING PYGAME WITHOUT A CONTROLLER /////////
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
#/////// END OF CODE FOR USING PYGAME WITHOUT A CONTROLLER /////////

        # Handle events
        for event in ioevents :
            if event == "sright" :
                player.set_vel(10)
            elif event == "lright" :
                player.set_vel(15)
            elif event == "sleft" :
                player.set_vel(-10)
            elif event == "lleft" :
                player.set_vel(-15)
            elif event == "upb" :
                player.punch(enemy, event)
            elif event == "downb" :
                player.punch(enemy, event)
            elif event == "ntrlb" :
                player.punch(enemy, event)
            else :
                player.set_vel(0)


        
        # Redraw sprites
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

