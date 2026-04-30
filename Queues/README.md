# Queues

This directory contains Python implementations of the Queue data structure.

## Contents

- [Queue Implementation](QueueImple.py): Basic implementation of a FIFO (First-In-First-Out) queue using a Python list. Includes `enqueue` ($O(n)$ due to `insert(0)`) and `dequeue` ($O(1)$) methods.
- [Queue with Two Stacks](QueueWith2StacksImple.py): Implements a queue using two stacks (represented by Python lists) to achieve FIFO behavior with $O(1)$ amortized time for `enqueue` and `dequeue`.
