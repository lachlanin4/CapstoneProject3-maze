"""
This is the class that encapsulates the entry to the maze.
It has nominal size since it will go straight into another
section. Once you go into the maze via the entry you can't
exit back out via it - perhaps a portcullis drops down
behind you and locks you in! 
"""

from section import Section

class Entry(Section):

    def __init__(self):
        super().__init__()
        pass