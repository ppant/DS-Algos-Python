# Array Pair Sum: Given an integer array, output all the unique pairs 
# that sum up to a specific value k.

# Author: Pradeep K. Pant, ppant@cpan.org

# The O(N) algorithm uses the set data structure. We perform a linear pass 
# from the beginning and for each element we check whether k-element is in the 
# set of seen numbers. If it is, then we found a pair of sum k and add it to 
# the output. If not, this element doesn’t belong to a pair yet, and we add it 
# to the set of seen elements. The algorithm is really simple once we figure 
# out using a set. The complexity is O(N) because we do a single linear scan of 
# the array, and for each element we just check whether the corresponding number 
# to form a pair is in the set or add the current element to the set. 
# Insert and find operations of a set are both average O(1), so the algorithm 
# is O(N) in total.

def sum_arr_uniq_pairs(arr,k):
    # Check for the array length 
    if len(arr) < 2:
        return 
    
     # Sets for tracking if element is already seen?
    # We'll use set data structure which stores immutable data types 
    seen = set()
    output = set()
    
    # For every number in array
    for num in arr:
        
        # Set target difference
        # Logic is to check for difference between say first num and sum no 
        # which we have passed in function
        target = k-num
        
        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
        
        else:
            # Add a tuple with the corresponding pair
            output.add( (min(num,target),  max(num,target)) )
    
    
    # FOR TESTING
    return len(output)
    # Nice one-liner for printing output
    #return '\n'.join(map(str,list(output)))
      
   
#  Test
result = sum_arr_uniq_pairs([1,2,2,3,4,1,1,3,2,1,3,1,2,2,4,0],5)
print (result);
