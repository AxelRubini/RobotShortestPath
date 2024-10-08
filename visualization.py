import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from utils import cube
import numpy as np

def visualize_path(path, obstacles, grid_size, current=None):
    plt.clf()
    ax = plt.axes(projection='3d')

    for obstacle in obstacles:
        faces = cube(obstacle, 1)
        ax.add_collection3d(Poly3DCollection(faces, facecolors='red', linewidths=1, edgecolors='r', alpha=.5))

    for node in path:
        faces = cube(node, 1)
        ax.add_collection3d(Poly3DCollection(faces, facecolors='blue', linewidths=1, edgecolors='b', alpha=.6))

    if current:
        faces = cube(current, 1)
        ax.add_collection3d(Poly3DCollection(faces, facecolors='green', linewidths=1, edgecolors='g', alpha=.6))

    ax.set_xlim([0, grid_size[0]])
    ax.set_ylim([0, grid_size[1]])
    ax.set_zlim([0, grid_size[2]])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.draw()
    plt.pause(0.2)

def visualize_path_final(path, obstacles, grid_size):
    plt.ion()  # Enable interactive mode
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for obstacle in obstacles:
        faces = cube(obstacle, 1)
        ax.add_collection3d(Poly3DCollection(faces, facecolors='red', linewidths=1, edgecolors='r', alpha=.5))

    for node in path:
        faces = cube(node, 1)
        ax.add_collection3d(Poly3DCollection(faces, facecolors='blue', linewidths=1, edgecolors='b', alpha=.6))

    # Plot the smoothed path points
    path = np.array(path)
    ax.scatter(path[:, 0], path[:, 1], path[:, 2], color='green', s=10)

    ax.set_xlim([0, grid_size[0] * 100])  # Adjusted for real coordinates
    ax.set_ylim([0, grid_size[1] * 100])  # Adjusted for real coordinates
    ax.set_zlim([0, grid_size[2] * 100])  # Adjusted for real coordinates

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show(block=True)  # Ensure the plot stays open

