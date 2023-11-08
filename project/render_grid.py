from project.enums.color import Color
from project.enums.grid_size import GridSize


def render_grid_array(grid, ant):
    while 0 <= ant.x < GridSize.WIDTH.value and 0 <= ant.y < GridSize.HEIGHT.value:

        # Если находимся на белой клетке
        if grid.grid_array[ant.y, ant.x] == Color.WHITE.value:
            ant.turn_clockwise()
            grid.change_color_to_black(ant.x, ant.y)
            grid.black_cell_count += 1

        # Если находимся на черной клетке
        else:
            ant.turn_counterclockwise()
            grid.change_color_to_white(ant.x, ant.y)
            grid.black_cell_count -= 1

        ant.move()

    return grid.grid_array
