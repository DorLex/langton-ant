from project.configs import Color


def change_color_to_black(grid, ant):
    grid[ant.y, ant.x] = Color.BLACK.value


def change_color_to_white(grid, ant):
    grid[ant.y, ant.x] = Color.WHITE.value
