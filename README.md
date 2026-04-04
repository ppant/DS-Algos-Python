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

---

## 📖 Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Data Structures](#data-structures)
  - [Arrays](#arrays)
  - [Linked Lists](#linked-lists)
  - [Stacks](#stacks)
  - [Queues](#queues)
  - [Trees](#trees)
- [Algorithms](#algorithms)
  - [Sorting](#sorting)
  - [Recursion & Dynamic Programming](#recursion--dynamic-programming)
  - [Graph Algorithms](#graph-algorithms)
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
├── LinkedLists/         # 🔗 Singly and Doubly Linked Lists
├── Stacks/              # 📚 Stack implementations and applications
├── Queues/              # 📦 Queue implementations (FIFO)
├── deque/               # 🔄 Double-ended queue
├── Trees/               # 🌳 Binary Trees, BSTs, Heaps, and Traversals
├── Sorting/             # 📊 Common sorting algorithms
├── Recursion/           # 🔀 Recursive problems and Dynamic Programming
├── GraphAlgorithms/     # 🗺️ Graph traversal (BFS, DFS) and pathfinding
├── Error-debug/         # ⚠️ Error handling and debugging examples
└── README.md            # This file
```

---

## 📊 Data Structures

### Arrays 🔤
Common array-based algorithms and manipulations.
- [Anagram Check](Arrays/): Sorted & Manual solutions
- [Array Pair Sum](Arrays/ArrayPairSumSol.py): Find pairs that sum to k
- [Find Missing Element](Arrays/): XOR, Brute Force, Hash Table, Sum approaches

### Linked Lists 🔗
Implementations and problems involving linked structures.
- [Singly Linked List](LinkedLists/SingleLinkedListImple.py) & [Doubly Linked List](LinkedLists/DoublyLinkedListImple.py)
- [Cycle Detection](LinkedLists/SinglyLinkedListCycleCheckImple.py): Detect cycles using two pointers
- [Reverse Linked List](LinkedLists/LinkedListReversal.py): In-place reversal
- [Nth to Last Node](LinkedLists/LinkedListNthToLastNode.py): Find the n-th node from the end

### Stacks 📚
LIFO (Last-In-First-Out) data structures.
- [Stack Implementation](Stacks/StackImple.py): Basic operations (push, pop, peek)
- [Balanced Parentheses](Stacks/BalanceParenthlessCheckImple.py): Check for balanced brackets

### Queues 📦
FIFO (First-In-First-Out) data structures.
- [Queue Implementation](Queues/QueueImple.py): Basic operations (enqueue, dequeue)
- [Queue with Two Stacks](Queues/QueueWith2StacksImple.py): Implementing FIFO using LIFO structures

### Deque 🔄
Double-ended queue operations.
- [Deque Implementation](deque/DequeImple.py): Operations at both ends

### Trees 🌳
Hierarchical data structures.
- [Binary Search Tree](Trees/BinarySearchTreesImple.py): Complete BST implementation
- [Binary Heap](Trees/BinaryHeapImple.py): Min-heap implementation
- [BST Validation](Trees/BinarySearchTreeCheckImpleSol1.py): Multiple solutions
- [Tree Traversals](Trees/TreeLevelOrderPrintImple.py): Level order (BFS) printing
- [Trim BST](Trees/TrimBinarySearchTreeImple.py): Keep nodes within a range
- [Binary Search](Trees/BinarySearchImple.py): Iterative & Recursive approaches

---

## ⚡ Algorithms

### Sorting 📊
Algorithms for arranging elements in order.
- [Bubble Sort](Sorting/BubbleSortImple.py) - O(n²)
- [Selection Sort](Sorting/SelectionSortImple.py) - O(n²)
- [Insertion Sort](Sorting/InsertionSortImple.py) - O(n²)
- [Shell Sort](Sorting/ShellSortImple.py) - O(n log n)
- [Merge Sort](Sorting/MergeSortImple.py) - O(n log n)
- [Quick Sort](Sorting/QuickSortImple.py) - O(n log n) average

### Recursion & Dynamic Programming 🔀
Solving problems by breaking them into smaller sub-problems.
- [Fibonacci Sequence](Recursion/): Iterative, Recursive & DP solutions
- [Coin Change Problem](Recursion/): Recursive & DP approaches
- [String Operations](Recursion/): Reverse & Permutations
- [Word Split](Recursion/RecursionWordSplit.py): Dynamic Programming solution

### Graph Algorithms 🗺️
Algorithms for graph traversal and pathfinding.
- [Adjacency List](GraphAlgorithms/AdjacencyListGraphImple.py): Graph ADT
- [Breadth First Search (BFS)](GraphAlgorithms/BFS.py): Word Ladder problem
- [Depth First Search (DFS)](GraphAlgorithms/DFSGeneral.py): General & Knight's Tour

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