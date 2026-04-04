# Data Structures and Algorithms using Python

This repository contains a collection of common programming problems and data structure implementations in Python 3. It is designed to serve as a reference for students and developers preparing for technical interviews or interested in fundamental computer science concepts.

## Table of Contents

- [Project Structure](#project-structure)
- [Data Structures](#data-structures)
  - [Arrays](#arrays)
  - [Linked Lists](#linked-lists)
  - [Stacks](#stacks)
  - [Queues](#queues)
  - [Deque](#deque)
  - [Trees](#trees)
- [Algorithms](#algorithms)
  - [Recursion](#recursion)
  - [Sorting](#sorting)
  - [Graph Algorithms](#graph-algorithms)
- [Error Handling](#error-handling)
- [Usage](#usage)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [License](#license)

---

## Usage

Most scripts in this repository are standalone and can be executed directly using the Python 3 interpreter.

Example:
```bash
python3 Arrays/Anagram_Check_Sorted_Sol.py
```

---

## Project Structure

The repository is organized into categorical directories, each containing relevant implementations and a dedicated `README.md` for more details.

```text
.
├── Arrays/             # Array-based problems and algorithms
├── Error-debug/        # Examples of error handling and debugging
├── GraphAlgorithms/    # Graphs, BFS, DFS, and related problems
├── LinkedLists/        # Singly and Doubly Linked Lists
├── Queues/             # Queue implementations
├── Recursion/          # Recursive problems and Dynamic Programming
├── Sorting/            # Common sorting algorithms
├── Stacks/             # Stack implementations and applications
├── Trees/              # Binary Trees, BSTs, and Heaps
└── deque/              # Double-ended queue implementation
```

---

## Data Structures

### Arrays
Common array-based algorithms and manipulations.
- [Anagram Check](Arrays/): [Sorted Solution](Arrays/Anagram_Check_Sorted_Sol.py), [Manual Solution](Arrays/Anagram_Check_manual_Sol.py)
- [Array Pair Sum](Arrays/ArrayPairSumSol.py): Find unique pairs that sum to $k$.
- [Find Missing Element](Arrays/): [XOR](Arrays/ArrayFindTheMissingElement_XOR_sol.py), [Brute Force](Arrays/ArrayFindTheMissingElement_brute_force_sol.py), [Hash Table](Arrays/ArrayFindTheMissingElement_hash_table_sol.py), [Sum/Subtract](Arrays/ArrayFindTheMissingElement_takingSumandSubtract_sol.py)

### Linked Lists
Implementations and problems involving linked structures.
- [Singly Linked List](LinkedLists/SingleLinkedListImple.py) & [Doubly Linked List](LinkedLists/DoublyLinkedListImple.py)
- [Cycle Check](LinkedLists/SinglyLinkedListCycleCheckImple.py): Detect cycles using two pointers.
- [Reverse Linked List](LinkedLists/LinkedListReversal.py): In-place reversal.
- [Nth to Last Node](LinkedLists/LinkedListNthToLastNode.py): Find the $n$-th node from the end.

### Stacks
LIFO (Last-In-First-Out) data structures.
- [Stack Implementation](Stacks/StackImple.py): Basic operations (`push`, `pop`, `peek`).
- [Balanced Parentheses](Stacks/BalanceParenthlessCheckImple.py): Check for balanced brackets in a string.

### Queues
FIFO (First-In-First-Out) data structures.
- [Queue Implementation](Queues/QueueImple.py): Basic operations (`enqueue`, `dequeue`).
- [Queue with Two Stacks](Queues/QueueWith2StacksImple.py): Implementing FIFO using two LIFO stacks.

### Deque
Double-ended queue operations.
- [Deque Implementation](deque/DequeImple.py): Operations at both ends (`addFront`, `addRear`, etc.).

### Trees
Hierarchical data structures.
- [Binary Search Tree (BST)](Trees/BinarySearchTreesImple.py): Full implementation.
- [Binary Heap](Trees/BinaryHeapImple.py): Min-heap implementation.
- [Validate BST](Trees/): [Solution 1](Trees/BinarySearchTreeCheckImpleSol1.py), [Solution 2](Trees/BinarySearchTreeCheckImpleSol2.py)
- [Binary Search](Trees/): [Iterative](Trees/BinarySearchImple.py), [Recursive](Trees/BinarySearchRecursiveImple.py)
- [Tree Traversals](Trees/TreeLevelOrderPrintImple.py): Level order (BFS) printing.
- [Trim a BST](Trees/TrimBinarySearchTreeImple.py): Keep nodes within a range.
- [Representations](Trees/): [Nodes & References](Trees/TreeRepresentationWithNodesReferences.py), [List of Lists](Trees/buildTreeTest.py)

---

## Algorithms

### Recursion
Solving problems by breaking them into smaller sub-problems.
- [Fibonacci Sequence](Recursion/): [Iterative](Recursion/FibonacciSeqIterative.py), [Recursive](Recursion/FibonacciSeqRecursion.py), [Dynamic Programming](Recursion/FibonacciSeqDynamic.py)
- [Coin Change](Recursion/): [Recursive](Recursion/CoinChangeProblemRecursion.py), [Dynamic Programming](Recursion/CoinChangeProblemDynamic.py)
- [String Operations](Recursion/): [Reverse String](Recursion/RecursionReverseStr.py), [Permutations](Recursion/RecursionStrPermutation.py)
- [Math & Misc](Recursion/): [Cumulative Sum](Recursion/RecursionCumulativeSum.py), [Sum of Digits](Recursion/RecursionSumOfDigits.py), [Word Split](Recursion/RecursionWordSplit.py)

### Sorting
Algorithms for arranging elements in a specific order.
- [Bubble Sort](Sorting/BubbleSortImple.py)
- [Selection Sort](Sorting/SelectionSortImple.py)
- [Insertion Sort](Sorting/InsertionSortImple.py)
- [Shell Sort](Sorting/ShellSortImple.py)
- [Merge Sort](Sorting/MergeSortImple.py)
- [Quick Sort](Sorting/QuickSortImple.py)

### Graph Algorithms
Algorithms for graph traversal and pathfinding.
- [Adjacency List](GraphAlgorithms/AdjacencyListGraphImple.py): Graph ADT implementation.
- [Breadth First Search (BFS)](GraphAlgorithms/BFS.py): Word Ladder problem.
- [Depth First Search (DFS)](GraphAlgorithms/DFSGeneral.py): General implementation and [Knight's Tour](GraphAlgorithms/TheKnightsTourProblem.py).

---

## Error Handling

Examples of robust error handling in Python.
- [Exceptions](Error-debug/ErrorExceptions.py): `try-except-else-finally` blocks and input validation.

### Build Tree (List of Lists)
Building a tree using a list-of-lists representation.
- **File**: `Trees/buildTreeTest.py`

### Tree Build Test
Test implementation for building trees using a list-of-lists approach.
- **File**: `Trees/buildTreeTest.py`

### Tree Representation (List of Lists)
Implementing a tree using list-of-lists approach.
- **File**: `Trees/buildTreeTest.py`

### Build Tree Test
Test script for building trees.
- **File**: `Trees/buildTreeTest.py`

### Tree Representation (List of Lists)
Building a tree and manipulating it using a list of lists.
- **File**: `Trees/buildTreeTest.py`

### Build Tree Test
Build a tree and fetch nodes and insert using list of lists.
- **File**: `Trees/buildTreeTest.py`

### Build Tree Test
Demonstrates building a tree and manipulating nodes using a list-of-lists approach.
- **File**: `Trees/buildTreeTest.py`

---

## Usage

Most scripts are standalone. You can run them using the Python 3 interpreter:

```bash
python3 path/to/script.py
```

Example:
```bash
python3 Sorting/BubbleSortImple.py
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Copyright (c) 2007 - 2026 Pradeep K. Pant

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Author: Pradeep K. Pant*
