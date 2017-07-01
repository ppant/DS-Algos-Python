# Computes the cumulative sum
# Author: Pradeep K. Pant, ppant@cpan.org

# Write a recursive function which takes an integer and computes the cumulative 
# sum of 0 to that integer For example, if n=4 , return 4+3+2+1+0, which is 10.
# This problem is very similar to the factorial problem presented during the 
# introduction to recursion. Remember, always think of what the base case will 
# look like. In this case, we have a base case of n =0 (Note, you could have 
# also designed the cut off to be 1). In this case, we have: 
# n + (n-1) + (n-2) + .... + 0

# Implement recusion sum routine
def recursion_cululative_sum(n):
    # Checking edge case is really important
        if (n == 0):
            return 0
        #print (n)
        # Check for n + (n-1) ... cases
        return n + recursion_cululative_sum(n-1) 
# Test
print (recursion_cululative_sum(5))
# Result = 5+4+3+2+1+0