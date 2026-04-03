# Arrays

This directory contains implementations and solutions related to array-based problems.

## Contents

### Anagram Check
Checks if two strings are anagrams of each other.
- **Files**: `Anagram_Check_Sorted_Sol.py`, `Anagram_Check_manual_Sol.py`

### Array Pair Sum
Given an integer array, output all unique pairs that sum up to a specific value `k`.
- **File**: `ArrayPairSumSol.py`

### Find Missing Element
Find the missing element in a shuffled second array.
- **Files**: `ArrayFindTheMissingElement_XOR_sol.py`, `ArrayFindTheMissingElement_brute_force_sol.py`, `ArrayFindTheMissingElement_hash_table_sol.py`, `ArrayFindTheMissingElement_takingSumandSubtract_sol.py`
This directory contains Python implementations of common array-based algorithms and problems.

## Contents

- [Anagram Check (Sorted Solution)](Anagram_Check_Sorted_Sol.py): Checks if two strings are anagrams by comparing their sorted versions.
- [Anagram Check (Manual Solution)](Anagram_Check_manual_Sol.py): Checks if two strings are anagrams using a hash table (dictionary) to count character frequencies.
- [Array Find Missing Element (XOR Solution)](ArrayFindTheMissingElement_XOR_sol.py): Efficiently finds a missing element in a shuffled array using bitwise XOR.
- [Array Find Missing Element (Brute Force Solution)](ArrayFindTheMissingElement_brute_force_sol.py): Finds a missing element by sorting both arrays and comparing them.
- [Array Find Missing Element (Hash Table Solution)](ArrayFindTheMissingElement_hash_table_sol.py): Finds a missing element using a hash table (dictionary) to track element counts.
- [Array Find Missing Element (Sum/Subtract Solution)](ArrayFindTheMissingElement_takingSumandSubtract_sol.py): Finds a missing element by calculating the difference between the sums of the two arrays.
- [Array Pair Sum Solution](ArrayPairSumSol.py): Finds all unique pairs in an array that sum up to a specific value $k$ using a set for $O(n)$ complexity.
