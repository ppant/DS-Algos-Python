# Deque

This directory contains Python implementations of the Deque (Double-Ended Queue) data structure.

## Contents

- [Deque Implementation](DequeImple.py): Basic implementation of a Deque using a Python list. Includes operations like `addFront`, `addRear`, `removeFront`, `removeRear`, `isEmpty`, and `size`. Note: `addFront` and `removeFront` are $O(1)$, while `addRear` and `removeRear` are $O(n)$ in this implementation due to list shifting.
