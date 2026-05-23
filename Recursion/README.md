# Recursion

This directory contains Python implementations of problems solved using recursion and dynamic programming.

## Contents

### Fibonacci Sequence
- [Fibonacci (Iterative)](FibonacciSeqIterative.py): Iterative implementation of the Fibonacci sequence. $O(n)$ time.
- [Fibonacci (Recursive)](FibonacciSeqRecursion.py): Simple recursive implementation of the Fibonacci sequence. $O(2^n)$ time.
- [Fibonacci (Dynamic Programming)](FibonacciSeqDynamic.py): Optimized Fibonacci sequence using memoization. $O(n)$ time.

### Coin Change Problem
- [Coin Change (Recursive)](CoinChangeProblemRecursion.py): Basic recursive solution to find the minimum number of coins for change.
- [Coin Change (Dynamic Programming)](CoinChangeProblemDynamic.py): Optimized solution to the coin change problem using dynamic programming. $O(n \cdot m)$ time, where $n$ is the target amount and $m$ is the number of coins.

### Other Recursive Problems
- [Cumulative Sum](RecursionCumulativeSum.py): Computes the cumulative sum from 0 to $n$ recursively. $O(n)$ time.
- [Reverse a String](RecursionReverseStr.py): Reverses a string using recursive calls. $O(n)$ time.
- [String Permutations](RecursionStrPermutation.py): Generates all possible permutations of a given string. $O(n!)$ time.
- [Sum of Digits](RecursionSumOfDigits.py): Calculates the sum of all individual digits in an integer recursively. $O(\log_{10} n)$ time.
- [Word Split](RecursionWordSplit.py): Determines if a string can be split into words from a given list.
