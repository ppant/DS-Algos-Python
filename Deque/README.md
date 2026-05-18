# Deque

This directory contains Python implementations of the Deque (Double-Ended Queue) data structure.

## Contents

- [Deque Implementation](DequeImple.py): Basic implementation of a Deque using a Python list. Includes operations like `addFront`, `addRear`, `removeFront`, `removeRear`, `isEmpty`, and `size`. Time complexity is $O(1)$ for `addFront` and `removeFront`, but $O(n)$ for `addRear` and `removeRear` due to list shifting.
