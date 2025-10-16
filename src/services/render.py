import numpy as np
from PIL import Image

from src.core.constants import BASE_DIR
from src.entities.ant import Ant
from src.entities.grid import Grid
from src.enums.color import Color
from src.enums.grid import GridSize


class Renderer:
    def __init__(self, grid: Grid, ant: Ant) -> None:
        self.grid = grid
        self.ant = ant

    def generate_grid_matrix(self) -> np.ndarray:
        while 0 <= self.ant.x < GridSize.WIDTH and 0 <= self.ant.y < GridSize.HEIGHT:
            self._handle_cell()
            self.ant.move()

        return self.grid.matrix

    def _handle_cell(self) -> None:
        if self.grid.matrix[self.ant.y, self.ant.x] == Color.WHITE:  # Если находимся на белой клетке
            self.__handle_white_cell()

        else:  # Если находимся на черной клетке
            self.__handle_black_cell()

    def __handle_white_cell(self) -> None:
        self.ant.turn_clockwise()
        self.grid.change_cell_color(self.ant.x, self.ant.y, Color.BLACK)
        self.grid.black_cell_count += 1

    def __handle_black_cell(self) -> None:
        self.ant.turn_counterclockwise()
        self.grid.change_cell_color(self.ant.x, self.ant.y, Color.WHITE)
        self.grid.black_cell_count -= 1

    def generate_result_png(self) -> None:
        image: Image = Image.fromarray(self.grid.matrix, mode='L').convert('1')
        image.save(BASE_DIR / 'langton_ant.png', format='PNG')
