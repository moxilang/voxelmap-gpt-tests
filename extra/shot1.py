import numpy as np
from voxelmap import Model
from voxelmap.mesh import MarchingMesh, MeshView

# Dimensions of the spaceship grid
shape = (40, 40, 40)
arr = np.zeros(shape, dtype=int)

# --- CORE STRUCTURE: stacked plates + ridges ---
for z in range(10, 30, 2):
    arr[z:z+1, 10:30, 10:30] = 1  # horizontal jagged plates

for i in range(5):
    arr[15+i, 10+i:30-i, 10+i:30-i] = 1  # inward stacked layers

# --- POWER CORE (spherical-ish center) ---
cx, cy, cz = 20, 20, 20
for x in range(14, 26):
    for y in range(14, 26):
        for z in range(14, 26):
            if (x-cx)**2 + (y-cy)**2 + (z-cz)**2 < 25:
                arr[z, y, x] = 2  # core label

# --- BRACING STRUTS + CONDUITS ---
arr[18:22, 10:15, 20] = 3  # left brace
arr[18:22, 25:30, 20] = 3  # right brace
arr[20, 20, 10:15] = 3     # front conduit
arr[20, 20, 25:30] = 3     # back conduit

# --- ASYMMETRICAL MODULES ---
arr[10:13, 30:35, 15:20] = 4  # wing-like fin
arr[28:32, 5:10, 10:13] = 4   # lower turret cluster
arr[15:25, 5:8, 30:35] = 4    # antenna frame
arr[30:34, 30:34, 30:34] = 4  # lattice cube

# --- SURFACE PATTERNING ---
for i in range(10, 30, 3):
    arr[29, i, 15:25] = 5  # top ridges
    arr[10, i, 15:25] = 5  # bottom vents

# --- NEON STRIPS ---
arr[20, 10:30, 10] = 6  # cyan strip
arr[20, 10:30, 29] = 7  # magenta strip
arr[10, 10:30, 20] = 8  # yellow strip

# --- Create model and assign colors ---
m = Model(arr)
m.set_color(1, "#555555", 1.0)    # dark metal plates
m.set_color(2, "white", 0.9)      # power core
m.set_color(3, "#8888ff", 0.8)    # blue-tinted braces
m.set_color(4, "#333333", 1.0)    # black-gray modules
m.set_color(5, "#777777", 0.7)    # surface ridges
m.set_color(6, "cyan", 1.0)       # neon cyan
m.set_color(7, "magenta", 1.0)    # neon magenta
m.set_color(8, "yellow", 1.0)     # neon yellow

# --- Export as OBJ + MTL ---
MarchingMesh(m.array, palette=m.palette, out_file="spaceship.obj")

# --- View interactively ---
MeshView("spaceship.obj", palette=m.palette, mode="both",
         wireframe_color="white", background_color="black")
