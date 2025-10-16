import logging
from logging import INFO, Logger, getLogger

import numpy as np

from src.entities.ant import Ant
from src.entities.grid import Grid
from src.enums.ant import StartAntCoordinates
from src.enums.color import Color
from src.enums.direction import Direction
from src.enums.grid import GridSize

from src.services.render import Renderer

logging.basicConfig(level=INFO)

logger: Logger = getLogger(__name__)


def main() -> None:
    grid: Grid = Grid(
        GridSize.WIDTH,
        GridSize.HEIGHT,
        Color.WHITE,
        np.uint8,
    )

    ant: Ant = Ant(
        StartAntCoordinates.X_START,
        StartAntCoordinates.Y_START,
        Direction.UP,
    )

    renderer: Renderer = Renderer(grid, ant)

    renderer.generate_grid_matrix()
    renderer.generate_result_png()

    logger.info(f'Количество черных клеток: {grid.black_cell_count}')


if __name__ == '__main__':
    main()
