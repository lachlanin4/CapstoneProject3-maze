##Game entity will be ac lass that has attributes of x and y coordinates and a symbol(character representation)
#The classes that will inherit GameEntity are Player, Wall and Exit, each of these classes need their own attributes and behviours/methods
#Player needs to allow movement and track where the player is within the maze
#Wall needs to block the players path and not let them move through it
#Exit needs to tell the player that they have won

player=Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
walls = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Create a custom event for adding a new enemy
#pygame defines events internally as integers, so you need to define a new event with a unique integer. The last event pygame reserves is called USEREVENT, so defining ADDENEMY = pygame.USEREVENT + 1
ADDWALL = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

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