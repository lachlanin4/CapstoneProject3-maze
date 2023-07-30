#import pygame module
import pygame

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

#initlaise pygame
pygame.init()

class Player(pygame.sprite.Sprite): #Player is the child class of pygame.sprite.Sprite() class so it inherits all the attributes and methods
    def __init__ (self):
        super(Player, self).__init__()

#Define constansts for screen width and heihgt, not sure why I need to do this
SCREEN_WIDTH=800
SCREEN_HEIGHT=600

#Create screen object
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #This returns a surface with the specified dimensions, it will be the inside of the window and the OS controls the borders and title bar

#You can draw to the screen using a surface
#Asurface is a rectangular object on which you can draw

#make screen white
screen.fill((255,255,255))

#create a surface, passing in width and length
surf = pygame.Surface((50,50))

#give surf colour to differentiate from screen
surf.fill((0,0,0)) #filled with black
rect=surf.get_rect() #access underlying Rect using .get_rect and this is stored for later

#Need to use .blit() or .flip() to see what you have drawn on screen
#.blit stands for block transfer and it is copying the contents of one surface onto another
#you can only user blit from one surface to another

#Draw surf onto screen with blit
#surface to draw onto.blit(surface to be add),(x,y)
#putting the coordinates as half of screens dimensions attempts to center the blit
#but it won't s the coordinates will be the top left corner of the rectangle
#screen.blit(surf,(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
surf_center = (
    (SCREEN_WIDTH-surf.get_width())/2,
    (SCREEN_HEIGHT-surf.get_height())/2
)
#centered it properly with the above maths
screen.blit(surf, surf_center)
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
    #Look at every event in the queue
    for event in pygame.event.get():
        #did user hit a key?(KEYDOWN type)
        if event.type ==KEYDOWN:
            #if escape key, stop the loop
            if event.key==K_ESCAPE:
                running=False

        #did user click window close button, if so stop loop
        elif event.type==QUIT:
            running =False

