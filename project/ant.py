from project.enums.direction import Direction


class Ant:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def turn_clockwise(self):
        self.direction = (self.direction + 1) % 4

    def turn_counterclockwise(self):
        self.direction = (self.direction - 1) % 4

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
