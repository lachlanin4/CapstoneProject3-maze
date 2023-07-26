"""
This is the class that encapsulates a tee junction in the maze.
It has three access points and can be orientated to represent
left or right hand. Its shaped like the letter 'T'.
"""

from section import Section


class Tee(Section):
    def __init__(self, name: str):
        super().__init__(name)
        pass
