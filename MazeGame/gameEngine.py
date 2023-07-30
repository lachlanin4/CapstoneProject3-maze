#Game engine class will manage game flow and interactions
#will have methods for starting game, handling player input(so the arrow keys), update game state, check win lose conditions
#Game engine initalises maze and places game entities (player, walls and exit and displays inital state)
#process user input for player movement and update player's position accordingly. so the methods for moving up down and right etc will be in this class
#check for collison with wall or if reached exit displaying appropriate messages
#provide option to play again or quit
import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#from gameEntity import Game_Entity, Player, Wall,Exit

class Game_Engine:
    pass


PINK = (255,192,203)   
SCREEN_WIDTH=800
SCREEN_HEIGHT=600

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill((133,123,200)) #Fill the screen first because it will fill over everything else

PLAYER_X =50
PLAYER_Y=50
PLAYER_HEIGHT = 40
PLAYER_WIDTH= 40

pygame.draw.rect(screen,PINK,(PLAYER_X,PLAYER_Y,PLAYER_WIDTH,PLAYER_HEIGHT))


# t1= pygame.Surface((50,50)) #Wanted to use this method with t1Rect.move_ip(x,y) but I could not get it working at all
# t1Rect=t1.get_rect()
# screen.blit(t1,t1Rect)
# pygame.display.flip()

running =True
while running:
    for event in pygame.event.get():
        if event.type ==KEYDOWN:
            if event.key ==K_UP:
                PLAYER_Y -= 10
            if event.key ==K_DOWN:
                PLAYER_Y +=10
            if event.key ==K_RIGHT:
                PLAYER_X +=10
            if event.key ==K_LEFT:
                PLAYER_X -=10
            if event.key==K_ESCAPE:
                running=False
        elif event.type==QUIT:
            running =False
    
    screen.fill((133,123,200))
    pygame.draw.rect(screen,PINK,(PLAYER_X,PLAYER_Y,PLAYER_WIDTH,PLAYER_HEIGHT))
    #Keep player on screen
    # if player.rect.left < 0:
    #     player.rect.left = 0
    # if player.rect.right > SCREEN_WIDTH:
    #     player.rect.right = SCREEN_WIDTH
    # if player.rect.top <= 0:
    #     player.rect.top = 0
    # if player.rect.bottom >= SCREEN_HEIGHT:
    #     player.rect.bottom = SCREEN_HEIGHT
    pygame.display.update()
    # if pygame.sprite.spritecollideany(player,walls_group): #After moving checks if player and walls have collided and if so ends games
    #     print("You have lost")
    #     player.kill()
    #     print("RIP")
    #     running=False