import logging
from logging import INFO, Logger, getLogger

import numpy as np

from src.entities.ant import Ant
from src.entities.grid import Grid
from src.enums.ant import StartAntCoordinates
from src.enums.color import Color
from src.enums.direction import Direction
from src.enums.grid import GridSize
from src.render_grid import render_result_grid_array
from src.services.image import generate_png_from_array

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

    result_grid_array: np.ndarray = render_result_grid_array(grid, ant)

    generate_png_from_array(result_grid_array)

    logger.info(f'Количество черных клеток: {grid.black_cell_count}')


if __name__ == '__main__':
    main()
