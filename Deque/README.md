# Deque

This directory contains Python implementations of the Deque (Double-Ended Queue) data structure.

## Contents

- [Deque Implementation](DequeImple.py): Basic implementation of a Deque using a Python list.
  - `addFront()` and `removeFront()`: $O(1)$ complexity as they operate on the end of the list.
  - `addRear()` and `removeRear()`: $O(n)$ complexity due to list shifting when inserting/popping at index 0.
