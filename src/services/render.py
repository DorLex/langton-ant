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
            # Если находимся на белой клетке
            if self.grid.matrix[self.ant.y, self.ant.x] == Color.WHITE:
                self.ant.turn_clockwise()
                self.grid.change_color_to_black(self.ant.x, self.ant.y)
                self.grid.black_cell_count += 1

            # Если находимся на черной клетке
            else:
                self.ant.turn_counterclockwise()
                self.grid.change_color_to_white(self.ant.x, self.ant.y)
                self.grid.black_cell_count -= 1

            self.ant.move()

        return self.grid.matrix

    def generate_result_png(self) -> None:
        image: Image = Image.fromarray(self.grid.matrix, mode='L').convert('1')
        image.save(BASE_DIR / 'langton_ant.png', format='PNG')
