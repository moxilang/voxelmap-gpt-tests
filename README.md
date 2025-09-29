# VoxelMapGPT Experiments

This repository compares code generations from **baseline GPT-4o** with those created using the **VoxelMapGPT-4o Assistant** (powered by the [Voxelmap-Python](https://github.com/moxilang/voxelmap) package).

* [Voxelmap portfolio](https://voxelmap.vercel.app)
* [VoxelMapGPT-4o Assistant](INSERT-GPT-ASSISTANT-LINK)

---

## Overview

The purpose of this project is to evaluate how GPT-4o performs when paired with a domain-specific assistant.

* **Baseline (GPT-4o only):** Relied on generic geometry libraries such as `trimesh`. Results were simple, inconsistent, and often required retries.
* **VoxelMapGPT-4o (Assistant + Voxelmap):** Defaulted to voxel-based modeling and produced structured, symmetric, and visually striking results, including layered cakes and coherent spacecraft.

---

## Repository Structure

```
.
├── space.py               # Spaceship generated with VoxelMapGPT-4o Assistant
├── cake.py                # Birthday cake generated with VoxelMapGPT-4o Assistant
├── baseline/
│   ├── cake.py            # Baseline cake (GPT-4o only, first attempt)
│   ├── cake_shot2.py      # Baseline cake (second attempt, still weaker)
│   └── space.py           # Baseline spaceship (GPT-4o only)
```

* **baseline/** → Code from regular GPT-4o without the assistant or Voxelmap
* **root scripts** → Generated with VoxelMapGPT-4o Assistant, using the Voxelmap package by default

---

## Results

### Birthday Cake

* **VoxelMapGPT-4o:** Five layers, spiral frosting, checkerboard plate, symmetric candles
* **Baseline GPT-4o:** Stacked cylinders and spheres, much simpler

| VoxelMapGPT-4o                             | Baseline GPT-4o                          |
| ---------------------------------------- | ---------------------------------------- |
| ![Voxelmap Cake](docs/cake_voxelmap.png) | ![Baseline Cake](docs/cake_baseline.png) |

---

### Spaceship

* **VoxelMapGPT-4o:** Fuselage, cockpit, wings, engines, and tail fin in symmetry
* **Baseline GPT-4o:** Random primitives, little structure

| VoxelMapGPT-4o                                  | Baseline GPT-4o                               |
| --------------------------------------------- | --------------------------------------------- |
| ![Voxelmap Spaceship](docs/ship_voxelmap.png) | ![Baseline Spaceship](docs/ship_baseline.png) |

*(Add screenshots to a `/docs/` folder for display.)*

---

## Key Takeaways

* VoxelMapGPT-4o produces symmetric, coherent, and creative geometry
* Baseline GPT-4o outputs are simpler and less consistent
* Even with retries, baselines did not reach the assistant’s quality

---

## Quickstart

Install [Voxelmap](https://github.com/moxilang/voxelmap):

```bash
pip install voxelmap
```

Run a script:

```bash
python cake.py     # Generates a 5-layer voxel cake
python space.py    # Generates a voxel spaceship
```

Meshes are exported as `.obj` and can be viewed with `MeshView`, Blender, or MeshLab.


---

## Conclusion

With the **VoxelMapGPT-4o Assistant**, GPT-4o is capable of generating not only functional code but also richer geometry and more aesthetic 3D outputs. This repository highlights the contrast between baseline GPT code and augmented results when supported by a voxel-aware assistant.
