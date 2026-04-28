# Graph Algorithms

This directory contains Python implementations of common graph-based algorithms and data structures.

## Contents

- [Adjacency List Implementation](AdjacencyListGraphImple.py): Implements the Graph Abstract Data Type (ADT) using an adjacency list (dictionaries in Python). Includes `Vertex` and `Graph` classes. $O(V + E)$
- [Breadth First Search (BFS)](BFS.py): Implements BFS to solve the Word Ladder problem, finding the shortest transformation path between words. $O(V + E)$
- [General Depth First Search (DFS)](DFSGeneral.py): Provides a general implementation of DFS, including discovery and finish times for vertices. $O(V + E)$
- [DFS - Knight's Tour Problem](DFSImpleTheKnightsTourProblem.py): Another implementation of DFS specifically tailored to the Knight's Tour puzzle. $O(V + E)$
- [The Knight's Tour Problem](TheKnightsTourProblem.py): Focuses on generating the knight's move graph and solving the tour using DFS and backtracking. $O(V + E)$
- [Word Ladder Problem](WordLadderProblem.py): Specifically focuses on building the word ladder graph where edges connect words that differ by only one letter. $O(V + E)$
