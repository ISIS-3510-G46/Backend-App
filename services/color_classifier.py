import numpy as np
from PIL import Image 

# https://stackoverflow.com/questions/3241929/how-to-find-the-dominant-most-common-color-in-an-image
def get_dominant_color(image_file):
    # Resize image to speed up processing
    img_file = Image.open(image_file)
    img = img_file.copy()
    img.thumbnail((100, 100))

    # Reduce colors (uses k-means internally)
    paletted = img.convert('P', palette=Image.ADAPTIVE)

    # Find the color that occurs most often
    palette = paletted.getpalette()
    color_counts = sorted(paletted.getcolors(), reverse=True)
    palette_index = color_counts[1][1]
    dominant_color = palette[palette_index*3:palette_index*3+3]
    final_color = closest_basic_color(dominant_color)

    return final_color



colors_map = {
    'Rojo': (255, 0, 0),
    'Verde': (50, 128,50),
    'Azul': (0, 0, 255),
    'Amarillo': (255, 255, 0),
    'Negro': (0, 0, 0),
    'Blanco': (255, 255, 255),
}

def closest_basic_color(rgb):
    min_dist = float('inf')
    closest_name = None
    for name, value in colors_map.items():
        dist = np.linalg.norm(np.array(rgb) - np.array(value))
        if dist < min_dist:
            min_dist = dist
            closest_name = name
    return closest_name