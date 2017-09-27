# The knight tour problem: depth first search (DFS) Implementation

# Author: Pradeep K. Pant, ppant@cpan.org
# Ref: http://interactivepython.org/runestone/static/pythonds/Graphs/ImplementingKnightsTour.html

# The knight’s tour is a special case of a depth first search where the goal is to create 
# the deepest depth first tree, without any branches. The more general depth first search 
# is actually easier. Its goal is to search as deeply as possible, connecting as many nodes 
# in the graph as possible and branching where necessary. 
# It is even possible that a depth first search will create more than one tree. When the 
# depth first search algorithm creates a group of trees we call this a depth first forest. 
# As with the breadth first search our depth first search makes use of predecessor links to 
# construct the tree. In addition, the depth first search will make use of two additional 
# instance variables in the Vertex class. The new instance variables are the discovery and 
# finish times. The discovery time tracks the number of steps in the algorithm before a 
# vertex is first encountered. The finish time is the number of steps in the algorithm 
# before a vertex is colored black. As we will see after looking at the algorithm, the 
# discovery and finish times of the nodes provide some interesting properties we can use 
# in later algorithms.

# Graph class
# The Graph class, contains a dictionary that maps vertex names to vertex objects.
# Graph() creates a new, empty graph.
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    # adds an instance of Vertex to the graph
    # addVertex(vert)
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    # finds the vertex in the graph named vertKey.
    # getVertex(vertKey)
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList
    # Adds a new, directed edge to the graph that connects two vertices
    # addEdge(fromVert, toVert)
    # addEdge(fromVert, toVert, weight) Adds a new, weighted, directed edge to 
    # the graph that connects two vertices.
    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
    # getVertices() returns the list of all vertices in the graph.
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

# In code below since the two functions dfs and its helper dfsvisit use a variable to keep 
# track of the time across calls to dfsvisit we chose to implement the code as methods of 
# a class that inherits from the Graph class. This implementation extends the graph class 
# by adding a time instance variable and the two methods dfs and dfsvisit. Looking at line 
# 84 you will notice that the dfs method iterates over all of the vertices in the graph 
# calling dfsvisit on the nodes that are white. The reason we iterate over all the nodes, 
# rather than simply searching from a chosen starting node, is to make sure that all nodes 
# in the graph are considered and that no vertices are left out of the depth first forest. 
# It may look unusual to see the statement for aVertex in self, but remember that in this 
# case self is an instance of the DFSGraph class, and iterating over all the vertices in 
# an instance of a graph is a natural thing to do.


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

# The general running time for depth first search is as follows. The loops in dfs both 
# run in O(V), not counting what happens in dfsvisit, since they are executed once for 
# each vertex in the graph. In dfsvisit the loop is executed once for each edge in the 
# adjacency list of the current vertex. Since dfsvisit is only called recursively if the 
# vertex is white, the loop will execute a maximum of once for every edge in the graph or 
# O(E). So, the total time for depth first search is O(V+E).

