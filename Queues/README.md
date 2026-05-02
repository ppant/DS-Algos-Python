# Queues

This directory contains Python implementations of the Queue data structure.

## Contents

- [Queue Implementation](QueueImple.py): Basic implementation of a FIFO (First-In-First-Out) queue using a Python list.
  - `enqueue()`: $O(n)$ complexity due to `insert(0)`.
  - `dequeue()`: $O(1)$ complexity using `pop()`.
- [Queue with Two Stacks](QueueWith2StacksImple.py): Implements a queue using two stacks to achieve FIFO behavior with $O(1)$ amortized complexity for both `enqueue` and `dequeue`.
