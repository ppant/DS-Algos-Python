# Binary Search Tree Implementation

# Author: Pradeep K. Pant, ppant@cpan.org

def binary_search(arr,ele):
    
    # First and last index values
    first = 0
    last = len(arr) - 1
    
    found = False
    
    
    while first <= last and not found:
        
        mid = (first+last)//2 # or // for Python 3
        
        # Match found
        if arr[mid] == ele:
            found = True
        
        # Set new midpoints up or down depending on comparison
        else:
            # Set down
            if ele < arr[mid]:
                last = mid -1
            # Set up 
            else:
                first = mid + 1
                
    return found

# Test 
# list must already be sorted!
arr = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(arr,4))
# True
#print(binary_search(arr,2.2))
# False