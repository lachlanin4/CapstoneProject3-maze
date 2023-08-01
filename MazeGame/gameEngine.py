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
    K_y
)

from gameEntity import Game_Entity, Player, Wall,Exit, all_entities_group, walls_group,Maze,exit_group
from gameEntity import locked_door_group,Locked_Door,Button,button_group

class Game_Engine:
    def __init__(self) -> None:
        pass

    def handling_user_input(self):
        for event in pygame.event.get():
            if event.type ==KEYDOWN:
                if event.key ==K_UP:
                    player.y -= 20
                    player.moves +=1
                if event.key ==K_DOWN:
                    player.y +=20
                    player.moves +=1
                if event.key ==K_RIGHT:
                    player.x +=20
                    player.moves +=1
                if event.key ==K_LEFT:
                    player.x -=40
                    player.moves +=1
                if event.key==K_ESCAPE:
                    running=False
            elif event.type==QUIT:
                running =False
    
    def hit_wall_text(self):
        text = myfont.render('You lost! You hit a wall.', True, PINK, ORCHID)
        textRect = text.get_rect(center =(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        text1 = myfont.render('Press Y if you want to play again', True, PINK, ORCHID)
        text1Rect = text1.get_rect(center =(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2)+50))
        screen.blit(text1, text1Rect)
        text2 = myfont.render('Press Esc or close window to Quit', True, PINK, ORCHID)
        text2Rect = text2.get_rect(center =(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2)+100))
        screen.blit(text2, text2Rect)
        pygame.display.flip()
        time.sleep(0.5)

    def beat_level_text(self):
        text = myfont.render((f'You beat this level!In {player.moves}moves!'), True, PINK, ORCHID)
        textRect = text.get_rect(center =(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        text1 = myfont.render('Press Y to play the next level', True, PINK, ORCHID)
        text1Rect = text1.get_rect(center =(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2)+50))
        screen.blit(text1, text1Rect)
        text2 = myfont.render('Press Esc or close window to Quit', True, PINK, ORCHID)
        text2Rect = text2.get_rect(center =(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2)+100))
        screen.blit(text2, text2Rect)
        pygame.display.flip()
        time.sleep(0.5)
    
    def beat_final_level_text(self):
        text = myfont.render((f'You beat this level!In {player.moves}moves!'), True, PINK, ORCHID)
        textRect = text.get_rect(center =(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        text1 = myfont.render('Press Y to play from the beginning', True, PINK, ORCHID)
        text1Rect = text1.get_rect(center =(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2)+50))
        screen.blit(text1, text1Rect)
        text2 = myfont.render('Press Esc or close window to Quit', True, PINK, ORCHID)
        text2Rect = text2.get_rect(center =(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2)+100))
        screen.blit(text2, text2Rect)
        pygame.display.flip()
        time.sleep(0.5)

    def hit_locked_door_text(self):
        text = myfont.render('You shall not pass! (unless you press the button)', True, PINK, ORCHID)
        textRect = text.get_rect(center =(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(text, textRect)
        text1 = myfont.render('Press Y if you want to play this level again', True, PINK, ORCHID)
        text1Rect = text1.get_rect(center =(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2)+50))
        screen.blit(text1, text1Rect)
        text2 = myfont.render('Press Esc or close window to Quit', True, PINK, ORCHID)
        text2Rect = text2.get_rect(center =(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2)+100))
        screen.blit(text2, text2Rect)
        pygame.display.flip()
        time.sleep(0.5)


PINK = (255,192,203)   
SCREEN_WIDTH=800
SCREEN_HEIGHT=600

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill((133,123,200)) #Fill the screen first because it will fill over everything else

PLAYER_X =700
PLAYER_Y=550
PLAYER_HEIGHT = 40
PLAYER_WIDTH= 40

#font=pygame.font.Font

player = Player(PLAYER_X,PLAYER_Y,40,40)
#font = pygame.font.Font(get_default_font(),32)
myfont = pygame.font.SysFont(None,50)
moves = 0
pressed_button = False

running =True
while running:
    Game_Engine().handling_user_input()
    
    screen.fill((133,123,200))
    player.draw_player()
    Exit(SCREEN_WIDTH-50,SCREEN_HEIGHT-130,40,40).add_exit()
    Maze(SCREEN_WIDTH,SCREEN_HEIGHT).add_maze1()
    Button(750,SCREEN_HEIGHT-30,20,20).add_button()
    Locked_Door(0,540,60,10).add_locked_door()
    Locked_Door(500,SCREEN_HEIGHT-60,10,60).add_locked_door()

    pygame.display.update()
    if pygame.sprite.spritecollideany(player,walls_group): #After moving checks if player and walls have collided and if so ends games
        player.kill()
        Game_Engine().hit_wall_text()
        player.moves=0
        pressed_button=False
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key == K_y:
                    # text = myfont.render('Good Choice back to the start!', True, PINK, ORCHID) 
                    # textRect = text.get_rect(center =(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)) #Not sure how to get rid of all the text without lots of code
                    # screen.blit(text, textRect)
                    # pygame.display.flip()
                    # time.sleep(1)
                    player.y=550
                    player.x=700
                elif event.key ==K_ESCAPE:
                    running=False
            elif event.type==QUIT:
                running=False
    #If player reaches exit provide option to play again or exit, if play again by pressing y key loads next level
    if pygame.sprite.spritecollideany(player,exit_group):
        Game_Engine().beat_level_text()
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key == K_y:
                    #load maze 2
                    for sprite in walls_group:
                        sprite.kill()
                    for sprite in exit_group:
                        sprite.kill()
                    player.moves=0
                    #pressed_button=False #Would add this if any other levels had a button to press
                    screen.fill((133,123,200))
                    player.y=550
                    player.x=750
                    pygame.display.update()
                    while running:      
                        Game_Engine().handling_user_input()
                        screen.fill((152, 222, 222))
                        player.draw_player()
                        Exit(SCREEN_WIDTH-300,300,40,40).add_exit()
                        Maze(SCREEN_WIDTH,SCREEN_HEIGHT).add_maze2()
                        pygame.display.update()
                        if pygame.sprite.spritecollideany(player,walls_group): #After moving checks if player and walls have collided and if so ends games
                            player.kill()
                            Game_Engine().hit_wall_text()
                            player.moves=0
                            for event in pygame.event.get():
                                if event.type==KEYDOWN:
                                    if event.key == K_y:
                                        player.y=550
                                        player.x=750
                                    elif event.key ==K_ESCAPE:
                                        running=False
                                elif event.type==QUIT:
                                    running=False
                        #If player reaches exit provide option to play again or exit, if play again by pressing y key loads next level
                        if pygame.sprite.spritecollideany(player,exit_group):
                            Game_Engine().beat_level_text()
                            for event in pygame.event.get():
                                if event.type==KEYDOWN:
                                    if event.key == K_y:
                                        #load maze 3
                                        for sprite in walls_group:
                                            sprite.kill()
                                        for sprite in exit_group:
                                            sprite.kill()
                                        player.moves=0
                                        screen.fill((23, 166, 154))
                                        player.y=550
                                        player.x=750
                                        pygame.display.update()
                                        while running:
                                            Game_Engine().handling_user_input()
                                            screen.fill((23, 166, 154))
                                            player.draw_player()
                                            Exit(SCREEN_WIDTH-50,50,40,40).add_exit()
                                            Maze(SCREEN_WIDTH,SCREEN_HEIGHT).add_maze3()
                                            pygame.display.update()
                                            if pygame.sprite.spritecollideany(player,walls_group): #After moving checks if player and walls have collided and if so ends games
                                                player.kill()
                                                Game_Engine().hit_wall_text()
                                                player.moves=0
                                                for event in pygame.event.get():
                                                    if event.type==KEYDOWN:
                                                        if event.key == K_y:
                                                            player.y=550
                                                            player.x=750
                                                        elif event.key ==K_ESCAPE:
                                                            running=False
                                                    elif event.type==QUIT:
                                                        running=False
                                            #If player reaches exit provide option to play again or exit, if play again by pressing y key loads next level
                                            if pygame.sprite.spritecollideany(player,exit_group):
                                                Game_Engine().beat_final_level_text()
                                                for event in pygame.event.get():
                                                    if event.type==KEYDOWN:
                                                        if event.key == K_y:
                                                            #This will need to take them back to the beginning
                                                            for sprite in walls_group:
                                                                sprite.kill()
                                                            for sprite in exit_group:
                                                                sprite.kill()
                                                            player.moves=0
                                                            screen.fill((23, 166, 154))
                                                            player.y=550
                                                            player.x=750
                                                            ##The new level has not been generated yet i think add 1 more level then work on other things
                                                            pygame.display.update()
                                                        elif event.key ==K_ESCAPE:
                                                            running=False
                                                    elif event.type==QUIT:
                                                        running=False
                                    elif event.key ==K_ESCAPE:
                                        running=False
                                elif event.type==QUIT:
                                    running=False
    if pygame.sprite.spritecollideany(player,button_group):
        pressed_button =True
        # locked_door.colour = (133,123,200)
        # screen.blit(locked_door.surf, locked_door.rect)
        # pygame.display.update()
        
    if pygame.sprite.spritecollideany(player,locked_door_group):
        if pressed_button==True:
            pass
        elif pressed_button==False:
            player.kill()
            #Rendering text if you lose
            Game_Engine().hit_locked_door_text()
            player.moves=0
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key == K_y:
                        player.y=550
                        player.x=700
                    elif event.key ==K_ESCAPE:
                        running=False
                elif event.type==QUIT:
                    running=False


 