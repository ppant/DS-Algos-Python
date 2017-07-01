# Sum of all individual integers
# Author: Pradeep K. Pant, ppant@cpan.org

# Given an integer, create a function which returns the sum of all the individual 
# digits in that integer. For example: if n = 4321, return 4+3+2+1

# Implement recusion sum routine
def recursion_sum_digits(n):
    # Checking edge case is really important
    if len(str(n)) == 1:
        return n
    #print (n)
    # Recursion, use modulo operator to get RMD and then use divide to pass
    # to recursive routine next interation repeat same procedure
    # with small number and add
    else:
        return n%10 + recursion_sum_digits(n/10)         
    
# Test
print (recursion_sum_digits(4321))
# Result = 4+3+2+1 = 10