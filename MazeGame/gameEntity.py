##Game entity will be a class that has attributes of x and y coordinates and a symbol(character representation)
#The classes that will inherit GameEntity are Player, Wall and Exit, each of these classes need their own attributes and behviours/methods
#Player needs to allow movement and track where the player is within the maze
#Wall needs to block the players path and not let them move through it
#Exit needs to tell the player that they have won
import pygame
pygame.init()
#from gameEngine import screen

PINK = (255,192,203)   
ORCHID = (218,112,214) #A colour

SCREEN_WIDTH=800
SCREEN_HEIGHT=600

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill((133,123,200)) #Fill the screen first because it will fill over everything else

#maze class needs to have attributes of width, height, maze layout, start and exit position
#needs to have methods to generate and display the maze and check if player has reached exit

all_entities_group =pygame.sprite.Group()

class Game_Entity(pygame.sprite.Sprite):
    #entity_group =pygame.sprite.Group()
    def __init__(self):
        super().__init__()
        #Maybe add self.surf =pygame.Surface(width,height) to create everything as sprites
        self.x=None
        self.y=None
        self.symbol=None ######Need to add this one
        #self.all_entities_group =pygame.sprite.Group()
    def add_new_entity(self):
        all_entities_group.add(self)
    
    def draw_entities(self): #This would be useful if there was more entites than walls such as locked doors n stuff but as it's just a maze so far only display maze function would really be necessary and that would be in maze class
         for entity in self.all_entities_group:
              screen.blit(entity.surf,entity.rect) #if this doesn't work try draw.rects
              pass
             

class Player(Game_Entity):
     #allow movement and track where player is
    def __init__(self,x,y,width,height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height= height
        self.moves = 0
        self.surf = pygame.Surface((self.width,self.height))
        self.rect = self.surf.get_rect(topleft=(self.x,self.y))

    def draw_player(self):
        #pygame.draw.rect(screen,PINK,(self.x,self.y,self.width,self.height))
        #print(self.y)
        self.rect=self.surf.get_rect(topleft=(self.x,self.y))
        screen.blit(self.surf, self.rect)

    

walls_group = pygame.sprite.Group()

class Wall(Game_Entity):
     #Block player's path
    def __init__(self,x,y,width,height):
        super().__init__()
        self.x = x #Shouldn't need this should use the xy from the Game_Entity class
        self.y = y
        self.width = width
        self.height = height
        self.surf = pygame.Surface((self.width,self.height))
        self.rect = self.surf.get_rect(topleft=(self.x,self.y))
        #self.wall = pygame.draw.rect(screen,ORCHID,(self.x,self.y,self.width,self.height)) #should this be a method instead?
        #self.walls_group = pygame.sprite.Group()


    def add_wall(self):
        #new_wall = pygame.draw.rect(screen,ORCHID,(self.x,self.y,self.width,self.height))
        #new_wall
        #new_wall=pygame.Surface((self.width,self.height))

        screen.blit(self.surf, self.rect)
        walls_group.add(self) #Does self in parameters add this Wall() to sprite group
        #To make sure this gets drawn on do I need to display.update()?
        Game_Entity.add_new_entity(self) #Does this add to game entites?
        #ADDWALL =pygame.USEREVENT +1 #Pygame internally defines events as integers and the last one is USERVENT, so +1 to that will make the event number unique

    #Add methods to add vertical walls and horizontal walls
        
exit_group = pygame.sprite.Group()
class Exit(Game_Entity):
     #Tell player they have won
     #Add method to tell player they have won - when their sprites collide player has won
    def __init__(self,x,y,width,height):
        super().__init__()
        self.x = x
        self.y=y
        self.width=width
        self.height=height
        self.surf = pygame.Surface((self.width,self.height))
        self.rect = self.surf.get_rect(topleft=(self.x,self.y))

    def add_exit(self):
        #self.rect=self.surf.get_rect(topleft=(self.x,self.y))
        screen.blit(self.surf, self.rect)
        exit_group.add(self)
        Game_Entity.add_new_entity(self)

key_group = pygame.sprite.Group()
class Key(Game_Entity):
     #Tell player they have won
     #Add method to tell player they have won - when their sprites collide player has won
    def __init__(self,x,y,width,height):
        super().__init__()
        self.x = x
        self.y=y
        self.width=width
        self.height=height
        self.surf = pygame.Surface((self.width,self.height))
        self.rect = self.surf.get_rect(topleft=(self.x,self.y))

    def add_key(self):
        #self.rect=self.surf.get_rect(topleft=(self.x,self.y))
        screen.blit(self.surf, self.rect)
        key_group.add(self)
        Game_Entity.add_new_entity(self)





class Maze():
    #considering putting some attributes here if they can be shared by all the instances/mazes
    #start_position=(0,0)
    #exit_position=(end,end)
    def __init__(self,width,height):
        self.width = width #instance attributes #These are unused need to integrate them into the Wall callings
        self.height = height
        self.start_position = None
        self.exit_position = None #need to make exit sprite a rect
        self.layout = []

        #method to generate maze
    def add_maze1(self):
        #Generate maze outline
        Wall(0,0,SCREEN_WIDTH,5).add_wall() #top wall
        Wall(0,0,5,SCREEN_HEIGHT).add_wall() #left wall
        Wall(0,SCREEN_HEIGHT-5,SCREEN_WIDTH,5).add_wall() #
        Wall(SCREEN_WIDTH-5,0,5,SCREEN_HEIGHT).add_wall()

        #Horizontal Wall
        Wall(60,540,760,5).add_wall()
        Wall(0,540-60,600,5).add_wall()
        #Wall()
    def add_maze2(self):
        #Generate maze outline
        Wall(0,0,SCREEN_WIDTH,5).add_wall() #top wall
        Wall(0,0,5,SCREEN_HEIGHT).add_wall() #left wall
        Wall(0,SCREEN_HEIGHT-5,SCREEN_WIDTH,5).add_wall() #
        Wall(SCREEN_WIDTH-5,0,5,SCREEN_HEIGHT).add_wall()

        #Horizontal Walls, have a gap of 60 between their y's
        Wall(0,SCREEN_HEIGHT-60,120,5).add_wall()
        Wall(180,SCREEN_HEIGHT-60,300,5).add_wall()
        Wall(550,SCREEN_HEIGHT-60,300,5).add_wall()

        Wall(60,SCREEN_HEIGHT-120,100,5).add_wall()
        Wall(240,SCREEN_HEIGHT-120,120,5).add_wall()
        Wall(390,SCREEN_HEIGHT-120,200,5).add_wall()
        Wall(640,SCREEN_HEIGHT-120,(800-640-5),5).add_wall()

        Wall(50,SCREEN_HEIGHT-180,500,5).add_wall()
        Wall(590,SCREEN_HEIGHT-180,120,5).add_wall()


        Wall(40,SCREEN_HEIGHT-240,300,5).add_wall()
        Wall(390,SCREEN_HEIGHT-240,300,5).add_wall()
        Wall(730,SCREEN_HEIGHT-240,30,5).add_wall()

        #Vertical Walls
        Wall(680,SCREEN_HEIGHT-120,5,60).add_wall()
        Wall(270,SCREEN_HEIGHT-120,5,60).add_wall()

        Wall(550,SCREEN_HEIGHT-180,5,65).add_wall()
        Wall(700,SCREEN_HEIGHT-180,5,65).add_wall()

    def add_maze3(self):
        #Generate maze outline
        Wall(0,0,SCREEN_WIDTH,5).add_wall() #top wall
        Wall(0,0,5,SCREEN_HEIGHT).add_wall() #left wall
        Wall(0,SCREEN_HEIGHT-5,SCREEN_WIDTH,5).add_wall() #
        Wall(SCREEN_WIDTH-5,0,5,SCREEN_HEIGHT).add_wall()

        #Horizontal Walls, have a gap of 60 between their y's
        Wall(70,SCREEN_HEIGHT-60,120,5).add_wall()
        Wall(260,SCREEN_HEIGHT-60,200,5).add_wall()
        Wall(500,SCREEN_HEIGHT-60,175,5).add_wall()
        Wall(725,SCREEN_HEIGHT-60,30,5).add_wall()

        Wall(0,SCREEN_HEIGHT-120,50,5).add_wall()
        Wall(90,SCREEN_HEIGHT-120,400,5).add_wall()
        Wall(535,SCREEN_HEIGHT-120,200,5).add_wall()

        Wall(0,SCREEN_HEIGHT-180,10,5).add_wall()
        Wall(110,SCREEN_HEIGHT-180,70,5).add_wall()
        Wall(219,SCREEN_HEIGHT-180,83,5).add_wall()
        Wall(340,SCREEN_HEIGHT-180,200,5).add_wall()
        Wall(580,SCREEN_HEIGHT-180,300,5).add_wall()

        Wall(45,SCREEN_HEIGHT-240,100,5).add_wall()
        Wall(180,SCREEN_HEIGHT-240,321,5).add_wall()
        Wall(360,SCREEN_HEIGHT-240,350,5).add_wall()
        Wall(750,SCREEN_HEIGHT-240,100,5).add_wall()

        Wall(43,SCREEN_HEIGHT-300,120,5).add_wall()
        Wall(213,SCREEN_HEIGHT-300,291,5).add_wall()
        Wall(541,SCREEN_HEIGHT-300,10,5).add_wall()
        Wall(589,SCREEN_HEIGHT-300,12,5).add_wall()
        Wall(640,SCREEN_HEIGHT-300,40,5).add_wall()
        Wall(720,SCREEN_HEIGHT-300,10,5).add_wall()
        Wall(768,SCREEN_HEIGHT-300,50,5).add_wall()

        Wall(20,SCREEN_HEIGHT-360,100,5).add_wall()
        Wall(159,SCREEN_HEIGHT-360,38,5).add_wall()
        Wall(236,SCREEN_HEIGHT-360,56,5).add_wall()
        Wall(332,SCREEN_HEIGHT-360,108,5).add_wall()
        Wall(480,SCREEN_HEIGHT-360,10,5).add_wall()
        Wall(530,SCREEN_HEIGHT-360,50,5).add_wall()
        Wall(619,SCREEN_HEIGHT-360,137,5).add_wall()


        #Vertical Walls
        Wall(320,SCREEN_HEIGHT-120,5,60).add_wall()

        Wall(450,SCREEN_HEIGHT-180,5,60).add_wall()





    


        #method to display maze
        #This will be lots of Wall(x,y,width,height).add_wall() instances

        #method to check player has react exit
    def player_reached_exit(self,playerRect,exitRect):
        # if pygame.sprite.collide_rect(playerRect,exitRect):
        #     print("You have won!")
        #     print("Do you want to quit or play again?")
        pass
