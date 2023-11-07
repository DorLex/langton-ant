from enum import Enum

WIDTH = 1024
HEIGHT = 1024

ANT_X_START = 512
ANT_Y_START = 512


class AntDirection(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Color(Enum):
    WHITE = 255
    BLACK = 0
