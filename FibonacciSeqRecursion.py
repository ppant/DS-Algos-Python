# Implement Fibonacci sequence using recursion
# Author: Pradeep K. Pant, ppant@cpan.org
# Our function will accept a number n and return the nth number of the fibonacci
# sequence Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts off with a base case checking to see if
# n = 0 or 1, then it returns 1. Else it returns fib(n-1)+fib(n+2).
# Implement recursion word_split()
def fibonacci_recursion(n):
    print (n)
    # First check for the base case
    if n == 0 or n == 1:
         return n
    else: 
        #recursion check for last two items and add them recursively
       return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

# Test
    # We'll try to find the 9th no in the fibnacci sequence which is 34
    print (fibonacci_recursion(9))
    #print fibonacci_recursion(3)
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    # The recursive solution is exponential time Big-O , with O(2^n). However, 
    # its a very simple and basic implementation to consider: