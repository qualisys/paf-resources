# Utility functions.
#
# author: Dimitar Stanev <jimstanev@gmail.com>
# https://github.com/mitkof6/opensim_automated_pipeline
##
import re
import os
import opensim
import numpy as np
import pandas as pd
from scipy import linalg
# import matplotlib.pyplot as plt # include this when generating plots to verify force filter

def rotate_data_table(table, axis, deg):
    """Rotate OpenSim::TimeSeriesTableVec3 entries using an axis and angle.

    Parameters
    ----------
    table: OpenSim.common.TimeSeriesTableVec3

    axis: 3x1 vector

    deg: angle in degrees

    """
    R = opensim.Rotation(np.deg2rad(deg),
                         opensim.Vec3(axis[0], axis[1], axis[2]))
    for i in range(table.getNumRows()):
        vec = table.getRowAtIndex(i)
        vec_rotated = R.multiply(vec)
        table.setRowAtIndex(i, vec_rotated)

def mm_to_m(table, label):
    """Scale from units in mm for units in m.

    Parameters
    ----------
    label: string containing the name of the column you want to convert

    """
    c = table.updDependentColumn(label)
    for i in range(c.size()):
        c[i] = opensim.Vec3(c[i][0] * 0.001, c[i][1] * 0.001, c[i][2] * 0.001)

def lowess_bell_shape_kern(t, v, label, tau=.0005, output_dir='.'):
    """lowess_bell_shape_kern(t, v, tau = .005) -> vest Locally weighted
    regression: fits a nonparametric regression curve to a
    scatterplot.  The arrays t and v contain an equal number of
    elements; each pair (t[i], v[i,j]) defines a data point in the
    scatterplot. Depending on j, this corresponds to the x,y or z
    column of the matrix v. The function returns the estimated
    (smooth) values of each columns of y in a matrix.  The kernel
    function is the bell shaped function with parameter tau. Larger
    tau will result in a smoother curve.

    """
    r = len(t)

    # convert tuple into np.array
    t_np = np.zeros(r)
    for i in range(r):
        t_np[i] = t[i]

    # convert Vec3 into np.array
    v_np = np.zeros((r, 3))
    for i in range(r):
        v_np[i, 0] = v[i][0]  # extract x component at each time step
        v_np[i, 1] = v[i][1]
        v_np[i, 2] = v[i][2]

    # interpolate to replace NaN
    v_int = np.zeros((r, 3))
    for j in range(3):
        v_pd = pd.Series(v_np[:, j])
        v_pd = v_pd.interpolate(limit_direction="both", kind="cubic")
        v_int[:, j] = v_pd.to_numpy()

    # initializing all weights from the bell shape kernel function
    for j in range(3):
        w = [np.exp(- (t_np - t_np[i])**2/(2*tau)) for i in range(r)]

    # looping through all v-points
    vest = np.zeros((r, 3))
    for j in range(3):
        for i in range(r):
            weights = w[i]
            b = np.array([np.sum(weights * v_int[:, j]),
                          np.sum(weights * v_int[:, j] * t_np)])
            A = np.array([[np.sum(weights), np.sum(weights * t_np)],
                          [np.sum(weights * t_np), np.sum(weights * t_np * t_np)]])
            theta = linalg.solve(A, b)
            vest[i, j] = theta[0] + theta[1] * t_np[i]

    # validation
    # plt.figure()
    # plt.plot(v_np[:, 0], label='raw')
    # plt.ylabel(label)
    # plt.xlabel('sample')
    # plt.plot(vest[:, 0], label='filtered')
    # plt.legend()
    # plt.savefig(output_dir + '/{}_x.pdf'.format(label))

    # plt.figure()
    # plt.plot(v_np[:, 1], label='raw')
    # plt.ylabel(label)
    # plt.xlabel('sample')
    # plt.plot(vest[:, 1], label='filtered')
    # plt.legend()
    # plt.savefig(output_dir + '/{}_y.pdf'.format(label))

    # plt.figure()
    # plt.plot(v_np[:, 2], label='raw')
    # plt.ylabel(label)
    # plt.xlabel('sample')
    # plt.plot(vest[:, 2], label='filtered')
    # plt.legend()
    # plt.savefig(output_dir + '/{}_z.pdf'.format(label))
    # plt.close('all')

    return vest

def create_opensim_storage(time, data, column_names):
    """Creates a OpenSim::Storage.

    Parameters
    ----------
    time: SimTK::Vector

    data: SimTK::Matrix

    column_names: list of strings

    Returns
    -------
    sto: OpenSim::Storage

    """
    sto = opensim.Storage()
    sto.setColumnLabels(list_to_osim_array_str(['time'] + column_names))
    for i in range(data.nrow()):
        row = opensim.ArrayDouble()
        for j in range(data.ncol()):
            row.append(data.get(i, j))

        sto.append(time[i], row)

    return sto

def list_to_osim_array_str(list_str):
    """Convert Python list of strings to OpenSim::Array<string>."""
    arr = opensim.ArrayStr()
    for element in list_str:
        arr.append(element)

    return arr