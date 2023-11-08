from project.configs import Direction


def turn_clockwise(ant):
    ant.direction = (ant.direction + 1) % 4


def turn_counterclockwise(ant):
    ant.direction = (ant.direction - 1) % 4


def move_ant(ant):
    if ant.direction == Direction.UP.value:
        ant.y -= 1
    elif ant.direction == Direction.RIGHT.value:
        ant.x += 1
    elif ant.direction == Direction.DOWN.value:
        ant.y += 1
    else:
        ant.x -= 1
