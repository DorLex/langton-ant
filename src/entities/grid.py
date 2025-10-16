from typing import TypeAlias

import numpy as np

from src.enums.color import Color


class Grid:
    def __init__(self, width: int, height: int, color: int, dtype: TypeAlias) -> None:
        self.width = width
        self.height = height
        self.color = color
        self.dtype = dtype

        self.grid_array: np.ndarray = np.full((self.width, self.height), self.color, self.dtype)

        self.black_cell_count: int = 0

    def change_color_to_black(self, x: int, y: int) -> None:
        self.grid_array[y, x] = Color.BLACK

    def change_color_to_white(self, x: int, y: int) -> None:
        self.grid_array[y, x] = Color.WHITE
