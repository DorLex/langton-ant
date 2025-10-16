from src.enums.direction import Direction


class Ant:
    def __init__(self, x: int, y: int, direction: int) -> None:
        self.x = x
        self.y = y
        self.direction = direction

    def turn_clockwise(self) -> None:
        self.direction = (self.direction + 1) % 4

    def turn_counterclockwise(self) -> None:
        self.direction = (self.direction - 1) % 4

    def move(self) -> None:
        match self.direction:
            case Direction.UP:
                self.y -= 1
            case Direction.RIGHT:
                self.x += 1
            case Direction.DOWN:
                self.y += 1
            case _:
                self.x -= 1
