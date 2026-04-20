# Trees

This directory contains Python implementations of various tree-based data structures and algorithms.

## Contents

### Binary Search Trees (BST)
- [Binary Search Tree Implementation](BinarySearchTreesImple.py): A comprehensive implementation of a BST including insertion, deletion, and search. Time Complexity: $O(h)$ where $h$ is the height of the tree.
- [Validate BST (Solution 1)](BinarySearchTreeCheckImpleSol1.py): Validates a BST by performing an in-order traversal and checking if the resulting values are sorted. Time Complexity: $O(n)$.
- [Validate BST (Solution 2)](BinarySearchTreeCheckImpleSol2.py): Validates a BST by keeping track of the minimum and maximum allowable values for each node. Time Complexity: $O(n)$.
- [Trim a BST](TrimBinarySearchTreeImple.py): Trims a BST so that all node values fall within a specified range $[min, max]$. Time Complexity: $O(n)$.

### Search Algorithms
- [Binary Search (Iterative)](BinarySearchImple.py): Iterative implementation of the binary search algorithm on a sorted list. Time Complexity: $O(\log n)$.
- [Binary Search (Recursive)](BinarySearchRecursiveImple.py): Recursive implementation of the binary search algorithm. Time Complexity: $O(\log n)$.

### Heaps
- [Binary Heap Implementation](BinaryHeapImple.py): Implements a min-heap using a recursive approach, including `insert`, `delMin`, and `buildHeap`. Time Complexity: $O(\log n)$ for `insert`/`delMin`, $O(n)$ for `buildHeap`.

### Tree Representations & Traversals
- [Nodes and References Representation](TreeRepresentationWithNodesReferences.py): A simple implementation of a binary tree using a class-based nodes and references approach. Time Complexity: $O(1)$ for basic operations.
- [List of Lists Representation](buildTreeTest.py): Demonstrates building and manipulating a tree using a "list of lists" approach. Time Complexity: $O(1)$ for basic operations.
- [Tree Level Order Print](TreeLevelOrderPrintImple.py): Prints a binary tree in level order (breadth-first) using a queue. Time Complexity: $O(n)$.
