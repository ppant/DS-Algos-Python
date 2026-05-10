# Queues

This directory contains Python implementations of the Queue data structure.

## Contents

- [Queue Implementation](QueueImple.py): Basic implementation of a FIFO (First-In-First-Out) queue using a Python list. Complexity: `enqueue` is $O(n)$ due to `insert(0)`, while `dequeue` is $O(1)$.
- [Queue with Two Stacks](QueueWith2StacksImple.py): Implements a queue using two stacks. Complexity: Amortized $O(1)$ for both `enqueue` and `dequeue` operations.
