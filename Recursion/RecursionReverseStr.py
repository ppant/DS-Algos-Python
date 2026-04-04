# Reverse a string using recursion
# Author: Pradeep K. Pant, ppant@cpan.org

# Do not use iteration/slice instead use recursive calls
import sys
sys.setrecursionlimit(1000)

# Implement a recursive reverse function
def reverse_str(str):
    # Check for the base case
    if len(str) <= 1:
        return str
    else:
        # Implement recursive reverse
        # Take the rest of the string from index 1, reverse it, then append the first character
        return reverse_str(str[1:]) + str[0]
        
# Test
print(reverse_str('hello world'))
# Result: 'dlrow olleh'
