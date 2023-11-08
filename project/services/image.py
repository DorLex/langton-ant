from PIL import Image


def generate_png_from_array(grid_array):
    image = Image.fromarray(grid_array, mode='L').convert('1')
    image.save('langton_ant.png', format='PNG')
