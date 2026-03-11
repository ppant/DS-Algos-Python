# Data Structures and Algorithms using Python

A comprehensive collection of fundamental data structures and algorithms implemented in Python 3. This repository serves as a reference for common programming problems and their solutions, covering everything from basic array manipulations to complex graph algorithms.

## 📁 Project Structure

```text
.
├── Arrays/             # Array-based problems (Anagrams, Finding missing elements, etc.)
├── deque/              # Double-ended queue implementation
├── Error-debug/        # Examples of error handling and debugging in Python
├── GraphAlgorithms/    # BFS, DFS, Word Ladder, Knight's Tour
├── LinkedLists/        # Singly and Doubly Linked Lists, Reversal, Cycle detection
├── Queues/             # Queue implementation and Queues using Stacks
├── Recursion/          # Cumulative sum, Factorial, Fibonacci, Coin change, etc.
├── Sorting/            # Bubble, Selection, Insertion, Merge, Quick, and Shell sorts
├── Stacks/             # Stack implementation and Balanced Parentheses check
└── Trees/              # Binary Trees, BSTs, Heaps, Tree Traversal, and Balancing
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x

### Usage
Each script is designed to be standalone. You can run any file directly using the Python interpreter:

```bash
python Arrays/ArrayPairSumSol.py
```

Most files include test cases or example usage at the bottom, so you can see the algorithm in action immediately upon execution.

---

## 📚 Contents

### [Arrays](./Arrays)
- **Anagram Check**: Determine if two strings are anagrams.
- **Array Pair Sum**: Find unique pairs that sum up to a value `k`.
- **Find Missing Element**: Multiple solutions (XOR, Hash Table, Sum) to find a missing element in a shuffled array.

### [Linked Lists](./LinkedLists)
- **Singly & Doubly Linked Lists**: Basic implementations.
- **Cycle Check**: Detect cycles using Floyd's Cycle-Finding Algorithm.
- **Reversal**: In-place reversal of a linked list.
- **Nth to Last Node**: Locate the Nth node from the end.

### [Stacks](./Stacks)
- **Stack Implementation**: Standard LIFO operations.
- **Balanced Parentheses**: Algorithm to check for balanced brackets in an expression.

### [Queues & Deques](./Queues)
- **Queue Implementation**: Standard FIFO operations.
- **Queue with Two Stacks**: Implementation of a queue using two stacks.
- **Deque**: Double-ended queue implementation in [deque/](./deque).

### [Recursion](./Recursion)
- **Fibonacci Sequence**: Iterative, Recursive, and Dynamic Programming (Memoization) approaches.
- **Coin Change Problem**: Finding the minimum number of coins for change.
- **Permutations**: Generating all permutations of a string.
- **Cumulative Sum & Sum of Digits**: Basic recursive exercises.

### [Trees](./Trees)
- **Binary Search Tree (BST)**: Implementation and validation.
- **Binary Heap**: Implementation of a priority queue using a heap.
- **Tree Traversal**: Level order print and other traversal methods.
- **BST Trimming**: Removing nodes outside a specific range.
- **Build Tree**: Example of building a tree using lists in `buildTreeTest.py`.

### [Sorting](./Sorting)
Implementations with complexity analysis:
- **Bubble Sort**: $O(n^2)$
- **Selection Sort**: $O(n^2)$
- **Insertion Sort**: $O(n^2)$
- **Merge Sort**: $O(n \log n)$
- **Quick Sort**: $O(n \log n)$
- **Shell Sort**: $O(n \log n)$ to $O(n^2)$

### [Graph Algorithms](./GraphAlgorithms)
- **Adjacency List**: Standard graph representation.
- **BFS & DFS**: Breadth-First and Depth-First Search implementations.
- **Word Ladder Problem**: Application of BFS.
- **Knight's Tour**: Application of DFS.

### [Error Handling](./Error-debug)
- **Exception Handling**: Demonstration of `try-except-else-finally` blocks.

---

## 🎓 Acknowledgments
- Inspired by the Udemy course "Python for Data Structures, Algorithms, and Interviews".
- "Problem Solving with Algorithms and Data Structures using Python" by Bradley N. Miller and David L. Ranum.

---
*Author: Pradeep K. Pant*
