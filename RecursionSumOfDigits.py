# Sum of all individual integers
# Author: Pradeep K. Pant, ppant@cpan.org

# Given an integer, create a function which returns the sum of all the individual 
# digits in that integer. For example: if n = 4321, return 4+3+2+1

# Implement recusion sum routine
def recursion_sum_digits(n):
    # Checking edge case is really important
    str_n = str(n)
    print (str_n)
    if len(str_n) == 0:
        return n
    #print (n)
    # Recursion, use modulo operator to get RMD and then use divide to pass
    # to recursive routine next interation repeat same procedure
    # with small number and add
    else:
        return n%10 + recursion_sum_digits(n/10)         
    
# Test
print (recursion_sum_digits(12))
# Result = 9+8+5+4 = 25