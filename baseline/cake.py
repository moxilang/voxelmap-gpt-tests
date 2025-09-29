import numpy as np
import trimesh
from trimesh.creation import cylinder, icosphere

def make_cake(layers=5, candles_per_layer=12, seed=None):
    if seed:
        np.random.seed(seed)

    parts = []

    # Build cake layers (stacked cylinders)
    height_per_layer = 0.3
    radius_start = 1.5
    for i in range(layers):
        r = radius_start - (i * 0.2)
        h = height_per_layer
        layer = cylinder(radius=r, height=h, sections=24)
        layer.apply_translation([0, 0, i * h])
        parts.append(layer)

    # Add candles on top layer
    top_height = layers * height_per_layer
    candle_height = 0.4
    candle_radius = 0.05
    for j in range(candles_per_layer):
        angle = 2 * np.pi * j / candles_per_layer
        x = (radius_start - (layers-1)*0.2) * 0.8 * np.cos(angle)
        y = (radius_start - (layers-1)*0.2) * 0.8 * np.sin(angle)
        candle = cylinder(radius=candle_radius, height=candle_height, sections=6)
        candle.apply_translation([x, y, top_height])
        parts.append(candle)

        # Flame (small sphere)
        flame = icosphere(subdivisions=1, radius=0.07)
        flame.apply_translation([x, y, top_height + candle_height])
        parts.append(flame)

    # Unique touch: cherry on top
    cherry = icosphere(subdivisions=2, radius=0.15)
    cherry.apply_translation([0, 0, top_height + 0.6])
    parts.append(cherry)

    cake = trimesh.util.concatenate(parts)
    return cake

if __name__ == "__main__":
    cake = make_cake(layers=5, candles_per_layer=20, seed=123)
    cake.show()  # Interactive viewer
    cake.export("birthday_cake.obj")  # Export to OBJ
