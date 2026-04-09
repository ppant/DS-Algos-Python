# Trees

This directory contains Python implementations of various tree-based data structures and algorithms.

## Contents

### Binary Search Trees (BST)
- [Binary Search Tree Implementation](BinarySearchTreesImple.py): A comprehensive implementation of a BST with `TreeNode` and `BinarySearchTree` classes, including insertion, deletion, and search. Complexity: $O(h)$.
- [Validate BST (Solution 1)](BinarySearchTreeCheckImpleSol1.py): Validates a BST by performing an in-order traversal and checking if the resulting values are sorted. Complexity: $O(n)$.
- [Validate BST (Solution 2)](BinarySearchTreeCheckImpleSol2.py): Validates a BST by keeping track of the minimum and maximum allowable values for each node. Complexity: $O(n)$.
- [Trim a BST](TrimBinarySearchTreeImple.py): Trims a BST so that all node values fall within a specified range $[min, max]$. Complexity: $O(n)$.

### Heaps
- [Binary Heap Implementation](BinaryHeapImple.py): Implements a min-heap, including `insert`, `delMin`, and `buildHeap`. Complexity: $O(\log n)$ for insert/delete, $O(n)$ for buildHeap.

### Tree Representations & Traversals
- [Nodes and References Representation](TreeRepresentationWithNodesReferences.py): A simple implementation of a binary tree using a class-based nodes and references approach.
- [List of Lists Representation](buildTreeTest.py): Demonstrates building and manipulating a tree using a "list of lists" approach.
- [Tree Level Order Print](TreeLevelOrderPrintImple.py): Prints a binary tree in level order (breadth-first) using a queue. Complexity: $O(n)$.
