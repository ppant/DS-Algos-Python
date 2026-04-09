# Deque

This directory contains Python implementations of the Deque (Double-Ended Queue) data structure.

## Contents

- [Deque Implementation](DequeImple.py): Basic implementation of a Deque using a Python list. Includes operations like `addFront`, `addRear`, `removeFront`, `removeRear`, `isEmpty`, and `size`.
  - Complexity: $O(1)$ for `addFront` and `removeFront`, $O(n)$ for `addRear` and `removeRear` (due to list shifts).
