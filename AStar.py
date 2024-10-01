import heapq
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # For Mac OS X
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Function to create the vertices of a cube
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

# Function to calculate the Euclidean distance between two 3D points
def euclidean_distance(node1, node2):
    return np.sqrt((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2 + (node1[2] - node2[2]) ** 2)

# Visualization of the path with Matplotlib
def visualize_path(path, obstacles, grid_size, current=None):
    plt.clf()
    ax = plt.axes(projection='3d')

    # Visualize obstacles
    for obstacle in obstacles:
        faces = cube(obstacle, 1)
        ax.add_collection3d(Poly3DCollection(faces, facecolors='red', linewidths=1, edgecolors='r', alpha=.5))

    # Visualize the path
    for node in path:
        faces = cube(node, 1)
        ax.add_collection3d(Poly3DCollection(faces, facecolors='blue', linewidths=1, edgecolors='b', alpha=.6))

    # Visualize the current node
    if current:
        faces = cube(current, 1)
        ax.add_collection3d(Poly3DCollection(faces, facecolors='green', linewidths=1, edgecolors='g', alpha=.6))

    # Set limits
    ax.set_xlim([0, grid_size[0]])
    ax.set_ylim([0, grid_size[1]])
    ax.set_zlim([0, grid_size[2]])

    # Axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.draw()
    plt.pause(1)

def visualize_path_final(path, obstacles, grid_size):
    plt.clf()
    ax = plt.axes(projection='3d')

    # Visualize obstacles
    for obstacle in obstacles:
        faces = cube(obstacle, 1)
        ax.add_collection3d(Poly3DCollection(faces, facecolors='red', linewidths=1, edgecolors='r', alpha=.5))

    # Visualize the path
    for node in path:
        faces = cube(node, 1)
        ax.add_collection3d(Poly3DCollection(faces, facecolors='blue', linewidths=1, edgecolors='b', alpha=.6))

    # Set limits
    ax.set_xlim([0, grid_size[0]])
    ax.set_ylim([0, grid_size[1]])
    ax.set_zlim([0, grid_size[2]])

    # Axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show(block=True)
# A* Algorithm for a cubic 3D space with diagonal movements
def a_star(start, goal, obstacles, grid_size):
    # Possible movements in 3D (up, down, forward, backward, left, right, and diagonals)
    movements = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1),
                 (1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0),
                 (1, 0, 1), (1, 0, -1), (-1, 0, 1), (-1, 0, -1),
                 (0, 1, 1), (0, 1, -1), (0, -1, 1), (0, -1, -1),
                 (1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1),
                 (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]

    # Priority queue for nodes to explore
    open_list = []
    heapq.heappush(open_list, (0, start))  # (priority, node)

    # Dictionaries to keep track of the minimum cost and the path
    costs = {start: 0}
    path = {start: None}

    plt.ion()
    fig = plt.figure()

    while open_list:
        # Current node with the lowest cost
        _, current = heapq.heappop(open_list)

        # If we reach the goal node, reconstruct the path
        if current == goal:
            final_path = []
            while current is not None:
                final_path.append(current)
                current = path[current]
            return final_path[::-1]  # Return the path in reverse

        # Explore neighbors
        for movement in movements:
            neighbor = (current[0] + movement[0], current[1] + movement[1], current[2] + movement[2])

            # Check that the neighbor is within the grid limits and is not an obstacle
            if (0 <= neighbor[0] < grid_size[0] and
                    0 <= neighbor[1] < grid_size[1] and
                    0 <= neighbor[2] < grid_size[2] and
                    neighbor not in obstacles):

                new_cost = costs[current] + 1  # The cost of moving is always 1

                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    priority = new_cost + euclidean_distance(neighbor, goal)  # f(n) = g(n) + h(n)
                    heapq.heappush(open_list, (priority, neighbor))
                    path[neighbor] = current

        # Visualize the current state
        visualize_path(list(path.keys()), obstacles, grid_size, current)

    return None  # No path found

# Example usage
grid_size = (10, 10, 10)  # 3D grid 10x10x10
start = (0, 0, 0)
goal = (9, 9, 9)

# Define some obstacles in the grid
obstacles = [(5, 5, 5), (5, 5, 6), (5, 6, 5), (4, 5, 5), (5, 4, 5), (6, 5, 5),(5,5,4),(5,5,3),(5,5,2),(5,5,1),(5,5,0),(5,5,7),(5,5,8),(5,5,9)]

found_path = a_star(start, goal, obstacles, grid_size)

if found_path:
    print("Path found:", found_path)
    visualize_path_final(found_path, obstacles, grid_size)
else:
    print("No path found.")