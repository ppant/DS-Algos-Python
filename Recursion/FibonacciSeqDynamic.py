# Implement the function using dynamic programming by using a cache to store results (memoization).
# memoization + recursion = dynamic programming
# Author: Pradeep K. Pant, ppant@cpan.org

    # Instantiate Cache information
    n = 10
    cache = [None] * (n + 1)

# Implement fibonacci_dynamic
    def fibonacci_dynamic(n):
        # Base Case
        if n == 0 or n == 1:
            return n

        # Check cache if already val of n present if yes pick from there this will save time
        if cache[n] != None:
            return cache[n]

        # Recursive call to and keep setting cache
        cache[n] = fibonacci_dynamic(n - 1) + fibonacci_dynamic(n - 2)
        return cache[n]
# Test
    # We'll try to find the 9th no in the fibnacci sequence which is 34
    print (fibonacci_dynamic(9))
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    # The recursive-memoization solution is exponential time Big-O , with O(n)