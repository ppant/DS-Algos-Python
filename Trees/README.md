# Trees

This directory contains Python implementations of various tree-based data structures and algorithms.

## Contents

### Binary Search Trees (BST)
- [Binary Search Tree Implementation](BinarySearchTreesImple.py): A comprehensive implementation of a BST ($O(\log n)$ average, $O(n)$ worst).
- [Validate BST (Solution 1)](BinarySearchTreeCheckImpleSol1.py): Validates a BST by performing an in-order traversal ($O(n)$).
- [Validate BST (Solution 2)](BinarySearchTreeCheckImpleSol2.py): Validates a BST by keeping track of the minimum and maximum allowable values ($O(n)$).
- [Trim a BST](TrimBinarySearchTreeImple.py): Trims a BST so that all node values fall within a specified range ($O(n)$).

### Search Algorithms
- [Binary Search (Iterative)](BinarySearchImple.py): Iterative implementation of the binary search algorithm ($O(\log n)$).
- [Binary Search (Recursive)](BinarySearchRecursiveImple.py): Recursive implementation of the binary search algorithm ($O(\log n)$).

### Heaps
- [Binary Heap Implementation](BinaryHeapImple.py): Implements a min-heap, including `insert` ($O(\log n)$) and `delMin` ($O(\log n)$).

### Tree Representations & Traversals
- [Nodes and References Representation](TreeRepresentationWithNodesReferences.py): A simple implementation of a binary tree using a class-based nodes and references approach.
- [List of Lists Representation](BuildTreeTest.py): Demonstrates building and manipulating a tree using a "list of lists" approach.
- [Tree Level Order Print](TreeLevelOrderPrintImple.py): Prints a binary tree in level order ($O(n)$).
