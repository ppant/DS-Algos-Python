# Graph Algorithms

This directory contains Python implementations of common graph-based algorithms and data structures.

## Contents

- [Adjacency List Implementation](AdjacencyListGraphImple.py): Implements the Graph Abstract Data Type (ADT) using an adjacency list. Complexity: $O(V+E)$ for traversal.
- [Breadth First Search (BFS)](BFS.py): Implements BFS to solve the Word Ladder problem. Complexity: $O(V+E)$.
- [General Depth First Search (DFS)](DFSGeneral.py): Provides a general implementation of DFS. Complexity: $O(V+E)$.
- [DFS - Knight's Tour Problem](DFSImpleTheKnightsTourProblem.py): Another implementation of DFS specifically tailored to the Knight's Tour puzzle. Complexity: $O(k^N)$ where $k$ is the average branching factor.
- [The Knight's Tour Problem](TheKnightsTourProblem.py): Focuses on generating the knight's move graph and solving the tour using DFS and backtracking. Complexity: $O(k^N)$.
- [Word Ladder Problem](WordLadderProblem.py): Specifically focuses on building the word ladder graph. Complexity: $O(n \cdot L)$ where $n$ is number of words and $L$ is word length.
