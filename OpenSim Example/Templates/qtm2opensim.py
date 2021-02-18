# Read c3d file exported from Qualisys Track Manager and write .trc and .mot file for OpenSim.
#
# Example usage:
# https://github.com/qualisys/paf-resources/tree/master/OpenSim%20Example
#
# Inspired by:
# https://github.com/mitkof6/opensim_automated_pipeline
# https://simtk-confluence.stanford.edu/display/OpenSim/C3D+%28.c3d%29+Files#C3D(.c3d)Files-ReadingC3DfilesthroughPythonandC++
##

import os
import argparse
import opensim as osim
import numpy as np
import matplotlib.pyplot as plt
from utils import create_opensim_storage, lowess_bell_shape_kern, mm_to_m, rotate_data_table

parser = argparse.ArgumentParser()
parser.add_argument('--c3d_dir', required=True, help="Path to c3d file")
parser.add_argument('--c3d_file', required=True, help="C3d file name")

def convert_c3d(c3d_dir, c3d_file):

    FORCE_THRESHOLD = 10 # Force data will be set to zero if below threshold

    # Read c3d file
    adapter = osim.C3DFileAdapter()
    adapter.setLocationForForceExpression(1)
    tables = adapter.read(os.path.join(c3d_dir, c3d_file))

    # Get marker data from c3d file
    markers = adapter.getMarkersTable(tables)

    # Rotate marker data
    rotate_data_table(markers, [1, 0, 0], -90) # Assumes that z is pointing up vertically in QTM
        
    # Write marker data to .trc file
    trcAdapter = osim.TRCFileAdapter()
    trcAdapter.write(markers, os.path.join(c3d_dir, c3d_file.replace('.c3d','.trc')))
            
    # Get force data from c3d file
    forces = adapter.getForcesTable(tables)
    t = forces.getIndependentColumn()
    labels = forces.getColumnLabels()

    # create index of samples where force is below threshold
    numFPs = int(forces.getNumColumns()/3)
    r = len(t)
    below = np.full((numFPs,r), False)
    for fpID in range(numFPs):
        f = forces.getDependentColumn('f' + str(fpID + 1))
        fz = np.zeros(r)
        for i in range(r):
            fz[i] = f[i][2]
        below[fpID,:]=fz<FORCE_THRESHOLD

    # set force to zero where fz < threshold
    for i in range(r):
        vec = forces.getRowAtIndex(i)
        if below[0,i]:
            for j in range(3):
                vec[j]=osim.Vec3(0,0,0)
        if below[1,i]:
            for j in range(3,6):
                vec[j]=osim.Vec3(0,0,0)
        forces.setRowAtIndex(i,vec)

    # Plot forces to verify
    # for label in labels:
    #     f = forces.getDependentColumn(label)
    #     r = len(t)
    #     v_np = np.zeros((r, 3))
    #     for i in range(r):
    #         v_np[i, 0] = f[i][0]  
    #         v_np[i, 1] = f[i][1]
    #         v_np[i, 2] = f[i][2]  
    #     plt.plot(t, v_np[0:, 2])
    #     plt.title(label)
    #     plt.show()

    # Rotate forces (Assumes that z is pointing up vertically in QTM)
    rotate_data_table(forces, [1, 0, 0], 90)
    rotate_data_table(forces, [0, 1, 0], 180)
    rotate_data_table(forces, [0, 0, 1], 180)

    # conversion of unit (f -> N, p -> mm, tau -> Nmm)
    mm_to_m(forces, 'p1')
    mm_to_m(forces, 'p2')
    mm_to_m(forces, 'm1')
    mm_to_m(forces, 'm2')

    # interpolate and fit splines to smooth the data
    list_mat = list()
    for label in labels:
        f = forces.getDependentColumn(label)
        list_mat.append(lowess_bell_shape_kern(t, f, label, tau=.00005, output_dir=c3d_dir))

    # construct the matrix of the forces (forces, moments, torques / right and left)
    # (type opensim.Matrix)
    forces_task_np = np.array(list_mat)
    forces_task_mat = osim.Matrix(len(t), 18)
    for n in range(6):
        for j in range(3):
            for i in range(len(t)):
                forces_task_mat.set(i, 3 * n + j, forces_task_np[n, i, j])

    # export forces
    labels_list = ['ground_force_vx', 'ground_force_vy', 'ground_force_vz',
                'ground_force_px', 'ground_force_py', 'ground_force_pz',
                'ground_torque_x', 'ground_torque_y', 'ground_torque_z',
                '1_ground_force_vx', '1_ground_force_vy', '1_ground_force_vz',
                '1_ground_force_px', '1_ground_force_py', '1_ground_force_pz',
                '1_ground_torque_x', '1_ground_torque_y', '1_ground_torque_z']
    force_sto = create_opensim_storage(t, forces_task_mat, labels_list)
    force_sto.setName('GRF')
    force_sto.printResult(force_sto, c3d_file.replace('.c3d',''), c3d_dir, 0.001, '.mot')

# start convert_c3d when running directly from command line
if __name__ == '__main__':
    args = parser.parse_args()
    convert_c3d(args.c3d_dir, args.c3d_file)
