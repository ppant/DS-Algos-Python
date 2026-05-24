# Queues

This directory contains Python implementations of the Queue data structure.

## Contents

- [Queue Implementation](QueueImple.py): Basic implementation of a FIFO (First-In-First-Out) queue using a Python list. Time Complexity: $O(n)$ for `enqueue` (due to `insert(0)`), $O(1)$ for `dequeue`.
- [Queue with Two Stacks](QueueWith2StacksImple.py): Implements a queue using two stacks to achieve FIFO behavior. Time Complexity: Amortized $O(1)$ for both operations.
