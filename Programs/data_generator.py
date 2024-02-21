import numpy as np
import random
import os

def find_vertex(a, b, c):
    ac = c - a
    ab = b - a
    abxac = np.cross(ab, ac)
    ed = abxac / np.linalg.norm(abxac)
    ag = (ab + ac) / 3

    A = np.dot(ed, ed)
    B = 2 * np.dot(ag, ed)
    C = np.dot(ag, ag) - np.dot(ab, ab)

    discriminant = B**2 - 4*A*C
        
    if discriminant < 0:
        raise ValueError("No real solutions exist")

    sqrt_discriminant = np.sqrt(discriminant)
    x1 = (-B + sqrt_discriminant) / (2*A)
    x2 = (-B - sqrt_discriminant) / (2*A)

    return [a + x1 * ed + ag, a + x2 * ed + ag]

def near_vlist(p, vlistwc, elength):
    for nvk in range(len(vlistwc)):
        if np.linalg.norm(vlistwc[nvk][0] - p) < 0.99999*elength:
            return True
    return False

def near_vlistWC(p, c, vlistwc, elength):
    for nvk in range(len(vlistwc)):
        if c == vlistwc[nvk][1]:
            if np.linalg.norm(vlistwc[nvk][0] - p) < np.sqrt(3) * elength:
                return True
    return False

def node_find(new_tetra):
    return np.mean([vertex[0] for vertex in new_tetra], axis=0)

def collect_simulation_data(a, b, c, iteration_number, colornum):
    dlist = find_vertex(a, b, c)
    elength = np.linalg.norm(a - b)
    color_set = set(range(1, colornum + 1))
    vlistwc = [[a, 1], [b, 2], [c, 3], [dlist[0], 4], [dlist[1], 5]]
    tlistwc = [[[a, 1], [b, 2], [c, 3], [dlist[0], 4]], [[a, 1], [b, 2], [c, 3], [dlist[1], 5]]]

    for _ in range(iteration_number):
        Tetrawc = random.choice(tlistwc)
        for i in range(4):
            trianglewc = [x for j, x in enumerate(Tetrawc) if j != i]
            NewV = (2/3) * np.sum([x[0] for x in trianglewc], axis=0) - Tetrawc[i][0]
            colors = {x[1] for x in trianglewc}
            NewClist = list(color_set - colors)
            NewC = random.choice(NewClist)
            NewTetrawc = trianglewc + [[NewV, NewC]]
            
            if not (near_vlist(NewV, vlistwc, elength) or near_vlistWC(NewV, NewC, vlistwc, elength)):
                vlistwc.append([NewV, NewC])
                tlistwc.append(NewTetrawc)

    return vlistwc, tlistwc

def simulate_and_save_all_data(a, b, c, iteration_numbers, colornums, times):
    base_directory = "/home/mumu/thesis_program/Simulation_Data"
    if not os.path.exists(base_directory):
        os.makedirs(base_directory)
    
    result_messages = []

    for colornum in colornums:
        for iteration_number in iteration_numbers:
            dir_glist = os.path.join(base_directory, f"colornum_{colornum}", f"iteration_{iteration_number}", "glist")
            dir_vlistwc = os.path.join(base_directory, f"colornum_{colornum}", f"iteration_{iteration_number}", "vlistwc")
            dir_tetrawc = os.path.join(base_directory, f"colornum_{colornum}", f"iteration_{iteration_number}", "tetrawc")
            
            for directory in [dir_glist, dir_vlistwc, dir_tetrawc]:
                if not os.path.exists(directory):
                    os.makedirs(directory)

            for i in range(times):
                vlistwc, tlistwc = collect_simulation_data(a, b, c, iteration_number, colornum)
                glist = [node_find(tetra) for tetra in tlistwc]

                np.save(os.path.join(dir_glist, f"glist_{i+1}.npy"), glist)
                coords = np.array([item[0] for item in vlistwc])
                colors = np.array([item[1] for item in vlistwc])
                np.save(os.path.join(dir_vlistwc, f"coords_{i+1}.npy"), coords)
                np.save(os.path.join(dir_vlistwc, f"colors_{i+1}.npy"), colors)
                tetra_coords = np.array([[vertex[0] for vertex in tetra] for tetra in tlistwc])
                np.save(os.path.join(dir_tetrawc, f"tetra_coords_{i+1}.npy"), tetra_coords)
            
            result_messages.append(f"Saved data for colornum {colornum}, iteration {iteration_number}, set {i+1}")

    return result_messages

# Parameters for simulation
a = np.array([1, 0, 0])
b = np.array([0, 1, 0])
c = np.array([0, 0, 1])
#iteration_nums = [5000, 10000, 50000, 100000, 500000]  # Iteration numbers
#color_nums = [4, 5, 6, 7, 8, 9, 10, 11, 12, 50, 100]  # Number of colors
#dataset_nums = 5
iteration_nums = [500] # sample number of iterations
color_nums = [8]  # sample number of colors
dataset_nums = 1 # sample number of data

# Execute simulation and save all data
result_messages = simulate_and_save_all_data(a, b, c, iteration_nums, color_nums, dataset_nums)
for message in result_messages:
    print(message)
