##Game entity will be a class that has attributes of x and y coordinates and a symbol(character representation)
#The classes that will inherit GameEntity are Player, Wall and Exit, each of these classes need their own attributes and behviours/methods
#Player needs to allow movement and track where the player is within the maze
#Wall needs to block the players path and not let them move through it
#Exit needs to tell the player that they have won
import pygame

ORCHID = (218,112,214) #A colour

class Game_Entity(pygame.sprite.Sprite):
    #entity_group =pygame.sprite.Group()
    def __init__(self):
        super().__init__()
        self.x=None
        self.y=None
        self.symbol=None ######Need to add this one
        self.all_entities_group =pygame.sprite.Group()
    def add_new_entity(self,entity):
        self.all_entities_group.add(entity)
    
    def draw_entities(self):
         for entity in self.all_entities_group:
              #screen.blit(entity.surf,entity.rect) #if this doesn't work try draw.rects
              pass
             

class Player(Game_Entity):
     #allow movement and track where player is
     pass

class Wall(Game_Entity):
     #Block player's path
    def __init__(self,x,y,width,height):
        super().__init__()
        self.x = x #Shouldn't need this should use the xy from the Game_Entity class
        self.y = y
        self.width = width
        self.height = height
        #self.wall = pygame.draw.rect(screen,ORCHID,(self.x,self.y,self.width,self.height)) #should this be a method instead?
        self.walls_group = pygame.sprite.Group()


    def add_wall(self):
        new_wall = pygame.draw.rect(screen,ORCHID,(self.x,self.y,self.width,self.height))
        self.walls_group.add(new_wall) #To make sure this gets drawn on do I need to display.update()?
        self.all_entities_group.add(new_wall)
        #ADDWALL =pygame.USEREVENT +1 #Pygame internally defines events as integers and the last one is USERVENT, so +1 to that will make the event number unique

    #Add methods to add vertical walls and horizontal walls
        pass

class Exit(Game_Entity):
     #Tell player they have won
     #Add method to tell player they have won - when their sprites collide player has won
     pass
#player=Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
# walls = pygame.sprite.Group()
# all_sprites = pygame.sprite.Group()
# all_sprites.add(player)

# Create a custom event for adding a new enemy
#pygame defines events internally as integers, so you need to define a new event with a unique integer. The last event pygame reserves is called USEREVENT, so defining ADDENEMY = pygame.USEREVENT + 1
# ADDWALL = pygame.USEREVENT + 1
# pygame.time.set_timer(ADDENEMY, 250)

# Add a new enemy?
        # elif event.type == ADDWALL:
        #     # Create the new enemy and add it to sprite groups
        #     new_enemy = Enemy()
        #     enemies.add(new_enemy)
        #     all_sprites.add(new_enemy)

# Check if any enemies have collided with the player
if pygame.sprite.spritecollideany(player, walls):
    # If so, then remove the player and stop the loop
    player.kill()
    running = False
#spritecollideany checks if the rects of the two parameters have intersected so has the player sprite intersected with anything in the walls spritegroup?

#When you call kill() you a remmove a sprite from every group it is in and removes references to the sprite as well
#draw all sprites:
for entity in all_sprites:
    screen.blit(entity.sruf,entity.rect)

pygame.display.flip()