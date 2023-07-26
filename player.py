"""
This is the class that encapsulates the player who is
navigating the maze. Each player has a name to start
with and a place within the maze. They navigate simply
forward, backwards, left and right to begin with.
"""

from gameentity import GameEntity

class Player(GameEntity):
    def __init__(self):
        super().__init__()
        pass
