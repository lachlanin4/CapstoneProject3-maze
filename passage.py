"""
This is the class that encapsulates a passage in the maze.
It only length since it will only attach to another perhaps
more complex section.
"""

from section import Section

class Passage(Section):

    def __init__(self):
        super().__init__()
        pass