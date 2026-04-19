# Graph Algorithms

This directory contains Python implementations of common graph-based algorithms and data structures.

## Contents

- [Adjacency List Implementation](AdjacencyListGraphImple.py): Implements the Graph Abstract Data Type (ADT) using an adjacency list (dictionaries in Python). Includes `Vertex` and `Graph` classes.
- [Breadth First Search (BFS)](BFS.py): Implements BFS to solve the Word Ladder problem, finding the shortest transformation path between words. Time complexity: $O(V+E)$.
- [General Depth First Search (DFS)](DFSGeneral.py): Provides a general implementation of DFS, including discovery and finish times for vertices. Time complexity: $O(V+E)$.
- [DFS - Knight's Tour Problem](DFSImpleTheKnightsTourProblem.py): Another implementation of DFS specifically tailored to the Knight's Tour puzzle. Time complexity: $O(k^N)$ where $k$ is the branching factor and $N$ is the number of squares.
- [The Knight's Tour Problem](TheKnightsTourProblem.py): Focuses on generating the knight's move graph and solving the tour using DFS and backtracking.
- [Word Ladder Problem](WordLadderProblem.py): Specifically focuses on building the word ladder graph where edges connect words that differ by only one letter.
