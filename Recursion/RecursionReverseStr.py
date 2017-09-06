# Reverse a string using recursion
# Author: Pradeep K. Pant, ppant@cpan.org

# Do not use iteration/slice instead use recursive calls
import sys
sys.setrecursionlimit(1000)
# Implement a recursive reverse function
def reverse_str(str):
    #print (str)
    # Check for the base case at the end there will be at least one char
    if len(str) <= 1:
        return str
    else:
        # Implement recursive reverse
        # Take first index of the string and then add rest starts from index 1 and do a recursive call
        return reverse_str(str[1:] + str[0])        
        
# Test
print(reverse_str('hello world'))
#print( reverse_str('hello world'))
# 'dlrow olleh'
