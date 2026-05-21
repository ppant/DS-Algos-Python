# Trees

This directory contains Python implementations of various tree-based data structures and algorithms.

## Contents

### Binary Search Trees (BST)
- [Binary Search Tree Implementation](BinarySearchTreesImple.py): A comprehensive implementation of a BST. Complexity: $O(\log n)$ average, $O(n)$ worst case.
- [Validate BST (Solution 1)](BinarySearchTreeCheckImpleSol1.py): Validates a BST using in-order traversal. Complexity: $O(n)$.
- [Validate BST (Solution 2)](BinarySearchTreeCheckImpleSol2.py): Validates a BST using range check. Complexity: $O(n)$.
- [Trim a BST](TrimBinarySearchTreeImple.py): Trims a BST to a specified range. Complexity: $O(n)$.

### Search Algorithms
- [Binary Search (Iterative)](BinarySearchImple.py): Iterative binary search on a sorted list. Complexity: $O(\log n)$.
- [Binary Search (Recursive)](BinarySearchRecursiveImple.py): Recursive binary search. Complexity: $O(\log n)$.

### Heaps
- [Binary Heap Implementation](BinaryHeapImple.py): Min-heap implementation. Complexity: $O(\log n)$ for insert/delMin, $O(n)$ for buildHeap.

### Tree Representations & Traversals
- [Nodes and References Representation](TreeRepresentationWithNodesReferences.py): Simple binary tree using classes.
- [List of Lists Representation](BuildTreeTest.py): Tree using a "list of lists" approach.
- [Tree Level Order Print](TreeLevelOrderPrintImple.py): Level order traversal (BFS) using a queue. Complexity: $O(n)$.
