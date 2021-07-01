# Quick Sort Implementation
# Author: Pradeep K. Pant,  https://pradeeppant.com

#- The quick sort uses divide and conquer to gain the same advantages as the merge sort,
# while not using additional storage also known as "partition exchange sort" .
#    - As a trade-off, however, it is possible that the list may not be divided in half.
#    - When this happens, we will see that performance is diminished.
#- A quick sort first selects a value, which is called the "pivot" value.
#- The role of the pivot value is to assist with splitting the list.
#- The actual position where the pivot value belongs in the final sorted list, commonly 
# called the "split" point, will be used to divide the list for subsequent calls to the quick sort.

#- Performance:
#    - Worst case: O(n square)
#    - Best case: O(nlog n)
#    - Average case: O(nlog n)

# Reference material: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html

def quick_sort(arr):
    quick_sort_help(arr,0,len(arr)-1)

def quick_sort_help(arr,first,last):
   # do till this condition is satisfied..
    if first<last:
        # Split the list
        splitpoint = partition(arr,first,last)
        quick_sort_help(arr,first,splitpoint-1)
        quick_sort_help(arr,splitpoint+1,last)

def partition(arr,first,last):
    # use first entry as pivot val
    pivotvalue = arr[first]
    leftmark = first+1
    rightmark = last
    done = False
    # Looping starts
    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp
            
    # swapping
    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp
    return rightmark
        
# Test 
arr = [2,7,1,8,5,9,11,35,25]
quick_sort(arr)
print (arr)
#[1, 2, 5, 7, 8, 11, 25, 35]