# Trees

This directory contains Python implementations of various tree-based data structures and algorithms.

## Contents

### Binary Search Trees (BST)
- [Binary Search Tree Implementation](BinarySearchTreesImple.py): Comprehensive implementation of a BST. Time Complexity: $O(h)$ for search/insert/delete where $h$ is height of tree.
- [Validate BST (Solution 1)](BinarySearchTreeCheckImpleSol1.py): Validates a BST using in-order traversal. Time Complexity: $O(n)$.
- [Validate BST (Solution 2)](BinarySearchTreeCheckImpleSol2.py): Validates a BST using range checks. Time Complexity: $O(n)$.
- [Trim a BST](TrimBinarySearchTreeImple.py): Trims a BST to fall within a range $[min, max]$. Time Complexity: $O(n)$.

### Search Algorithms
- [Binary Search (Iterative)](BinarySearchImple.py): Iterative implementation of binary search. Time Complexity: $O(\log n)$.
- [Binary Search (Recursive)](BinarySearchRecursiveImple.py): Recursive implementation of binary search. Time Complexity: $O(\log n)$.

### Heaps
- [Binary Heap Implementation](BinaryHeapImple.py): Implements a min-heap. Time Complexity: $O(\log n)$ for insert/delMin, $O(n)$ for buildHeap.

### Tree Representations & Traversals
- [Nodes and References Representation](TreeRepresentationWithNodesReferences.py): Class-based binary tree implementation. Time Complexity: $O(1)$ for node creation.
- [List of Lists Representation](buildTreeTest.py): Tree manipulation using list of lists. Time Complexity: $O(1)$ for node creation.
- [Tree Level Order Print](TreeLevelOrderPrintImple.py): Prints a binary tree in level order. Time Complexity: $O(n)$.
