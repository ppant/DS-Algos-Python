# Graph Algorithms

This directory contains Python implementations of common graph-based algorithms and data structures.

## Contents

- [Adjacency List Implementation](AdjacencyListGraphImple.py): Implements the Graph Abstract Data Type (ADT) using an adjacency list. Time Complexity: $O(1)$ to add a vertex, $O(1)$ to add an edge.
- [Breadth First Search (BFS)](BFS.py): Implements BFS to solve the Word Ladder problem. Time Complexity: $O(V+E)$.
- [General Depth First Search (DFS)](DFSGeneral.py): Provides a general implementation of DFS, including discovery and finish times. Time Complexity: $O(V+E)$.
- [DFS - Knight's Tour Problem](DFSImpleTheKnightsTourProblem.py): Specifically tailored DFS for the Knight's Tour puzzle. Time Complexity: $O(k^N)$ where $k$ is the constant number of moves and $N$ is the number of squares.
- [The Knight's Tour Problem](TheKnightsTourProblem.py): Generating the knight's move graph and solving the tour using DFS. Time Complexity: $O(V+E)$ for graph building.
- [Word Ladder Problem](WordLadderProblem.py): Specifically focuses on building the word ladder graph. Time Complexity: $O(n \cdot m^2)$ where $n$ is number of words and $m$ is word length.
