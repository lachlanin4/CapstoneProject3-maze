#maze class needs to have attributes of width, height, maze layout, start and exit position
#needs to have methods to generate and display the maze and check if player has reached exit
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
pygame.init()

class Maze:
    #considering putting some attributes here if they can be shared by all the instances/mazes
    #start_position=(0,0)
    #exit_position=(end,end)
    def __init__(self,width,height):
        self.width = width #instance attributes
        self.height = height
        self.start_position = None
        self.exit_position = None #need to make exit sprite a rect
        self.layout = None

        #method to generate maze

        #method to display maze

        #method to check player has react exit
    def player_reached_exit(self,playerRect,exitRect):
        # if pygame.sprite.collide_rect(playerRect,exitRect):
        #     print("You have won!")
        #     print("Do you want to quit or play again?")
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
    

