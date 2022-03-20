import queue
import sys
import math

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#struct to hold values needed for search alg
class vertex:
    priority = sys.maxsize
    coords =(-1,-1)
    visited = False
    prev = None
    dist = 0

    #allows us to use min heap ops in PriorityQueue
    def __lt__(self, other):
        return self.priority < other.priority



#returns true if a pixel meets vertex critieria
def isVertex(i, v):
    pixel = i.getpixel(v)
    return (pixel[0] >= 200  or pixel[1] >= 200 or pixel[2] >= 200)

#returns an array of all verticies in an image
def getVertices(maze):
    v = []
    for x in range(maze.size[0]):
        for y in range(maze.size[1]):
           if isVertex(maze,(x,y)):
               temp = vertex()
               temp.coords = (x,y)
               v.append(temp)
    return v

#returns an array of the locs in allVerticies of vertex's adjacent to vertex v
def getNeighbors(image,v,vertices):
    neighbors = []

    if v[0] < image.size[0] - 1 and isVertex(image,(v[0] + 1,v[1])):
        for i in range (0, len(vertices)):
            if vertices[i].coords == (v[0] + 1,v[1]):
                neighbors.append(i)
    if v[0] != 0 and isVertex(image,(v[0] - 1,v[1])):
        for i in range(0, len(vertices)):
            if vertices[i].coords == (v[0] - 1,v[1]):
                neighbors.append(i)
    if v[1] < image.size[0] - 1 and isVertex(image,(v[0],v[1] + 1)):
        for i in range(0, len(vertices)):
            if vertices[i].coords == (v[0],v[1] + 1):
                neighbors.append(i)
    if v[1] != 0 and isVertex(image,(v[0] ,v[1] - 1)):
        for i in range(0, len(vertices)):
            if vertices[i].coords == (v[0],v[1] - 1):
                neighbors.append(i)

    return neighbors

# calculates absolute shortest distance between two points, used for BestFS
def estimateDistanceLeft(v,t):
    return( abs(v.coords[0] - t.coords[0]) + abs(v.coords[1] - t.coords[1]) + v.dist)

#main search algo that searches an image for shortest path between s and t
def BreadthFirstSearch(image, s, t):
    q = queue.Queue()
    q.put(s)
    allVertices = getVertices(image)

    while( not q.empty() and not t.visited):
       u = q.get()

       neighborLocs = getNeighbors(image,u.coords,allVertices)

       for i in range(0,len(neighborLocs)):

           if not allVertices[neighborLocs[i]].visited:
               allVertices[neighborLocs[i]].visited = True
               allVertices[neighborLocs[i]].prev = u
               allVertices[neighborLocs[i]].dist = u.dist + 1
               if( allVertices[neighborLocs[i]].coords == t.coords):
                   t =  allVertices[neighborLocs[i]]
               image.putpixel(allVertices[neighborLocs[i]].coords, GREEN)
               q.put(allVertices[neighborLocs[i]])

    for i in range(0,len(allVertices)):
        if allVertices[i].coords == t.coords:
            t = allVertices[i]


    v = t
    print("Length of shortest path: ", v.dist)
    while(not v.coords == s.coords):
        image.putpixel(v.coords, RED)
        v = v.prev
    image.putpixel(v.coords, RED)

#similar to BFS but uses a PriorityQueue to prioritieze vertex that are more likely to be a part of shortest path
def BestFirstSearch(image, s, t):
    pq = queue.PriorityQueue()
    pq.put(s)
    allVertices = getVertices(image)

    while (not pq.empty() and not t.visited):
        u = pq.get()

        neighborLocs = getNeighbors(image, u.coords, allVertices)

        for i in range(0, len(neighborLocs)):

            if not allVertices[neighborLocs[i]].visited:
                allVertices[neighborLocs[i]].visited = True
                allVertices[neighborLocs[i]].prev = u
                allVertices[neighborLocs[i]].dist = u.dist + 1
                allVertices[neighborLocs[i]].priority = estimateDistanceLeft(allVertices[neighborLocs[i]],t)

                if (allVertices[neighborLocs[i]].coords == t.coords):
                    t = allVertices[neighborLocs[i]]
                image.putpixel(allVertices[neighborLocs[i]].coords, GREEN)

                pq.put(allVertices[neighborLocs[i]])

    for i in range(0, len(allVertices)):
        if allVertices[i].coords == t.coords:
            t = allVertices[i]

    v = t
    print("Length of shortest path: ", v.dist)

    while (not v.coords == s.coords):
        image.putpixel(v.coords, RED)
        v = v.prev
    image.putpixel(v.coords, RED)













