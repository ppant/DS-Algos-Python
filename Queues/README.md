# Queues

This directory contains Python implementations of the Queue data structure.

## Contents

- [Queue Implementation](QueueImple.py): Basic implementation of a FIFO (First-In-First-Out) queue using a Python list. Includes `enqueue`, `dequeue`, `isEmpty`, and `size` methods. `enqueue` is $O(n)$ while `dequeue` is $O(1)$.
- [Queue with Two Stacks](QueueWith2StacksImple.py): Implements a queue using two stacks (represented by Python lists) to achieve FIFO behavior. Amortized $O(1)$ for both operations.
