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
        self.exit_position = None
        self.layout = None

PINK = (255,192,203)   
SCREEN_WIDTH=800
SCREEN_HEIGHT=600

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill((133,123,200)) #Fill the screen first because it will fill over everything else

PLAYER_X =50
PLAYER_Y=50
PLAYER_HEIGHT = 50
PLAYER_WIDTH= 50

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
                print("UP")
                #t1Rect.move_ip(0,-5)
                #pygame.display.update()
                PLAYER_Y -= 10
            if event.key==K_ESCAPE:
                running=False
        elif event.type==QUIT:
            running =False
    
    screen.fill((133,123,200))
    pygame.draw.rect(screen,PINK,(PLAYER_X,PLAYER_Y,PLAYER_WIDTH,PLAYER_HEIGHT))
    pygame.display.update()
