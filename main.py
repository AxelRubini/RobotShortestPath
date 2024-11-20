from BlankStack import BlankStack
from Robot import Robot
from astar import a_star
from visualization import visualize_path_final
from utils import convert_to_real_coordinates, smooth_path, world_discretizer
import Pallet
import csv

p1 = Pallet.Pallet(800,1200,1300,BlankStack(75,110,170))
print(p1.columns,p1.rows,len(p1.layers))
robot = Robot()
robot.Xcoordinate= 680
robot.layerScan(0,p1,BlankStack(75,110,170),450)
print(p1.layers)

grid_size = world_discretizer(2530,2650,2420,50)
start = (2, 1, 3)
goal = (9, 9, 9)
obstacles = [(5, 5, 5), (5, 5, 6), (5, 6, 5), (4, 5, 5), (5, 4, 5), (6, 5, 5), (5, 5, 4), (5, 5, 3), (5, 5, 2), (5, 5, 1), (5, 5, 0), (5, 5, 7), (5, 5, 8), (5, 5, 9)]

found_path = a_star(start, goal, obstacles, grid_size)

if found_path:

    real_path = convert_to_real_coordinates(found_path, 100)
    smooth_found_path = smooth_path(real_path)
    visualize_path_final(smooth_found_path, obstacles, grid_size)
else:
    print("No path found.")

with open("Output.csv","w",newline="") as csvfile:
    writer = csv.writer(csvfile)
    for points in real_path:
        writer.writerow([points[0],points[1],points[2],0,0,0])

csvfile.close()