import numpy as np
from voxelmap import Model
from voxelmap.mesh import MarchingMesh, MeshView

# Step 1: Symmetric voxel model
shape = (30, 20, 10)  # (Z, Y, X)
arr = np.zeros(shape, dtype=int)

# Fuselage
arr[5:25, 8:12, 4:6] = 1

# Cockpit
arr[23:27, 9:11, 4:6] = 2

# Wings
for i in range(5):
    arr[10+i, 6-i:14+i, 3] = 3
    arr[10+i, 6-i:14+i, 6] = 3

# Engines
arr[4:6, 7:9, 2:4] = 4
arr[4:6, 11:13, 2:4] = 4

# Tail
arr[5:15, 9:11, 6] = 5

# Symmetry across X-axis
arr = arr + arr[:, :, ::-1]

# Step 2: Model with solid colors only
m = Model(arr)
m.palette = {
    1: "gray",     # fuselage
    2: "blue",     # cockpit
    3: "silver",   # wings
    4: "orange",   # engines
    5: "red",      # tail fin
}

# Step 3: Mesh export
MarchingMesh(m.array, out_file="spaceship.obj", palette=m.palette, pad=1)

# Step 4: View solid (no wireframe, no transparency)
MeshView("spaceship.obj", palette=m.palette, mode="solid", background_color="black")
