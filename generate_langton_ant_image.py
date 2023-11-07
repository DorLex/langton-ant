import numpy as np
from PIL import Image

from project.ant import Ant
from project.configs import WIDTH, HEIGHT, ANT_X_START, ANT_Y_START, AntDirection, Color


def main():
    grid = np.full((WIDTH, HEIGHT), Color.WHITE.value, dtype=np.uint8)

    ant = Ant(ANT_X_START, ANT_Y_START, AntDirection.UP.value)

    black_cell_count = 0

    while 0 <= ant.x < WIDTH and 0 <= ant.y < HEIGHT:

        # Белая клетка
        if grid[ant.y, ant.x] == Color.WHITE.value:
            ant.direction = (ant.direction + 1) % 4
            grid[ant.y, ant.x] = Color.BLACK.value

        # Черная клетка
        else:
            ant.direction = (ant.direction - 1) % 4
            grid[ant.y, ant.x] = Color.WHITE.value
            black_cell_count += 1

        # Двигаем муравья вперед в соответствии с текущим направлением
        if ant.direction == 0:
            ant.y -= 1
        elif ant.direction == 1:
            ant.x += 1
        elif ant.direction == 2:
            ant.y += 1
        else:
            ant.x -= 1

    image = Image.fromarray(grid, mode='L').convert('1')
    image.save('langton_ant.png', format='PNG')

    print('Число черных клеток:', black_cell_count)


if __name__ == '__main__':
    main()
