# Recursion

This directory contains Python implementations of problems solved using recursion and dynamic programming.

## Contents

### Fibonacci Sequence
- [Fibonacci (Iterative)](FibonacciSeqIterative.py): Iterative implementation. Complexity: $O(n)$.
- [Fibonacci (Recursive)](FibonacciSeqRecursion.py): Simple recursive implementation. Complexity: $O(2^n)$.
- [Fibonacci (Dynamic Programming)](FibonacciSeqDynamic.py): Optimized using memoization. Complexity: $O(n)$.

### Coin Change Problem
- [Coin Change (Recursive)](CoinChangeProblemRecursion.py): Basic recursive solution. Complexity: Exponential.
- [Coin Change (Dynamic Programming)](CoinChangeProblemDynamic.py): Optimized using DP. Complexity: $O(n \cdot m)$ where $m$ is the number of coins.

### Other Recursive Problems
- [Cumulative Sum](RecursionCumulativeSum.py): Computes the cumulative sum from 0 to $n$ recursively. Complexity: $O(n)$.
- [Reverse a String](RecursionReverseStr.py): Reverses a string using recursive calls. Complexity: $O(n)$.
- [String Permutations](RecursionStrPermutation.py): Generates all possible permutations. Complexity: $O(n!)$.
- [Sum of Digits](RecursionSumOfDigits.py): Calculates the sum of digits recursively. Complexity: $O(\log_{10} n)$.
- [Word Split](RecursionWordSplit.py): Dynamic Programming solution. Complexity: $O(n^2)$ depending on dictionary lookups.
