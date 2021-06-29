# Bubble Sort Implementation

# Author: Pradeep K. Pant, ppant@cpan.org,  https://pradeeppant.com
# The bubble sort makes multiple passes through a list. It compares
#  adjacent items and exchanges those that are out of order. 
# Each pass through the list places the next largest value in its 
# proper place. In essence, each item “bubbles” up to the location 
# where it belongs.


# * Regardless of how the items are arranged in the initial list, n−1 passes will be 
# made to sort a list of size n, so 1 pass is n-1 comparisons, 2 pass is n-2 comparions and n-1 is 1 comparions.
# * A bubble sort is often considered the most inefficient sorting method since it 
# must exchange items before the final location is known. These “wasted” exchange 
# operations are very costly. However, because the bubble sort makes passes through 
# the entire unsorted portion of the list, it has the capability to do something most 
# sorting algorithms cannot. In particular, if during a pass there are no exchanges, 
# then we know that the list must be sorted. A bubble sort can be modified to stop early 
# , if it finds that the list has already become sorted. This means that for lists that require just 
# a few passes, a bubble sort may have an advantage in that it will recognize the sorted list and stop.
# * Performance: Worst case: O(n2) n square, best case O(n), average case: O(n2) n square

# Reference material: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html


def bubble_sort(arr):
    # For every element (arranged backwards)
    for n in range(len(arr)-1,0,-1):
        #
        for k in range(n):
            # If we come to a point to switch
            if arr[k]>arr[k+1]:
                # swapping
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
        
# Test 
arr = [2,7,1,8,5,9,11,35,25]
bubble_sort(arr)
print (arr)
#[1, 2, 5, 7, 8, 11, 25, 35]