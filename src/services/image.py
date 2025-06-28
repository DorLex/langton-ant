import numpy as np
from PIL import Image

from src.core.constants import BASE_DIR


def generate_png_from_array(grid_array: np.ndarray) -> None:
    image: Image = Image.fromarray(grid_array, mode='L').convert('1')
    image.save(BASE_DIR / 'langton_ant.png', format='PNG')
