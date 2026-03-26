# Sum of all individual integers
# Author: Pradeep K. Pant, ppant@cpan.org

# Given an integer, create a function which returns the sum of all the individual 
# digits in that integer. For example: if n = 4321, return 4+3+2+1

# Implement recursion sum routine
def recursion_sum_digits(n):
    # Base case: if n is less than 10, it's a single digit
    if n < 10:
        return n
    # Recursion: use modulo operator to get last digit and then use floor divide
    # to pass the rest to recursive routine
    else:
        return n % 10 + recursion_sum_digits(n // 10)
    
# Test
print(recursion_sum_digits(4321))
# Result = 4+3+2+1 = 10
print(recursion_sum_digits(12))
# Result = 1+2 = 3
