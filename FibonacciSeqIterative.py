# Implement fibonacci sequence with simple iteration.
# Author: Pradeep K. Pant, ppant@cpan.org

# Implement fibonacci_iterative()
def fibonacci_itertaive(n):
    # Initialize initial values
    first = 0
    second = 1
    next_node = 2
    # Looping from 3 node to nth node
    for i in range(3,n):
            # add second and next node and store sum in first node
            first = second + next_node
            # re-assign next_node val to second node
            second = next_node
            # re-assign first next_node val
            next_node = first
    return first

# Test
    # We'll try to find the 9th no in the fibonacci sequence which is 34
    print (fibonacci_itertaive(9))
    # 34
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    # The recursive solution is exponential time Big-O , with O(n).
