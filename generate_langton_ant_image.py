import numpy as np

from project.ant import Ant
from project.configs import WIDTH, HEIGHT, ANT_X_START, ANT_Y_START, Direction, Color

from project.services.grid import ant_change_grid
from project.services.image import generate_png_from_array


def main():
    grid = np.full((WIDTH, HEIGHT), Color.WHITE.value, dtype=np.uint8)
    ant = Ant(ANT_X_START, ANT_Y_START, Direction.UP.value)

    grid, black_cell_count = ant_change_grid(grid, ant)

    generate_png_from_array(grid)

    print(f'Количество черных клеток: {black_cell_count}')


if __name__ == '__main__':
    main()
