from astar import a_star
from visualization import visualize_path_final
from utils import convert_to_real_coordinates, smooth_path
import matplotlib.pyplot as plt
import csv

grid_size = (10, 10, 10)
start = (0, 0, 0)
goal = (9, 9, 9)
obstacles = [(5, 5, 5), (5, 5, 6), (5, 6, 5), (4, 5, 5), (5, 4, 5), (6, 5, 5), (5, 5, 4), (5, 5, 3), (5, 5, 2), (5, 5, 1), (5, 5, 0), (5, 5, 7), (5, 5, 8), (5, 5, 9)]

found_path = a_star(start, goal, obstacles, grid_size)

if found_path:

    real_path = convert_to_real_coordinates(found_path, 10)
    smooth_found_path = smooth_path(real_path)
    print("Path found:", found_path, "Smoothed path:", smooth_found_path, "Real path:", real_path)
    visualize_path_final(smooth_found_path, obstacles, grid_size)
else:
    print("No path found.")

with open("Output.csv","w",newline="") as csvfile:
    writer = csv.writer(csvfile)
    for points in smooth_found_path:
        writer.writerow([points[0],points[1],points[2],0,0,0])
    csvfile.close()