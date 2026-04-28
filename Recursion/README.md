# Recursion

This directory contains Python implementations of problems solved using recursion and dynamic programming.

## Contents

### Fibonacci Sequence
- [Fibonacci (Iterative)](FibonacciSeqIterative.py): Iterative implementation of the Fibonacci sequence. $O(n)$
- [Fibonacci (Recursive)](FibonacciSeqRecursion.py): Simple recursive implementation of the Fibonacci sequence. $O(2^n)$
- [Fibonacci (Dynamic Programming)](FibonacciSeqDynamic.py): Optimized Fibonacci sequence using memoization. $O(n)$

### Coin Change Problem
- [Coin Change (Recursive)](CoinChangeProblemRecursion.py): Basic recursive solution to find the minimum number of coins for change. $O(2^n)$
- [Coin Change (Dynamic Programming)](CoinChangeProblemDynamic.py): Optimized solution to the coin change problem using dynamic programming. $O(n \cdot m)$ where $n$ is the amount and $m$ is the number of coins.

### Other Recursive Problems
- [Cumulative Sum](RecursionCumulativeSum.py): Computes the cumulative sum from 0 to $n$ recursively. $O(n)$
- [Reverse a String](RecursionReverseStr.py): Reverses a string using recursive calls. $O(n)$
- [String Permutations](RecursionStrPermutation.py): Generates all possible permutations of a given string. $O(n \cdot n!)$
- [Sum of Digits](RecursionSumOfDigits.py): Calculates the sum of all individual digits in an integer recursively. $O(d)$ where $d$ is the number of digits.
- [Word Split](RecursionWordSplit.py): Determines if a string can be split into words from a given list. $O(n^2)$
