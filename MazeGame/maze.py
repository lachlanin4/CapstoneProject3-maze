#import and initliase pygame
import pygame
pygame.init()

#set up drawing window
screen = pygame.display.set_mode([500,500])

#run until user asks to quit
running=True
while running:
    #did user click close button
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    #Change background colour
    screen.fill((255,255,255))

    #Draw solid blue circle in center
    #parameters are where to draw it(screen), colour,center coordinates of circle, radius in pixels
    pygame.draw.circle(screen,(0,0,255),(250,250),75)

    #Flip the display, what we've done so far doesn't display if we dont't flip
    #Updates contents of display to screen. nothing happens without his
    pygame.display.flip()

#exits pygame after loop
pygame.quit()