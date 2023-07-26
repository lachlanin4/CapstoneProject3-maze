"""
This is the class that encapsulates a corner in the maze.
Its like a passage but with a bend in it. Changing the
orientation will allow it to represent any corner. Its
size is nominal to just handle the corners.
"""

from section import Section


class Corner(Section):
    def __init__(self, name: str):
        super().__init__(name)
        pass
