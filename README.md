# VoxelMapGPT Experiments

This repository compares code generations from **baseline GPT-4o** with those created using the **VoxelMapGPT-4o Assistant** (powered by the [Voxelmap-Python](https://github.com/moxilang/voxelmap) package).

* [Voxelmap portfolio](https://voxelmap.vercel.app)
* [VoxelMapGPT-4o Assistant](https://chatgpt.com/g/g-SYS9BBhP8-voxelmapgpt-v5-1)

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
| <img width="1052" height="834" alt="Screenshot from 2025-09-28 23-03-05" src="https://github.com/user-attachments/assets/d158b980-8f5f-4c1e-8847-7c8f0c7faabb" /> | <img width="867" height="815" alt="Screenshot from 2025-09-28 23-04-04" src="https://github.com/user-attachments/assets/ed49ab7a-b487-4890-9596-3fbedd87b750" />
 |

---

### Spaceship

* **VoxelMapGPT-4o:** Fuselage, cockpit, wings, engines, and tail fin in symmetry
* **Baseline GPT-4o:** Random primitives, little structure

| VoxelMapGPT-4o | Baseline GPT-4o |
| -------------- | --------------- |
| <img width="720" height="834" alt="Screenshot from 2025-09-29 13-22-34" src="https://github.com/user-attachments/assets/9a7ae6b3-4e72-4324-a79a-99f889e4fde9" /> | <img width="719" height="827" alt="Screenshot from 2025-09-29 13-22-29" src="https://github.com/user-attachments/assets/9f50f21f-9997-4701-bbd1-c1c906ac2af1" /> |

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
