from project.configs import Color, WIDTH, HEIGHT
from project.services.ant_service import turn_clockwise, turn_counterclockwise, move_ant


def ant_change_grid(grid, ant):
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

    return grid, black_cell_count


def change_color_to_black(grid, ant):
    grid[ant.y, ant.x] = Color.BLACK.value


def change_color_to_white(grid, ant):
    grid[ant.y, ant.x] = Color.WHITE.value
