# Queues

This directory contains Python implementations of the Queue data structure.

## Contents

- [Queue Implementation](QueueImple.py): Basic implementation of a FIFO (First-In-First-Out) queue using a Python list. Includes `enqueue`, `dequeue`, `isEmpty`, and `size` methods.
  - `enqueue`: $O(n)$ (due to list insertion at 0)
  - `dequeue`: $O(1)$
- [Queue with Two Stacks](QueueWith2StacksImple.py): Implements a queue using two stacks (represented by Python lists) to achieve FIFO behavior. Complexity: $O(1)$ amortized for enqueue and dequeue.
