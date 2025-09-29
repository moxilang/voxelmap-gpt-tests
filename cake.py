import numpy as np
from voxelmap import Model
from voxelmap.mesh import MarchingMesh, MeshView

# Dimensions
Z, Y, X = 30, 40, 40
arr = np.zeros((Z, Y, X), dtype=int)

center = (Y // 2, X // 2)
radii = [18, 15, 12, 9, 6]     # decreasing for layers
heights = [4, 4, 4, 4, 4]      # uniform height

# Layer colors (bottom to top)
colors = {
    1: "chocolate",
    2: "pink",
    3: "lemonchiffon",
    4: "lightblue",
    5: "plum",
    6: "orange",     # candles
    7: "white",      # frosting spiral
    8: "black",      # plate
}

# 1. Plate base (checkerboard)
for y in range(Y):
    for x in range(X):
        if (y + x) % 2 == 0:
            arr[0, y, x] = 8

# 2. Cake layers
z_start = 1
for i, (r, h) in enumerate(zip(radii, heights)):
    z_end = z_start + h
    for z in range(z_start, z_end):
        for y in range(Y):
            for x in range(X):
                dy, dx = y - center[0], x - center[1]
                if dy**2 + dx**2 <= r**2:
                    arr[z, y, x] = i + 1
    z_start = z_end

# 3. Candles (random-ish but symmetric)
top_z = z_start
candle_radius = 5
for angle in np.linspace(0, 2*np.pi, 24, endpoint=False):
    ry = int(center[0] + candle_radius * np.sin(angle))
    rx = int(center[1] + candle_radius * np.cos(angle))
    arr[top_z:top_z+2, ry, rx] = 6

# 4. Unique: Swirl icing (helix-style wrap)
for theta in np.linspace(0, 4 * np.pi, 100):
    radius = 17 - (theta / (4 * np.pi)) * 11  # spiral inward
    z = int(1 + (theta / (4 * np.pi)) * (z_start - 1))
    y = int(center[0] + radius * np.sin(theta))
    x = int(center[1] + radius * np.cos(theta))
    if 0 <= z < Z and 0 <= y < Y and 0 <= x < X:
        arr[z, y, x] = 7

# 5. Build model
m = Model(arr)
m.palette = {
    1: "chocolate",
    2: "pink",
    3: "lemonchiffon",
    4: "lightblue",
    5: "plum",
    6: "orange",
    7: "white",
    8: "black",
}

# 6. Export mesh + view
MarchingMesh(m.array, out_file="cake.obj", palette=m.palette, pad=1)
MeshView("cake.obj", palette=m.palette, mode="solid", background_color="white")
