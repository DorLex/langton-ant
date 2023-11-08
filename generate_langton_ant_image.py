import numpy as np

from project.ant import Ant
from project.configs import WIDTH, HEIGHT, ANT_X_START, ANT_Y_START, Direction, Color
from project.services.ant_service import move_ant, turn_clockwise, turn_counterclockwise
from project.services.grid_service import change_color_to_black, change_color_to_white
from project.services.image_service import generate_png_from_array


def main():
    grid = np.full((WIDTH, HEIGHT), Color.WHITE.value, dtype=np.uint8)

    ant = Ant(ANT_X_START, ANT_Y_START, Direction.UP.value)

    black_cell_count = 0
    while 0 <= ant.x < WIDTH and 0 <= ant.y < HEIGHT:

        # Если находимся на белой клетке
        if grid[ant.y, ant.x] == Color.WHITE.value:
            turn_clockwise(ant)
            change_color_to_black(grid, ant)
            black_cell_count += 1

        # Если находимся на черной клетке
        else:
            turn_counterclockwise(ant)
            change_color_to_white(grid, ant)
            black_cell_count -= 1

        move_ant(ant)

    generate_png_from_array(grid)

    print(f'Количество черных клеток: {black_cell_count}')


if __name__ == '__main__':
    main()
