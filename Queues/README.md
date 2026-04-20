# Queues

This directory contains Python implementations of the Queue data structure.

## Contents

- [Queue Implementation](QueueImple.py): Basic implementation of a FIFO (First-In-First-Out) queue using a Python list. Time Complexity: $O(n)$ for `enqueue` (insert at 0), $O(1)$ for `dequeue` (pop).
- [Queue with Two Stacks](QueueWith2StacksImple.py): Implements a queue using two stacks (represented by Python lists) to achieve FIFO behavior. Time Complexity: $O(1)$ amortized for both `enqueue` and `dequeue`.
