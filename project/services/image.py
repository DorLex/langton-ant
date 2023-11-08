from PIL import Image


def generate_png_from_array(grid):
    image = Image.fromarray(grid, mode='L').convert('1')
    image.save('langton_ant.png', format='PNG')
