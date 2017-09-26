# The knight tour problem

# Author: Pradeep K. Pant, ppant@cpan.org
# Ref: http://interactivepython.org/runestone/static/pythonds/Graphs/BuildingtheKnightsTourGraph.html

# The knight’s tour puzzle is played on a chess board with a single chess 
# piece, the knight. The object of the puzzle is to find a sequence of 
# moves that allow the knight to visit every square on the board exactly 
# once. One such sequence is called a “tour.”     
# we will solve the problem using two main steps:
# Represent the legal moves of a knight on a chessboard as a graph.
# Use a graph algorithm to find a path of length rows×columns−1rows×columns−1 
# where every vertex on the graph is visited exactly once.

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

# To represent the knight’s tour problem as a graph we will use the 
# following two ideas: Each square on the chessboard can be represented 
# as a node in the graph. Each legal move by the knight can be represented
# as an edge in the graph. 
def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row,col,bdSize)
            newPositions = genLegalMoves(row,col,bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0],e[1],bdSize)
                ktGraph.addEdge(nodeId,nid)
    return ktGraph

def posToNodeId(row, column, board_size):
    return (row * board_size) + column# Grpah class
# The genLegalMoves function takes the position of the knight on the 
# board and generates each of the eight possible moves. The legalCoord 
# helper function makes sure that a particular move that is generated is 
# still on the board.
def genLegalMoves(x,y,bdSize):
    newMoves = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX,bdSize) and \
                        legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

def legalCoord(x,bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False
    

   
# There are exactly 336 edges in the graph. Notice that the vertices 
# corresponding to the edges of the board have fewer connections 
# (legal moves) than the vertices in the middle of the board. Once 
# again we can see how sparse the graph is. If the graph was fully 
# connected there would be 4,096 edges. Since there are only 336 edges, 
# the adjacency matrix would be only 8.2 percent full.