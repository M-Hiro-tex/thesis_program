# Introduction
## The structure of the repository
```
/Programs
├── data_generator.py
├── picture_scatter_nPy.py
├── picture_vertex_nPy.py
└── vlistwc_vispy_nPy.py

/simulation_data
└── colornum_X
  └── iteration_Y
    ├── glist
      └── glist_N.npy
    |── vlistwc
      ├── coords_N.npy
      └── colors_N.npy
    └── tetrawc
      └── tetra_coords_N.npy

/run_venv

README.md
```
## How to use
### 1. Activate the virtual environment of Python 3.10.12
<table>
 <thead>
  <tr>
   <th>OS</th> <th>command line</th>
  </tr>
 </thead>
 <tr>
  <td> Linux/mac </td> <td>```source run_venv/bin/activate```</td>
 </tr>
 <tr>
  <td >Windows </td> <td>```/run_venv/bin/activate```</td>
 </tr>
</table>
to be able to use modules for runniing codes in the 'Programs' directory.

### 2. Run *data_generator.py*
```
python3 data_generator.py
```
to obtain data that are automatically stored in 'Simulation_Data' directory (Sample data have been already prepared in 'Simulation_Data' though :smile:).
### 3. Visualize data
glist -- *picture_scatter_nPy.py*, *picture_vertex_nPy.py*
vlistwc -- *vlistwc_vispy_nPy.py*
