"""
This is the class that encapsulates a room in the maze.
It can have upto four access points. Interesting things
might happen here.
"""

from section import Section


class Room(Section):
    def __init__(self, name: str):
        super().__init__(name)
        pass
