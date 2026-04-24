# Graph Algorithms

This directory contains Python implementations of common graph-based algorithms and data structures.

## Contents

- [Adjacency List Implementation](AdjacencyListGraphImple.py): Implements the Graph Abstract Data Type (ADT) using an adjacency list (dictionaries in Python). Includes `Vertex` and `Graph` classes. Complexity: $O(V+E)$ for traversal.
- [Breadth First Search (BFS)](BFS.py): Implements BFS to solve the Word Ladder problem, finding the shortest transformation path between words. Complexity: $O(V+E)$.
- [General Depth First Search (DFS)](DFSGeneral.py): Provides a general implementation of DFS, including discovery and finish times for vertices. Complexity: $O(V+E)$.
- [DFS - Knight's Tour Problem](DFSImpleTheKnightsTourProblem.py): Another implementation of DFS specifically tailored to the Knight's Tour puzzle. Complexity: $O(b^d)$ where $b$ is branching factor and $d$ is depth.
- [The Knight's Tour Problem](TheKnightsTourProblem.py): Focuses on generating the knight's move graph and solving the tour using DFS and backtracking. Complexity: $O(b^d)$.
- [Word Ladder Problem](WordLadderProblem.py): Specifically focuses on building the word ladder graph where edges connect words that differ by only one letter. Complexity: $O(n \cdot L^2)$ or $O(n \cdot L)$ where $n$ is number of words and $L$ is word length.
