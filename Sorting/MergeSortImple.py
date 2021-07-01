# Merge Sort Implementation
# Author: Pradeep K. Pant,  https://pradeeppant.com

#- Merge sort is a recursive algorithm (example of divide and conquer) that continually 
#  splits a list in half.
#    - If the list is empty or has one item, it is sorted by definition (the base case).
#    - If the list has more than one item, we split the list and recursively invoke a 
#      merge sort on both halves.
#    - Once the two halves are sorted, the fundamental operation, called a merge, 
#     is performed.
#    - Merging is the process of taking two smaller sorted lists and combining them 
#      together into a single, sorted, new list.
#    - This algorithm is used to sort a linked list
#    - Performance:
#        - Worst case: O(nlog n)
#        - Best case: O(nlog n)
#        - Average case: O(nlog n)

# Reference material: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html

def merge_sort(arr):
    # Check if arr is there? else already sorted
    if len(arr)>1:
        # look for mid point
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        # recursive routine to divide the list and invoke on both halves
        merge_sort(lefthalf)
        merge_sort(righthalf)
        # Once the tow halves are sorted merging takes place
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1
# Test 
arr = [11,2,5,4,7,6,8,1,23]
merge_sort(arr)
print (arr)
#[1, 2, 4, 5, 6, 7, 8, 11, 23]