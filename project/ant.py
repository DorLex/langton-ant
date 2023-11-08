from project.enums.color import Color
from project.enums.direction import Direction
from project.enums.grid_size import GridSize


class Ant:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def turn_clockwise(self):
        self.direction = (self.direction + 1) % 4

    def turn_counterclockwise(self):
        self.direction = (self.direction - 1) % 4

    def change_grid(self, grid):
        black_cell_count = 0
        while 0 <= self.x < GridSize.WIDTH.value and 0 <= self.y < GridSize.HEIGHT.value:

            # Если находимся на белой клетке
            if grid[self.y, self.x] == Color.WHITE.value:
                self.turn_clockwise()
                self.change_color_to_black(grid)
                black_cell_count += 1

            # Если находимся на черной клетке
            else:
                self.turn_counterclockwise()
                self.change_color_to_white(grid)
                black_cell_count -= 1

            self.move()

        return grid, black_cell_count

    def change_color_to_black(self, grid):
        grid[self.y, self.x] = Color.BLACK.value

    def change_color_to_white(self, grid):
        grid[self.y, self.x] = Color.WHITE.value

    def move(self):
        match self.direction:
            case Direction.UP.value:
                self.y -= 1
            case Direction.RIGHT.value:
                self.x += 1
            case Direction.DOWN.value:
                self.y += 1
            case _:
                self.x -= 1
