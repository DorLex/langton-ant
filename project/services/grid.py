from project.enums.color import Color
from project.enums.grid_size import GridSize


def ant_change_grid(grid, ant):
    black_cell_count = 0
    while 0 <= ant.x < GridSize.WIDTH.value and 0 <= ant.y < GridSize.HEIGHT.value:

        # Если находимся на белой клетке
        if grid[ant.y, ant.x] == Color.WHITE.value:
            ant.turn_clockwise()
            change_color_to_black(grid, ant)
            black_cell_count += 1

        # Если находимся на черной клетке
        else:
            ant.turn_counterclockwise()
            change_color_to_white(grid, ant)
            black_cell_count -= 1

        ant.move()

    return grid, black_cell_count


def change_color_to_black(grid, ant):
    grid[ant.y, ant.x] = Color.BLACK.value


def change_color_to_white(grid, ant):
    grid[ant.y, ant.x] = Color.WHITE.value