# Implement coin change problem
# Author: Pradeep K. Pant, ppant@cpan.org
# Given a target amount n and a list (array) of distinct coin values, what's the fewest coins needed to make the
# change amount.
# 1+1+1+1+1+1+1+1+1+1
# 5 + 1+1+1+1+1
# 5+5
# 10
# With 1 coin being the minimum amount.

# Solution strategy:
# This is a classic problem to show the value of dynamic programming. We'll show a basic recursive example and show
# why it's actually not the best way to solve this problem.
# Implement fibonacci_iterative()
def coin_change_recursion(target,coins):
    '''
        INPUT: Target change amount and list of coin values
        OUTPUT: Minimum coins needed to make change

        Note, this solution is not optimized.
        '''

    # Default to target value
    min_coins = target

    # Check to see if we have a single coin match (BASE CASE)
    if target in coins:
        return 1

    else:

        # for every coin value that is <= than target (Using list comprehension
        for i in [c for c in coins if c <= target]:

            # Recursive Call (add a count coin and subtract from the target)
            num_coins = 1 + coin_change_recursion(target - i, coins)

            # Reset Minimum if we have a new minimum (new num_coins less than min_coins)
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins

# Test
print (coin_change_recursion(8,[1,5]))
# 4
# Note
# The problem with this approach is that it is very inefficient! It can take many, 
# many recursive calls to finish this problem and its also inaccurate for non 
# standard coin values (coin values that are not 1,5,10, etc.)