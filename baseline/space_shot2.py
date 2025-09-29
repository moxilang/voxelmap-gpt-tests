import numpy as np
import trimesh
from trimesh.creation import box, icosphere, cylinder
import random

def random_box(scale_range=(0.2, 1.0), color=[200, 200, 200, 255]):
    scale = np.random.uniform(*scale_range, size=3)
    b = box(extents=scale)
    b.visual.vertex_colors = color
    return b

def random_cylinder(radius_range=(0.1, 0.3), height_range=(0.3, 1.0), color=[180, 180, 255, 255]):
    r = np.random.uniform(*radius_range)
    h = np.random.uniform(*height_range)
    cyl = cylinder(radius=r, height=h, sections=6)
    cyl.visual.vertex_colors = color
    return cyl

def random_wing(color=[255, 100, 100, 255]):
    verts = np.array([
        [0, 0, 0],
        [random.uniform(0.5, 1.0), 0, 0],
        [0, random.uniform(0.2, 0.5), 0]
    ])
    faces = [[0, 1, 2]]
    w = trimesh.Trimesh(vertices=verts, faces=faces)
    w.visual.vertex_colors = color
    return w

def make_spaceship(seed=None):
    if seed:
        random.seed(seed)
        np.random.seed(seed)
    
    parts = []

    # Central fuselage (blueish)
    body = random_cylinder(radius_range=(0.2, 0.3), height_range=(1.5, 2.5), color=[50, 100, 200, 255])
    parts.append(body)

    # Cockpit sphere (cyan glassy look)
    cockpit = icosphere(subdivisions=2, radius=0.25)
    cockpit.visual.vertex_colors = [100, 255, 255, 200]  # semi-transparent
    cockpit.apply_translation([0, 0, body.bounds[1, 2]])
    parts.append(cockpit)

    # Wings (red)
    for side in [-1, 1]:
        wing = random_wing(color=[200, 50, 50, 255])
        wing.apply_translation([side * 0.5, 0, body.bounds[1, 2] / 2])
        parts.append(wing)

    # Engines (orange)
    for side in [-1, 1]:
        eng = random_cylinder(radius_range=(0.1, 0.15), height_range=(0.5, 0.7), color=[255, 165, 0, 255])
        eng.apply_translation([side * 0.4, 0, -0.3])
        parts.append(eng)

    spaceship = trimesh.util.concatenate(parts)
    return spaceship

if __name__ == "__main__":


    ship = make_spaceship(seed=42)
    scene = trimesh.Scene([ship])
    scene.show(background=[0, 0, 0, 255])  # RGBA black

    ship.show()  # Opens interactive 3D viewer
    ship.export("spaceship.glb")  # Export with colors (GLB keeps them)

