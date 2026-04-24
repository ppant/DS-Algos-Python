# Queues

This directory contains Python implementations of the Queue data structure.

## Contents

- [Queue Implementation](QueueImple.py): Basic implementation of a FIFO (First-In-First-Out) queue using a Python list. Includes `enqueue`, `dequeue`, `isEmpty`, and `size` methods. Complexity: $O(1)$ for `dequeue`, $O(n)$ for `enqueue` (due to `list.insert(0,item)`).
- [Queue with Two Stacks](QueueWith2StacksImple.py): Implements a queue using two stacks (represented by Python lists) to achieve FIFO behavior. Complexity: $O(1)$ amortized.
