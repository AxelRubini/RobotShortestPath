import numpy as np
from scipy.interpolate import CubicSpline

def cube(center, size):
    x, y, z = center
    d = size / 2
    vertices = np.array([[x - d, y - d, z - d],
                         [x + d, y - d, z - d],
                         [x + d, y + d, z - d],
                         [x - d, y + d, z - d],
                         [x - d, y - d, z + d],
                         [x + d, y - d, z + d],
                         [x + d, y + d, z + d],
                         [x - d, y + d, z + d]])
    faces = [[vertices[j] for j in [0, 1, 2, 3]],
             [vertices[j] for j in [4, 5, 6, 7]],
             [vertices[j] for j in [0, 3, 7, 4]],
             [vertices[j] for j in [1, 2, 6, 5]],
             [vertices[j] for j in [0, 1, 5, 4]],
             [vertices[j] for j in [3, 2, 6, 7]]]
    return faces

def euclidean_distance(node1, node2):
    return np.sqrt((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2 + (node1[2] - node2[2]) ** 2)

def convert_to_real_coordinates(path, scale_factor):
    real_path = [(x * scale_factor, y * scale_factor, z * scale_factor) for (x, y, z) in path]
    return real_path


def smooth_path(path, num_points=100):
    path = np.array(path)
    t = np.linspace(0, 1, len(path))
    cs_x = CubicSpline(t, path[:, 0])
    cs_y = CubicSpline(t, path[:, 1])
    cs_z = CubicSpline(t, path[:, 2])

    t_new = np.linspace(0, 1, num_points)
    smooth_path = np.vstack((cs_x(t_new), cs_y(t_new), cs_z(t_new))).T
    return smooth_path

