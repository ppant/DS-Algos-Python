# Recursion

This directory contains Python implementations of problems solved using recursion and dynamic programming.

## Contents

### Fibonacci Sequence
- [Fibonacci (Iterative)](FibonacciSeqIterative.py): Iterative implementation. Time Complexity: $O(n)$.
- [Fibonacci (Recursive)](FibonacciSeqRecursion.py): Simple recursive implementation. Time Complexity: $O(2^n)$.
- [Fibonacci (Dynamic Programming)](FibonacciSeqDynamic.py): Optimized Fibonacci using memoization. Time Complexity: $O(n)$.

### Coin Change Problem
- [Coin Change (Recursive)](CoinChangeProblemRecursion.py): Basic recursive solution. Time Complexity: $O(2^n)$ (highly dependent on coin denominations).
- [Coin Change (Dynamic Programming)](CoinChangeProblemDynamic.py): Optimized solution using dynamic programming. Time Complexity: $O(n \cdot m)$ where $n$ is the target amount and $m$ is the number of coin denominations.

### Other Recursive Problems
- [Cumulative Sum](RecursionCumulativeSum.py): Computes the cumulative sum from 0 to $n$ recursively. Time Complexity: $O(n)$.
- [Reverse a String](RecursionReverseStr.py): Reverses a string using recursive calls. Time Complexity: $O(n)$.
- [String Permutations](RecursionStrPermutation.py): Generates all possible permutations of a given string. Time Complexity: $O(n!)$.
- [Sum of Digits](RecursionSumOfDigits.py): Calculates the sum of all individual digits recursively. Time Complexity: $O(\log_{10} n)$.
- [Word Split](RecursionWordSplit.py): Determines if a string can be split into words. Time Complexity: $O(n^2)$ where $n$ is the length of the string.
