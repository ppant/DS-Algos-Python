# Trees

This directory contains Python implementations of various tree-based data structures and algorithms.

## Contents

### Binary Search Trees (BST)
- [Binary Search Tree Implementation](BinarySearchTreesImple.py): A comprehensive implementation of a BST. Complexity: $O(\log n)$ average, $O(n)$ worst case for search/insert/delete.
- [Validate BST (Solution 1)](BinarySearchTreeCheckImpleSol1.py): Validates a BST using in-order traversal. Complexity: $O(n)$ time, $O(h)$ space.
- [Validate BST (Solution 2)](BinarySearchTreeCheckImpleSol2.py): Validates a BST using range checks. Complexity: $O(n)$ time, $O(h)$ space.
- [Trim a BST](TrimBinarySearchTreeImple.py): Trims a BST to a specified range $[min, max]$. Complexity: $O(n)$.

### Search Algorithms
- [Binary Search (Iterative)](BinarySearchImple.py): Iterative binary search on a sorted list. Complexity: $O(\log n)$.
- [Binary Search (Recursive)](BinarySearchRecursiveImple.py): Recursive binary search. Complexity: $O(\log n)$.

### Heaps
- [Binary Heap Implementation](BinaryHeapImple.py): Implements a min-heap. Complexity: $O(\log n)$ for `insert`/`delMin`, $O(n)$ for `buildHeap`.

### Tree Representations & Traversals
- [Nodes and References Representation](TreeRepresentationWithNodesReferences.py): Class-based nodes and references approach. Complexity: $O(1)$ for basic node operations.
- [List of Lists Representation](BuildTreeTest.py): Tree manipulation using a "list of lists" approach.
- [Tree Level Order Print](TreeLevelOrderPrintImple.py): Prints a binary tree in level order (BFS). Complexity: $O(n)$.
