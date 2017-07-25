# Selection Sort Implementation

# Author: Pradeep K. Pant, ppant@cpan.org
# The selection sort improves on the bubble sort by making only 
# one exchange for every pass through the list. In order to do this, 
# a selection sort looks for the largest value as it makes a pass 
# and, after completing the pass, places it in the proper location. 
# As with a bubble sort, after the first pass, the largest item is 
# in the correct place. After the second pass, the next largest is 
# in place. This process continues and requires n−1 passes to sort 
# n items, since the final item must be in place after the (n−1) st pass.

def selection_sort(arr):
    
    # For every slot in array
    for fillslot in range(len(arr)-1,0,-1):
        positionOfMax=0
        
        # For every set of 0 to fillslot+1
        for location in range(1,fillslot+1):
            # Set maximum's location
            if arr[location]>arr[positionOfMax]:
                positionOfMax = location

        temp = arr[fillslot]
        arr[fillslot] = arr[positionOfMax]
        arr[positionOfMax] = temp
        
# Test 
arr = [2,7,1,8,5,9,11,35,25]
selection_sort(arr)
print (arr)
#[1, 2, 5, 7, 8, 11, 25, 35]