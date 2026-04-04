# Graph Word ladder problem: Building the Word Ladder Graph

# Author: Pradeep K. Pant, ppant@cpan.org
# Ref: http://interactivepython.org/runestone/static/pythonds/Graphs/BuildingtheWordLadderGraph.html

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.distance = 0
        self.pred = None

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setDistance(self, d):
        self.distance = d

    def getDistance(self):
        return self.distance

    def setPred(self, p):
        self.pred = p

    def getPred(self):
        return self.pred

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')

def traverse(y):
    x = y
    path = []
    while (x and x.getPred()):
        path.append(x.getId())
        x = x.getPred()
    if x:
        path.append(x.getId())
    print(" -> ".join(path[::-1]))

# Test
g = Graph()
words = ["FOOL", "POOL", "POLL", "POLE", "PALE", "SALE", "SAGE"]
for i in range(len(words)-1):
    g.addEdge(words[i], words[i+1])
    g.addEdge(words[i+1], words[i]) # Bidirectional for word ladder

bfs(g, g.getVertex('FOOL'))
print("Path from FOOL to SAGE:")
traverse(g.getVertex('SAGE'))
