# Insertion Sort Implementation

# Author: Pradeep K. Pant, https://pradeeppant.com

# Insertion sort always maintains a sorted sub list in the lower portion of the list
# Each new item is then "inserted" back into the previous sublist such that the 
# sorted sub list is one item larger

# Complexity O(n2) square

# Reference material: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html

def insertion_sort(arr):
    
    # For every index in array
    for i in range(1,len(arr)):
        
        # Set current values and position
        currentvalue = arr[i]
        position = i
        
        # Sorted Sublist
        while position>0 and arr[position-1]>currentvalue:
            
            arr[position]=arr[position-1]
            position = position-1

        arr[position]=currentvalue
        
# Test 
arr = [2,7,1,8,5,9,11,35,25]
insertion_sort(arr)
print (arr)

#[1, 2, 5, 7, 8, 11, 25, 35]