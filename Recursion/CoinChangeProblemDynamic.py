# Implement coin change problem- Dynamic programming imple
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
def coin_change_dynamic(target,coins,known_results):
    '''
    INPUT: This funciton takes in a target amount and a list of possible coins to use.
    It also takes a third parameter, known_results, indicating previously calculated results.
    The known_results parameter shoud be started with [0] * (target+1)
    
    OUTPUT: Minimum number of coins needed to make the target.
    '''
    
    # Default output to target
    min_coins = target
    
    # Base Case
    if target in coins:
        known_results[target] = 1
        return 1
    
    # Return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]
    
    else:
        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:
            
            # Recursive call, note how we include the known results!
            num_coins = 1 + coin_change_dynamic(target-i,coins,known_results)
            
            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins
                
                # Reset the known result
                known_results[target] = min_coins
                
    return min_coins

# Test
# Caching
target = 74
coins = [1,5,10,25]
known_results = [0]*(target+1)

print (coin_change_dynamic(target,coins,known_results))
#print (coin_change_dynamic(8,[1,5]))
# 2