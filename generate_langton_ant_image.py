import numpy as np

from project.ant import Ant
from project.enums.ant_coordinates import AntCoordinates
from project.enums.color import Color
from project.enums.direction import Direction
from project.enums.grid_size import GridSize

from project.services.image import generate_png_from_array


def main():
    grid = np.full(
        (GridSize.WIDTH.value, GridSize.HEIGHT.value),
        Color.WHITE.value,
        dtype=np.uint8
    )

    ant = Ant(AntCoordinates.X_START.value, AntCoordinates.Y_START.value, Direction.UP.value)

    grid, black_cell_count = ant.change_grid(grid)

    generate_png_from_array(grid)

    print(f'Количество черных клеток: {black_cell_count}')


if __name__ == '__main__':
    main()
