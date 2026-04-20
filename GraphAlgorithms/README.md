# Graph Algorithms

This directory contains Python implementations of common graph-based algorithms and data structures.

## Contents

- [Adjacency List Implementation](AdjacencyListGraphImple.py): Implements the Graph Abstract Data Type (ADT) using an adjacency list (dictionaries in Python). Time Complexity: $O(V+E)$.
- [Breadth First Search (BFS)](BFS.py): Implements BFS to solve the Word Ladder problem, finding the shortest transformation path between words. Time Complexity: $O(V+E)$.
- [General Depth First Search (DFS)](DFSGeneral.py): Provides a general implementation of DFS, including discovery and finish times for vertices. Time Complexity: $O(V+E)$.
- [DFS - Knight's Tour Problem](DFSImpleTheKnightsTourProblem.py): Implementation of DFS specifically tailored to the Knight's Tour puzzle. Time Complexity: $O(V+E)$.
- [The Knight's Tour Problem](TheKnightsTourProblem.py): Focuses on generating the knight's move graph and solving the tour. Time Complexity: $O(V+E)$.
- [Word Ladder Problem](WordLadderProblem.py): Specifically focuses on building the word ladder graph where edges connect words that differ by only one letter. Time Complexity: $O(n \cdot m^2)$ where $n$ is the number of words and $m$ is the word length.
