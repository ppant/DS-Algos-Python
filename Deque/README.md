# Deque

This directory contains Python implementations of the Deque (Double-Ended Queue) data structure.

## Contents

- [Deque Implementation](DequeImple.py): Basic implementation of a Deque using a Python list. Includes operations like `addFront`, `addRear`, `removeFront`, `removeRear`, `isEmpty`, and `size`.
  - `addFront` and `removeFront`: $O(1)$
  - `addRear` and `removeRear`: $O(n)$ (due to list shifting)
