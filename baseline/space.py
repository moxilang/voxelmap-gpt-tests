import numpy as np
import trimesh
from trimesh.creation import box, icosphere, cylinder
import random

def random_box(scale_range=(0.2, 1.0)):
    """Create a randomly scaled box primitive."""
    scale = np.random.uniform(*scale_range, size=3)
    return box(extents=scale)

def random_cylinder(radius_range=(0.1, 0.3), height_range=(0.3, 1.0)):
    """Create a cylinder primitive."""
    r = np.random.uniform(*radius_range)
    h = np.random.uniform(*height_range)
    return cylinder(radius=r, height=h, sections=6)

def random_wing():
    """Create a flat, triangular wing shape."""
    verts = np.array([
        [0, 0, 0],
        [random.uniform(0.5, 1.0), 0, 0],
        [0, random.uniform(0.2, 0.5), 0]
    ])
    faces = [[0, 1, 2]]
    return trimesh.Trimesh(vertices=verts, faces=faces)

def make_spaceship(seed=None):
    if seed:
        random.seed(seed)
        np.random.seed(seed)
    
    parts = []

    # Central fuselage
    body = random_cylinder(radius_range=(0.2, 0.3), height_range=(1.5, 2.5))
    parts.append(body)

    # Cockpit sphere
    cockpit = icosphere(subdivisions=2, radius=0.25)
    cockpit.apply_translation([0, 0, body.bounds[1, 2]])
    parts.append(cockpit)

    # Wings
    for side in [-1, 1]:
        wing = random_wing()
        wing.apply_translation([side * 0.5, 0, body.bounds[1, 2] / 2])
        parts.append(wing)

    # Engines
    for side in [-1, 1]:
        eng = random_cylinder(radius_range=(0.1, 0.15), height_range=(0.5, 0.7))
        eng.apply_translation([side * 0.4, 0, -0.3])
        parts.append(eng)

    spaceship = trimesh.util.concatenate(parts)
    return spaceship

if __name__ == "__main__":
    ship = make_spaceship(seed=42)
    ship.show()  # Opens interactive 3D viewer
    ship.export("spaceship.obj")  # Save for later in Blender/other tools
