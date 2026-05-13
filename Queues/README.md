# Queues 📦

This directory contains Python implementations of the Queue data structure.

## Contents

- [Queue Implementation](QueueImple.py): Basic implementation of a FIFO (First-In-First-Out) queue using a Python list. Time Complexity: `enqueue` is $O(n)$ due to `insert(0)`, while `dequeue` is $O(1)$ using `pop()`.
- [Queue with Two Stacks](QueueWith2StacksImple.py): Implements a queue using two stacks to achieve FIFO behavior. Time Complexity: $O(1)$ amortized for both `enqueue` and `dequeue`.
