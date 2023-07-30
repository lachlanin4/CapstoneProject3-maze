#maze class needs to have attributes of width, height, maze layout, start and exit position
#needs to have methods to generate and display the maze and check if player has reached exit
import pygame

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


    

