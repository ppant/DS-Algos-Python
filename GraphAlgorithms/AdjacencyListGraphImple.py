# Graph Implementation - Adjacency list

# Author: Pradeep K. Pant, ppant@cpan.org
# Ref: http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html

# * We'll use dictionaries to implement the adjacency list in Python which is the easiest way. 
# * To implement the Graph ADT we'll create two classes, Graph, which holds the master list of 
#   vertices, and Vertex, which will represent each vertex in the graph.
# * Each Vertex uses a dictionary to keep track of the vertices to which it is connected, and the weight of each edge. This dictionary is called connectedTo. 

# Vetex class
class Vertex:
    # constructor simply initializes the id, which will typically be a string
    # and the connectedTo dictionary
    def __init__(self,key): 
        self.id = key
        self.connectedTo = {}
    # add a connection from this vertex to another
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    # returns all of the vertices in the adjacency list, as represented by the 
    # connectedTo instance variable
    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id
    # returns the weight of the edge from this vertex to the vertex passed as a parameter
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

# Grpah class
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

# Test
# Now using the Graph and Vertex classes just defined we'll create a 
# graph. First we create six vertices numbered 0 through 5. Then we 
# display the vertex dictionary. Notice that for each key 0 through 5 
# we have created an instance of a Vertex. Next, we add the edges that connect 
# the vertices together. Finally, a nested loop verifies that each edge in the 
# graph is properly stored. 

# create six vertices numbered 0 through 5. 
# Then we display the vertex dictionary
g = Graph()
for i in range(6):
    g.addVertex(i)

print(g.vertList)
# {0: <__main__.Vertex object at 0x00000193B2E2CAC8>, 
# 1: <__main__.Vertex object at 0x00000193B2E2CB00>, 
# 2: <__main__.Vertex object at 0x00000193B2E2CB38>, 
# 3: <__main__.Vertex object at 0x00000193B2E2CB70>, 
# 4: <__main__.Vertex object at 0x00000193B2E2CBA8>, 
# 5: <__main__.Vertex object at 0x00000193B2E2CA20>}
#add the edges that connect the vertices together
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
# Nested loop verifies that each edge in the graph is properly stored. 
for v in g:
   for w in v.getConnections():
       print("( %s , %s )" % (v.getId(), w.getId()))
       
# Result
#( 0 , 5 )
#( 0 , 1 )
#( 1 , 2 )
#( 2 , 3 )
#( 3 , 5 )
#( 3 , 4 )
#( 4 , 0 )
#( 5 , 2 )
#( 5 , 4 )
 
