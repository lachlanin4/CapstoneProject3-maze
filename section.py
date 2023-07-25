"""
This is the class that encapsulates a section of the maze.
Although each section is different this includes some
common aspects that apply to any of them. Such common
aspects include name, height and width, x and y position within
the maze (based upon the bottom left hand corner of the
section), orientation (0, 90, 180, 270 degrees clockwise),
What other section its linkage passages connect to
(although this can vary) and an indication of whether the
player can navigate through any given linkage/access point.
Not all access points might be available all of the time.
"""

class Section:
    def __init__(self):
        pass