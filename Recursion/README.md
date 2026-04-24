# Recursion

This directory contains Python implementations of problems solved using recursion and dynamic programming.

## Contents

### Fibonacci Sequence
- [Fibonacci (Iterative)](FibonacciSeqIterative.py): Iterative implementation of the Fibonacci sequence. Complexity: $O(n)$.
- [Fibonacci (Recursive)](FibonacciSeqRecursion.py): Simple recursive implementation of the Fibonacci sequence. Complexity: $O(2^n)$.
- [Fibonacci (Dynamic Programming)](FibonacciSeqDynamic.py): Optimized Fibonacci sequence using memoization. Complexity: $O(n)$.

### Coin Change Problem
- [Coin Change (Recursive)](CoinChangeProblemRecursion.py): Basic recursive solution to find the minimum number of coins for change. Complexity: $O(c^n)$ where $c$ is the number of coins.
- [Coin Change (Dynamic Programming)](CoinChangeProblemDynamic.py): Optimized solution to the coin change problem using dynamic programming. Complexity: $O(n \cdot k)$ where $n$ is the target sum and $k$ is the number of coin types.

### Other Recursive Problems
- [Cumulative Sum](RecursionCumulativeSum.py): Computes the cumulative sum from 0 to $n$ recursively. Complexity: $O(n)$.
- [Reverse a String](RecursionReverseStr.py): Reverses a string using recursive calls. Complexity: $O(n)$.
- [String Permutations](RecursionStrPermutation.py): Generates all possible permutations of a given string. Complexity: $O(n \cdot n!)$.
- [Sum of Digits](RecursionSumOfDigits.py): Calculates the sum of all individual digits in an integer recursively. Complexity: $O(\log n)$.
- [Word Split](RecursionWordSplit.py): Determines if a string can be split into words from a given list. Complexity: $O(2^n)$ or $O(n^2)$ with DP.
