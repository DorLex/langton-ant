import numpy as np

from .enums.color import Color


class Grid:
    def __init__(self, width, height, color, dtype):
        self.width = width
        self.height = height
        self.color = color
        self.dtype = dtype

        self.grid_array = np.full((self.width, self.height), self.color, self.dtype)

        self.black_cell_count = 0

    def change_color_to_black(self, x, y):
        self.grid_array[y, x] = Color.BLACK.value

    def change_color_to_white(self, x, y):
        self.grid_array[y, x] = Color.WHITE.value
