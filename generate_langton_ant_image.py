import numpy as np

from project.ant import Ant
from project.enums.ant_coordinates import AntCoordinates
from project.enums.color import Color
from project.enums.direction import Direction
from project.enums.grid_size import GridSize
from project.grid import Grid
from project.render_grid import render_grid_array

from project.services.image import generate_png_from_array


def main():
    grid = Grid(GridSize.WIDTH.value, GridSize.HEIGHT.value, Color.WHITE.value, np.uint8)
    ant = Ant(AntCoordinates.X_START.value, AntCoordinates.Y_START.value, Direction.UP.value)

    final_grid_array = render_grid_array(grid, ant)

    generate_png_from_array(final_grid_array)

    print(f'Количество черных клеток: {grid.black_cell_count}')


if __name__ == '__main__':
    main()
