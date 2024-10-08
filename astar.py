import heapq
from utils import euclidean_distance
from visualization import visualize_path
import matplotlib.pyplot as plt

def a_star(start, goal, obstacles, grid_size):
    movements = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1),
                 (1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0),
                 (1, 0, 1), (1, 0, -1), (-1, 0, 1), (-1, 0, -1),
                 (0, 1, 1), (0, 1, -1), (0, -1, 1), (0, -1, -1),
                 (1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1),
                 (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]

    open_list = []
    heapq.heappush(open_list, (0, start))

    costs = {start: 0}
    path = {start: None}

    plt.ion()  # Enable interactive mode
    fig = plt.figure()

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            final_path = []
            while current is not None:
                final_path.append(current)
                current = path[current]
             # Disable interactive mode
            visualize_path(final_path,obstacles,grid_size)
            return final_path[::-1]

        for movement in movements:
            neighbor = (current[0] + movement[0], current[1] + movement[1], current[2] + movement[2])

            if (0 <= neighbor[0] < grid_size[0] and
                    0 <= neighbor[1] < grid_size[1] and
                    0 <= neighbor[2] < grid_size[2] and
                    neighbor not in obstacles):

                new_cost = costs[current] + 1

                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    priority = new_cost + euclidean_distance(neighbor, goal)
                    heapq.heappush(open_list, (priority, neighbor))
                    path[neighbor] = current

        # Visualize the current state of the path
        visualize_path(list(path.keys()), obstacles, grid_size, current)

    return None