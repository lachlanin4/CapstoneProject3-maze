#import pygame module
import pygame
#import sys module
import sys

#import pygame.locals, these are constants.
#importing these means you can call them like K_UP instead of pygame.K_UP
#These are referencing keyboard keys, up down left right esc
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#Define constansts for screen width and heihgt, not sure why I need to do this
SCREEN_WIDTH=800
SCREEN_HEIGHT=600

#initlaise pygame
pygame.init()

# class Player(pygame.sprite.Sprite): #Player is the child class of pygame.sprite.Sprite() class so it inherits all the attributes and methods
#     def __init__ (self):
#         #super(Player, self).__init__() #This way of calling super() function is for older versions of python
#         super().__init__() #calls init method of sprite
#         #self.surf=pygame.Surface((75,25)) #The surface that will be drawn on screen is an attribute of 'player
#         #self.surf.fill((155,255,255)) #Made it black
#         #self.rect=self.surf.get_rect() #This is defining and initlasing .rect which will be used to draw the player later on

#     #Moves sprite based on arrow keys pressed
#     #move_ip stands for move in place
#     def update(self):
#         if event.key==K_UP:
#             player.rect.top +=5
#             print("Up")
#         if event.key==K_DOWN:
#             player.rect.move_ip(0,5)
#         if event.key==K_LEFT:
#             player.rect.move_ip(-5,0)
#         if event.key==K_RIGHT:
#             player.rect.move(5,0)

#Instantiate player
#player=Player()



#Create screen object
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #This returns a surface with the specified dimensions, it will be the inside of the window and the OS controls the borders and title bar

#You can draw to the screen using a surface
#Asurface is a rectangular object on which you can draw

#make screen white
screen.fill((0,0,0))

#create a surface, passing in width and length
#surf = pygame.Surface((50,50))

""""""
#Not using this line of code anymore
#give surf colour to differentiate from screen
#surf.fill((0,0,0)) #filled with white
""""""
#rect=surf.get_rect() #access underlying Rect using .get_rect and this is stored for later

#Need to use .blit() or .flip() to see what you have drawn on screen
#.blit stands for block transfer and it is copying the contents of one surface onto another
#you can only user blit from one surface to another

#Draw surf onto screen with blit
#surface to draw onto.blit(surface to be drawn on),(x,y)
#putting the coordinates as half of screens dimensions attempts to center the blit
#but it won't s the coordinates will be the top left corner of the rectangle
#screen.blit(surf,(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
# surf_center = (
#     (SCREEN_WIDTH-surf.get_width())/2,
#     (SCREEN_HEIGHT-surf.get_height())/2
# )
#centered it properly with the above maths
#screen.blit(surf, surf_center)
screen.blit(player.surf,(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
#screen.blit(player.surf,player.rect) #When you blit onto the player.rect it puts it a the top left corner of the display
#.flip updates the display with everything that's been drawn since last flip()
pygame.display.flip()

#sprite is a pircture
#pygame has a sprite class which can hold several graphical representations
#of any game object you want to display, to use it create a new class
#that extends Sprite which allows you to use built in methods

""""""






#to capture and process input use pygame event system
#all user input results in an event being generated
#all events put in an event queue
#code to handle events is called an event handler
#each event in pygrame has a type, the types focussed on in this will be keypresses and window closure
#keypresses has event type KEYDOWN and window closure type QUIT
#Access everything in event queue with pygame.event.get()
#Then loop through, inspect each event type and respond accordingly

#control variable to keep main loop running and be able to stop it

running=True

#Main loop
#Event Handler - runs through everything in event queue, if event queue empty it doesn't do anything
while running:
    #Tutorial told me to put this code here but if it doesn't work then put it above the event handler
#Returns dictionary of all the keys pressed at the beginning of every frame
    #pressed_keys =pygame.key.get_pressed() #returns a dictionary containg all the KEYDOWN events in the queue
            #update the player sprite after every frame based on keypresses
    #player.update(pressed_keys)
    #Look at every event in the queue
    for event in pygame.event.get():
        #print(pygame.event.get())
        #print(pygame.key.get_pressed())
        #did user hit a key?(KEYDOWN type)
        if event.type ==KEYDOWN:
            #print("A key pressed")
            #if escape key, stop the loop
            # if event.key==K_UP:
            #     player.rect.move_ip(0,-5)
            #     print("Up")
            # if event.key==K_DOWN:
            #     player.rect.move_ip(0,5)
            # if event.key==K_LEFT:
            #     player.rect.move_ip(-5,0)
            # if event.key==K_RIGHT:
            #     player.rect.move(5,0)
            player.update()
            if event.key==K_ESCAPE:
                running=False

        #did user click window close button, if so stop loop
        elif event.type==QUIT:
            running =False

    #pressed_keys =pygame.key.get_pressed() #returns a dictionary containg all the KEYDOWN events in the queue
            #update the player sprite after every frame based on keypresses
    #player.update(pressed_keys)

    

