#Game engine class will manage game flow and interactions
#will have methods for starting game, handling player input(so the arrow keys), update game state, check win lose conditions
#Game engine initalises maze and places game entities (player, walls and exit and displays inital state)
#process user input for player movement and update player's position accordingly. so the methods for moving up down and right etc will be in this class
#check for collison with wall or if reached exit displaying appropriate messages
#provide option to play again or quit
import pygame
import time
PINK = (255,192,203)   
ORCHID = (218,112,214)

pygame.init()
pygame.font.init()
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from gameEntity import Game_Entity, Player, Wall,Exit, all_entities_group, walls_group,Maze,exit_group

class Game_Engine:
    def __init__(self) -> None:
        pass

    pass


PINK = (255,192,203)   
SCREEN_WIDTH=800
SCREEN_HEIGHT=600

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill((133,123,200)) #Fill the screen first because it will fill over everything else

PLAYER_X =750
PLAYER_Y=550
PLAYER_HEIGHT = 40
PLAYER_WIDTH= 40

#font=pygame.font.Font

player = Player(PLAYER_X,PLAYER_Y,40,40)
#font = pygame.font.Font(get_default_font(),32)
myfont = pygame.font.SysFont(None,50)

running =True
while running:
    for event in pygame.event.get():
        if event.type ==KEYDOWN:
            if event.key ==K_UP:
                player.y -= 20
            if event.key ==K_DOWN:
                player.y +=20
            if event.key ==K_RIGHT:
                player.x +=10
            if event.key ==K_LEFT:
                player.x -=40
            if event.key==K_ESCAPE:
                running=False
        elif event.type==QUIT:
            running =False
    
    screen.fill((133,123,200))
    player.draw_player()
    Exit(SCREEN_WIDTH-50,SCREEN_HEIGHT-130,40,40).add_exit()
    Maze(SCREEN_WIDTH,SCREEN_HEIGHT).add_maze1()
    #Wall(70,70,700,10).add_wall() #Need to put this into maze class somehow
    #Game_Entity.draw_entities()
    #Keep player on screen
    # if Player(PLAYER_X,PLAYER_Y,40,40).draw_player().left < 0: #get this working with the stuff we've got now
    #     player.rect.left = 0
    # if player.rect.right > SCREEN_WIDTH:
    #     player.rect.right = SCREEN_WIDTH
    # if player.rect.top <= 0:
    #     player.rect.top = 0
    # if player.rect.bottom >= SCREEN_HEIGHT:
    #     player.rect.bottom = SCREEN_HEIGHT
    pygame.display.update()
    if pygame.sprite.spritecollideany(player,walls_group): #After moving checks if player and walls have collided and if so ends games
        print("You hit a wall! You have lost")
        player.kill()
        print("RIP")
        text = myfont.render('You lost! You hit a wall. Back to the start!', True, PINK, ORCHID)
        textRect = text.get_rect(center =(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        pygame.display.flip()
        time.sleep(0.5)
        #running=False
        player.y=550
        player.x=750
    if pygame.sprite.spritecollideany(player,exit_group):
        #print("You have won!")
        text = myfont.render('GeeksForGeeks', True, PINK, ORCHID)
        textRect = text.get_rect(topleft =(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        #textRect.center = 
        screen.blit(text, textRect)
 