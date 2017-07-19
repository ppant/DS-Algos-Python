# Binary Search Implementation Recursive approach

# Author: Pradeep K. Pant, ppant@cpan.org

def rec_bin_search(arr,ele):
    
    # Base Case!
    if len(arr) == 0:
        return False
    
    # Recursive Case
    else:
        
        mid = len(arr)//2
        
        # If match found
        if arr[mid]==ele:
            return True
        
        else:
            
            # Call again on second half
            if ele<arr[mid]:
                return rec_bin_search(arr[:mid],ele)
            
            # Or call on first half
            else:
                return rec_bin_search(arr[mid+1:],ele)
# Test 
# list must already be sorted!
# list must already be sorted!
arr = [1,2,3,4,5,6,7,8,9,10]
rec_bin_search(arr,3)
# True
rec_bin_search(arr,15)
# False