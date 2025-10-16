from typing import TypeAlias

import numpy as np

from src.enums.color import Color


class Grid:
    def __init__(self, width: int, height: int, color: int, dtype: TypeAlias) -> None:
        self.width = width
        self.height = height
        self.color = color
        self.dtype = dtype

        self.matrix: np.ndarray = np.full((self.width, self.height), self.color, self.dtype)

        self.black_cell_count: int = 0

    def change_cell_color(self, x: int, y: int, color: Color) -> None:
        self.matrix[y, x] = color
