import numpy as np
from voxelmap import Model
from voxelmap.mesh import MarchingMesh, MeshView

# Base array (dense cube)
arr = np.zeros((50, 50, 50), dtype=int)

# --- CORE: large embedded power sphere ---
cx, cy, cz = 25, 25, 25
for x in range(15, 35):
    for y in range(15, 35):
        for z in range(15, 35):
            if (x-cx)**2 + (y-cy)**2 + (z-cz)**2 < 90:
                arr[z, y, x] = 2  # power core (lime green)

# --- DARK METAL PLATES: surround core, evenly spaced ---
for z in range(10, 40, 3):
    arr[z, 12:38, 12:38] = 1  # full coverage plates

# --- STRUCTURAL BRACES around core ---
arr[20:30, 10:15, 25] = 3  # left brace
arr[20:30, 35:40, 25] = 3  # right brace
arr[25, 10:15, 20:30] = 3  # front
arr[25, 35:40, 20:30] = 3  # back
arr[25, 20:30, 10:15] = 3  # bottom
arr[25, 20:30, 35:40] = 3  # top

# --- ASYMMETRICAL COMPLEX MODULES ---
arr[10:15, 38:48, 20:30] = 4  # fin panel
arr[35:45, 5:15, 15:20] = 4   # antenna block
arr[15:35, 5:8, 35:45] = 4    # turret row

# --- LATTICE MODULES (multi-cube) ---
for x in range(3):
    for y in range(3):
        arr[40+x*2, 40+y*2, 10:13] = 5  # external cage

# --- SURFACE DETAILS: extrusions, ridges, vents ---
for i in range(15, 35, 2):
    arr[39, i, 20:30] = 6  # upper ridges
    arr[10, i, 20:30] = 6  # lower vent-like

# --- NEON LIGHTING STRIPS: angled layout ---
arr[25, 15:35, 12] = 7  # cyan line
arr[25, 15:35, 37] = 8  # magenta line
arr[15, 12, 15:35] = 9  # yellow cross-beam

# --- Add new detail types ---
arr[12:15, 12:15, 12:15] = 10   # node cluster
arr[45:48, 45:48, 45:48] = 11  # distant spike
arr[18:20, 18:20, 38:41] = 12  # rear grid
arr[30:33, 40:43, 30:33] = 13  # upper dome pad

# --- Define model and assign colors ---
m = Model(arr)
m.set_color(1, "#444444", 0.5)    # dark metal plates (semi-transparent)
m.set_color(2, "lime", 1.0)       # power core
m.set_color(3, "#8888ff", 1.0)    # structural braces
m.set_color(4, "#222222", 1.0)    # external modules
m.set_color(5, "#666666", 1.0)    # lattice components
m.set_color(6, "#999999", 1.0)    # ridges and vents
m.set_color(7, "cyan", 1.0)       # neon cyan
m.set_color(8, "magenta", 1.0)    # neon magenta
m.set_color(9, "yellow", 1.0)     # neon yellow
m.set_color(10, "orange", 1.0)    # internal node
m.set_color(11, "red", 1.0)       # aggressive tip
m.set_color(12, "blue", 1.0)      # grid segment
m.set_color(13, "purple", 1.0)    # dome structure

# --- Export mesh with full palette ---
MarchingMesh(m.array, palette=m.palette, out_file="spaceship.obj")

# --- Wireframe mode only for lime core (label 2) ---
custom_palette = dict(m.palette)
# Override wireframe target to core only
wireframe_color = "lime"

# --- Launch viewer ---
MeshView("spaceship.obj",
         palette=custom_palette,
         mode="both",
         wireframe_color=wireframe_color,
         background_color="black")
