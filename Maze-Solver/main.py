# Created by: Andrew McKernan
# Date: 11/20/21
# Summary: This project reads in a maze.bmp and calculates the shortest path between two points. There are two algorithms
#          used here. Breadth First search is a normal shortest path alg similar to djikstras, Best First Search leverages
#          a priority queue with priority of anticipated distance to destination that allows it to visit less nodes than BFS

from PIL import Image
from searchAlgs import *

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

m1 = input("Please enter maze file name\n")
startLoc = input("Please enter starting vertex row and col ex: 14 22\n").split(' ')
endLoc = input("Please enter destination pixel row and col ex: 14 22\n").split(' ')

#m1 = "maze1.bmp"


#m1 (4,0)
#m2 (1,0)
s = vertex()
s.coords = (int(startLoc[0]),int(startLoc[1]))
t = vertex()

#m1(16,31)
#m2(30,31)
t.coords = (int(endLoc[0]),int(endLoc[1]))
maze = Image.open(m1)

breadthOut = input("Please enter out file name of Breadth First Search\n")
bestOut = input("Please enter out file name of Best First Search\n")



BestFirstSearch(maze,s,t)
maze.save(bestOut)
BreadthFirstSearch(maze,s,t)
maze.save(breadthOut)

