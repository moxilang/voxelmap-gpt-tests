import numpy as np
import trimesh
from trimesh.creation import cylinder, icosphere

def make_cake(layers=5, candles_per_layer=12, seed=None):
    if seed:
        np.random.seed(seed)

    parts = []
    colors = []

    # --- Cake layers ---
    height_per_layer = 0.3
    radius_start = 1.5
    for i in range(layers):
        r = radius_start - (i * 0.2)
        h = height_per_layer
        layer = cylinder(radius=r, height=h, sections=32)
        layer.apply_translation([0, 0, i * h])

        # Alternate colors (chocolate/vanilla)
        color = [139, 69, 19, 255] if i % 2 == 0 else [245, 222, 179, 255]
        layer.visual.vertex_colors = np.tile(color, (layer.vertices.shape[0], 1))

        parts.append(layer)

    # --- Candles + Flames ---
    top_height = layers * height_per_layer
    candle_height = 0.4
    candle_radius = 0.05
    palette = [
        [255, 0, 0, 255],    # red
        [0, 255, 0, 255],    # green
        [0, 0, 255, 255],    # blue
        [255, 255, 0, 255],  # yellow
        [255, 105, 180, 255] # pink
    ]

    for j in range(candles_per_layer):
        angle = 2 * np.pi * j / candles_per_layer
        x = (radius_start - (layers-1)*0.2) * 0.8 * np.cos(angle)
        y = (radius_start - (layers-1)*0.2) * 0.8 * np.sin(angle)

        # Candle stick
        candle = cylinder(radius=candle_radius, height=candle_height, sections=12)
        candle.apply_translation([x, y, top_height])
        candle_color = palette[j % len(palette)]
        candle.visual.vertex_colors = np.tile(candle_color, (candle.vertices.shape[0], 1))
        parts.append(candle)

        # Flame
        flame = icosphere(subdivisions=1, radius=0.07)
        flame.apply_translation([x, y, top_height + candle_height])
        flame.visual.vertex_colors = np.tile([255, 165, 0, 255], (flame.vertices.shape[0], 1))  # orange
        parts.append(flame)

    # --- Cherry on top ---
    cherry = icosphere(subdivisions=2, radius=0.15)
    cherry.apply_translation([0, 0, top_height + 0.6])
    cherry.visual.vertex_colors = np.tile([220, 20, 60, 255], (cherry.vertices.shape[0], 1))  # crimson red
    parts.append(cherry)

    # Combine all
    cake = trimesh.util.concatenate(parts)
    return cake

if __name__ == "__main__":
    cake = make_cake(layers=5, candles_per_layer=20, seed=123)
    cake.show()           # Interactive viewer
    cake.export("birthday_cake_colored.obj")  # Save with colors
