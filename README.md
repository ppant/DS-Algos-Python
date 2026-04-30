# 📚 Data Structures and Algorithms using Python

> A comprehensive learning resource for implementing common data structures and algorithms in Python

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![GitHub Stars](https://img.shields.io/github/stars/ppant/DS-Algos-Python.svg?style=social)](https://github.com/ppant/DS-Algos-Python)

---

## 🎯 About This Repository

This repository was started in **2017** with a simple goal: to create a comprehensive, well-documented collection of Data Structures and Algorithms implementations in Python. Whether you're preparing for technical interviews, learning CS fundamentals, or just brushing up on your algo skills, this repo serves as a practical reference.

### Why This Repository?
- 📖 **Educational**: Each implementation is well-commented and easy to understand
- 🔄 **Multiple Solutions**: Different approaches to the same problem (brute force, optimized, etc.)
- 🎓 **Interview Ready**: Solutions for common technical interview questions
- 🚀 **Practical**: Standalone scripts that can be run and modified

---

## 🤝 Contributing

This is an open-source learning project! We welcome contributions from everyone:
- Found a bug? Open an issue
- Have a better solution? Submit a pull request
- Want to add new algorithms? Contributions are always appreciated!
- Have learning notes? Share them with the community

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

---

## 📖 Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Data Structures](#data-structures)
  - [Arrays](#arrays-)
  - [Linked Lists](#linked-lists-)
  - [Stacks](#stacks-)
  - [Queues](#queues-)
  - [Deque](#deque-)
  - [Trees](#trees-)
- [Algorithms](#algorithms)
  - [Sorting](#sorting-)
  - [Recursion & Dynamic Programming](#recursion--dynamic-programming)
  - [Graph Algorithms](#graph-algorithms-)
- [Error Handling & Debugging](#error-handling--debugging)
- [Usage](#usage)
- [Quick Reference](#quick-reference)
- [License](#license)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Basic understanding of Python syntax

### Running Examples

Most scripts in this repository are standalone and can be executed directly:

```bash
# Run any Python script
python3 Arrays/Anagram_Check_Sorted_Sol.py

# Or run from the repo root
python3 Sorting/BubbleSortImple.py
```

---

## 📁 Project Structure

```
.
├── Arrays/              # 🔤 Array-based problems and algorithms
├── Deque/               # 🔄 Double-ended queue
├── ErrorHandling/       # ⚠️ Error handling and debugging examples
├── GraphAlgorithms/     # 🗺️ Graph traversal (BFS, DFS) and pathfinding
├── LinkedLists/         # 🔗 Singly and Doubly Linked Lists
├── Queues/              # 📦 Queue implementations (FIFO)
├── Recursion/           # 🔀 Recursive problems and Dynamic Programming
├── Sorting/             # 📊 Common sorting algorithms
├── Stacks/              # 📚 Stack implementations and applications
├── Trees/               # 🌳 Binary Trees, BSTs, Heaps, and Traversals
├── CONTRIBUTING.md      # 🤝 Contribution guidelines
├── LICENSE              # 📄 MIT License
└── README.md            # 📖 This file
```

---

## 📊 Data Structures

### Arrays 🔤
Common array-based algorithms and manipulations.
- [Anagram Check](Arrays/): [Sorted](Arrays/Anagram_Check_Sorted_Sol.py) $O(n \log n)$ & [Manual](Arrays/Anagram_Check_manual_Sol.py) $O(n)$ solutions
- [Array Pair Sum](Arrays/ArrayPairSumSol.py): Find pairs that sum to $k$ in $O(n)$
- [Find Missing Element](Arrays/): [XOR](Arrays/ArrayFindTheMissingElement_XOR_sol.py) $O(n)$, [Brute Force](Arrays/ArrayFindTheMissingElement_brute_force_sol.py) $O(n \log n)$, [Hash Table](Arrays/ArrayFindTheMissingElement_hash_table_sol.py) $O(n)$, & [Sum](Arrays/ArrayFindTheMissingElement_takingSumandSubtract_sol.py) $O(n)$ approaches

### Linked Lists 🔗
Implementations and problems involving linked structures.
- [Singly Linked List](LinkedLists/SingleLinkedListImple.py) $O(1)$ insertion, $O(n)$ access & [Doubly Linked List](LinkedLists/DoublyLinkedListImple.py) $O(1)$ insertion/deletion
- [Cycle Detection](LinkedLists/SinglyLinkedListCycleCheckImple.py): Detect cycles in $O(n)$ time using Floyd's algorithm
- [Reverse Linked List](LinkedLists/LinkedListReversal.py): In-place reversal in $O(n)$
- [Nth to Last Node](LinkedLists/LinkedListNthToLastNode.py): Find the $n$-th node from the end in $O(n)$

### Stacks 📚
LIFO (Last-In-First-Out) data structures.
- [Stack Implementation](Stacks/StackImple.py): Basic operations (push, pop, peek) in $O(1)$
- [Balanced Parentheses](Stacks/BalanceParenthlessCheckImple.py): Check for balanced brackets in $O(n)$ using a stack

### Queues 📦
FIFO (First-In-First-Out) data structures.
- [Queue Implementation](Queues/QueueImple.py): $O(n)$ enqueue (using `insert(0)`) and $O(1)$ dequeue
- [Queue with Two Stacks](Queues/QueueWith2StacksImple.py): Implementing FIFO in $O(1)$ amortized time

### Deque 🔄
Double-ended queue operations.
- [Deque Implementation](Deque/DequeImple.py): $O(1)$ front operations, $O(n)$ rear operations (due to list shifting)

### Trees 🌳
Hierarchical data structures.
- [Binary Search Tree](Trees/BinarySearchTreesImple.py): $O(\log n)$ average, $O(n)$ worst-case for search, insert, delete
- [BST Validation](Trees/): [Solution 1 (In-order)](Trees/BinarySearchTreeCheckImpleSol1.py) $O(n)$ & [Solution 2 (Range check)](Trees/BinarySearchTreeCheckImpleSol2.py) $O(n)$
- [Binary Search](Trees/): [Iterative](Trees/BinarySearchImple.py) $O(\log n)$ & [Recursive](Trees/BinarySearchRecursiveImple.py) $O(\log n)$
- [Binary Heap](Trees/BinaryHeapImple.py): $O(\log n)$ for insert and delete-min
- [Tree Traversals](Trees/TreeLevelOrderPrintImple.py): Level order (BFS) printing in $O(n)$
- [Trim BST](Trees/TrimBinarySearchTreeImple.py): Keep nodes within a range in $O(n)$
- [Tree Representations](Trees/): [Nodes & References](Trees/TreeRepresentationWithNodesReferences.py) & [List of Lists](Trees/buildTreeTest.py)

---

## ⚡ Algorithms

### Sorting 📊
Algorithms for arranging elements in order.
- [Bubble Sort](Sorting/BubbleSortImple.py) - $O(n^2)$
- [Selection Sort](Sorting/SelectionSortImple.py) - $O(n^2)$
- [Insertion Sort](Sorting/InsertionSortImple.py) - $O(n^2)$
- [Shell Sort](Sorting/ShellSortImple.py) - $O(n^2)$ worst-case
- [Merge Sort](Sorting/MergeSortImple.py) - $O(n \log n)$
- [Quick Sort](Sorting/QuickSortImple.py) - $O(n \log n)$ average

### Recursion & Dynamic Programming 🔀
Solving problems by breaking them into smaller sub-problems.
- [Fibonacci Sequence](Recursion/): [Iterative](Recursion/FibonacciSeqIterative.py) $O(n)$, [Recursive](Recursion/FibonacciSeqRecursion.py) $O(2^n)$, & [Dynamic Programming](Recursion/FibonacciSeqDynamic.py) $O(n)$
- [Coin Change Problem](Recursion/): [Recursive](Recursion/CoinChangeProblemRecursion.py) $O(2^n)$ & [Dynamic Programming](Recursion/CoinChangeProblemDynamic.py) $O(n \cdot m)$
- [String Operations](Recursion/): [Reverse](Recursion/RecursionReverseStr.py) $O(n)$ & [Permutations](Recursion/RecursionStrPermutation.py) $O(n!)$
- [Math Operations](Recursion/): [Cumulative Sum](Recursion/RecursionCumulativeSum.py) $O(n)$ & [Sum of Digits](Recursion/RecursionSumOfDigits.py) $O(n)$
- [Word Split](Recursion/RecursionWordSplit.py): $O(n^2)$ recursive solution

### Graph Algorithms 🗺️
Algorithms for graph traversal and pathfinding.
- [Adjacency List](GraphAlgorithms/AdjacencyListGraphImple.py): $O(1)$ to add vertex, $O(1)$ to add edge
- [Breadth First Search (BFS)](GraphAlgorithms/BFS.py): Word Ladder problem in $O(V+E)$
- [Depth First Search (DFS)](GraphAlgorithms/DFSGeneral.py): General DFS implementation in $O(V+E)$
- [Knight's Tour Problem](GraphAlgorithms/): [Graph Generation](GraphAlgorithms/TheKnightsTourProblem.py) & [DFS Solution](GraphAlgorithms/DFSImpleTheKnightsTourProblem.py) in $O(k^N)$ where $k$ is branching factor
- [Word Ladder Problem](GraphAlgorithms/WordLadderProblem.py): Building the word ladder graph in $O(n \cdot k^2)$ where $k$ is word length

---

## ⚠️ Error Handling & Debugging

- [Error and Exceptions](ErrorHandling/ErrorExceptions.py): Demonstrates `try`, `except`, `else`, and `finally` blocks for robust error handling.

---

## 📖 Usage

Most scripts in this repository are standalone. You can run them using the Python 3 interpreter:

```bash
python3 path/to/script.py
```

Example:
```bash
python3 Sorting/BubbleSortImple.py
```

---

## 📊 Quick Reference

| Topic | Easy | Medium | Hard |
|-------|------|--------|------|
| Arrays | Anagram Check | Array Pair Sum | Find Missing Element |
| Linked Lists | Singly LL | Cycle Detection | Reverse LL |
| Trees | Binary Search | BST Validation | Trim BST |
| Sorting | Bubble Sort | Merge Sort | Quick Sort |
| DP | Fibonacci | Coin Change | Word Split |

---

## 🎓 Learning Path

New to DSA? Follow this recommended order:
1. Start with **Arrays** - Fundamental data structure
2. Learn **Sorting** - Essential for interviews
3. Study **Linked Lists** - Understanding pointers/references
4. Master **Stacks & Queues** - Core data structures
5. Explore **Trees** - Most interview questions
6. Dive into **Recursion & DP** - Advanced problem solving
7. Finish with **Graphs** - Complex algorithms

---

## 🔮 Roadmap

- [ ] Add more graph algorithms (Dijkstra, Bellman-Ford)
- [ ] Include complexity analysis for each solution
- [ ] Add interactive examples/visualizations
- [ ] Create a difficulty level classification
- [ ] Add more test cases
- [ ] Create beginner-friendly guides

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
Copyright (c) 2017 - 2026 Pradeep K. Pant
```

---

## 👨‍💻 Author

**Pradeep K. Pant**
- Started: 2017
- Python enthusiast | Algorithm lover | Open source advocate

---

## ⭐ Show Your Support

If this repository helped you learn or prepare for interviews, please consider:
- ⭐ Starring the repository
- 🤝 Contributing improvements
- 📢 Sharing with others learning DSA
- 💬 Giving feedback

---

*Happy Learning! 🚀*
