# Data Structures and Algorithms using Python

This repository contains a collection of common programming problems and data structure implementations in Python.

## Table of Contents
- [Arrays](#arrays)
- [Linked Lists](#linked-lists)
- [Stacks](#stacks)
- [Queues](#queues)
- [Deque](#deque)
- [Recursion](#recursion)
- [Trees](#trees)
- [Sorting](#sorting)
- [Graph Algorithms](#graph-algorithms)
- [Error Handling](#error-handling)
- [Acknowledgments](#acknowledgments)

---

## Arrays

### Anagram Check
Checks if two strings are anagrams of each other.
- **Files**: `Arrays/Anagram_Check_Sorted_Sol.py`, `Arrays/Anagram_Check_manual_Sol.py`

### Array Pair Sum
Given an integer array, output all unique pairs that sum up to a specific value `k`.
- **File**: `Arrays/ArrayPairSumSol.py`

### Find Missing Element
Find the missing element in a shuffled second array.
- **Files**: `Arrays/ArrayFindTheMissingElement_XOR_sol.py`, `Arrays/ArrayFindTheMissingElement_brute_force_sol.py`, `Arrays/ArrayFindTheMissingElement_hash_table_sol.py`, `Arrays/ArrayFindTheMissingElement_takingSumandSubtract_sol.py`

---

## Linked Lists

### Singly Linked List Implementation
Basic skeleton for a Singly Linked List.
- **File**: `LinkedLists/SingleLinkedListImple.py`

### Doubly Linked List Implementation
Basic skeleton for a Doubly Linked List.
- **File**: `LinkedLists/DoublyLinkedListImple.py`

### Singly Linked List Cycle Check
Check if a singly linked list contains a cycle using the "two runners" (slow and fast pointers) strategy.
- **File**: `LinkedLists/SinglyLinkedListCycleCheckImple.py`

### Reverse a Linked List
Reverse a linked list in-place.
- **File**: `LinkedLists/LinkedListReversal.py`

### Nth to Last Node
Find the nth to last node in a linked list.
- **File**: `LinkedLists/LinkedListNthToLastNode.py`

---

## Stacks

### Stack Implementation
Basic stack operations (LIFO): `push`, `pop`, `peek`, `isEmpty`, `size`.
- **File**: `Stacks/StackImple.py`

### Balanced Parentheses Check
Check if a string of opening and closing parentheses is balanced.
- **File**: `Stacks/BalanceParenthlessCheckImple.py`

---

## Queues

### Queue Implementation
Basic queue operations (FIFO): `enqueue`, `dequeue`, `isEmpty`, `size`.
- **File**: `Queues/QueueImple.py`

### Queue with Two Stacks
Implement a queue using two stacks.
- **File**: `Queues/QueueWith2StacksImple.py`

---

## Deque

### Deque Implementation
Double-ended queue operations: `addFront`, `addRear`, `removeFront`, `removeRear`, `isEmpty`, `size`.
- **File**: `deque/DequeImple.py`

---

## Recursion

### Cumulative Sum
Compute the cumulative sum from 0 to `n`.
- **File**: `Recursion/RecursionCumulativeSum.py`

### Sum of Digits
Returns the sum of all individual digits in an integer.
- **File**: `Recursion/RecursionSumOfDigits.py`

### Word Split
Determine if a string can be split into words found in a given list.
- **File**: `Recursion/RecursionWordSplit.py`

### Reverse a String
Recursive implementation to reverse a string.
- **File**: `Recursion/RecursionReverseStr.py`

### String Permutations
Output all possible permutations of a string.
- **File**: `Recursion/RecursionStrPermutation.py`

### Fibonacci Sequence
Implementations using iteration, recursion, and dynamic programming (memoization).
- **Files**: `Recursion/FibonacciSeqIterative.py`, `Recursion/FibonacciSeqRecursion.py`, `Recursion/FibonacciSeqDynamic.py`

### Coin Change Problem
Find the fewest coins needed to make a change amount.
- **Files**: `Recursion/CoinChangeProblemRecursion.py`, `Recursion/CoinChangeProblemDynamic.py`

---

## Trees

### Binary Search Tree Implementation
- **File**: `Trees/BinarySearchTreesImple.py`

### Binary Heap Implementation
- **File**: `Trees/BinaryHeapImple.py`

### Binary Search
Recursive and iterative implementations.
- **Files**: `Trees/BinarySearchImple.py`, `Trees/BinarySearchRecursiveImple.py`

### Validate BST
Check if a binary tree is a valid Binary Search Tree.
- **Files**: `Trees/BinarySearchTreeCheckImpleSol1.py`, `Trees/BinarySearchTreeCheckImpleSol2.py`

### Trim a BST
Trim a BST so all nodes are within a given range `[min, max]`.
- **File**: `Trees/TrimBinarySearchTreeImple.py`

### Tree Representation (Nodes & References)
Implementing a tree using classes and references.
- **File**: `Trees/TreeRepresentationWithNodesReferences.py`

### Tree Level Order Print
Print a binary tree in level order.
- **File**: `Trees/TreeLevelOrderPrintImple.py`

---

## Sorting

### Bubble Sort
- **File**: `Sorting/BubbleSortImple.py`
- **Complexity**: $O(n^2)$ worst and average case, $O(n)$ best case.

### Selection Sort
- **File**: `Sorting/SelectionSortImple.py`
- **Complexity**: $O(n^2)$ for all cases.

### Insertion Sort
- **File**: `Sorting/InsertionSortImple.py`
- **Complexity**: $O(n^2)$ worst and average case, $O(n)$ best case.

### Merge Sort
- **File**: `Sorting/MergeSortImple.py`
- **Complexity**: $O(n \log n)$ for all cases.

### Quick Sort
- **File**: `Sorting/QuickSortImple.py`
- **Complexity**: $O(n^2)$ worst case, $O(n \log n)$ average/best case.

### Shell Sort
- **File**: `Sorting/ShellSortImple.py`
- **Complexity**: Between $O(n)$ and $O(n^2)$ depending on increment sequence.

---

## Graph Algorithms

### Adjacency List Implementation
- **File**: `GraphAlgorithms/AdjacencyListGraphImple.py`

### Breadth First Search (BFS) - Word Ladder Problem
- **Files**: `GraphAlgorithms/BFS.py`, `GraphAlgorithms/WordLadderProblem.py`

### Depth First Search (DFS) - Knight's Tour Problem
- **Files**: `GraphAlgorithms/DFSImpleTheKnightsTourProblem.py`, `GraphAlgorithms/TheKnightsTourProblem.py`

### General DFS
A more general implementation of Depth First Search.
- **File**: `GraphAlgorithms/DFSGeneral.py`

---

## Error Handling

### Basic Exception Handling
Demonstrates `try-except-else-finally` blocks and user input validation.
- **File**: `Error-debug/ErrorExceptions.py`

---

## Acknowledgments
- [Python for Data Structures, Algorithms, and Interviews on Udemy](https://www.udemy.com)
- [Problem Solving with Algorithms and Data Structures using Python](http://interactivepython.org/runestone/static/pythonds/index.html)
- [Big O Notation - Plain English Explanation](https://stackoverflow.com/questions/487258/what-is-a-plain-english-explanation-of-big-o-notation/487278#487278)
