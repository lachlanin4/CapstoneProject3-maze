"""
This is the class that encapsulates a component part of the
game that is displayed. It is a base class that all other
displayed game components inherit from. It incorporates
common aspects that apply to any of them. Such common
aspects include name, height and width, x and y position within
the maze. Derived classes might overload, constrain or overload
these aspects as required.
"""


class GameEntity:
    def __init__(
        self,
        name: str,
        start_x: int = 0,
        start_y: int = 0,
        height: int = 1,
        width: int = 1,
    ):
        self._name = name
        self._start_x = start_x
        self._start_y = start_y
        self._height = height
        self._width = width
        self._current_x = start_x
        self._current_y = start_y

    @property
    def name(self):
        return self._name

    @property
    def start_x(self):
        return self._start_x

    @property
    def start_y(self):
        return self._start_y

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @property
    def current_x(self):
        return self._current_x

    @property
    def current_y(self):
        return self._current_y

    @start_x.setter
    def start_x(self, start_x: int):
        self._start_x = start_x

    @start_y.setter
    def start_y(self, start_y: int):
        self._start_y = start_y

    @height.setter
    def height(self, height: int):
        self._start_x = height

    @width.setter
    def width(self, width: int):
        self._width = width

    @current_x.setter
    def current_x(self, current_x: int):
        self._current_x = current_x

    @current_y.setter
    def current_y(self, current_y: int):
        self._current_y = current_y
