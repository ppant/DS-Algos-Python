# Find the missing element in an array/list

# Author: Pradeep K. Pant, ppant@cpan.org

# Find the Missing Element in an array/list
# Consider an array of non-negative integers. A second array is formed by 
# shuffling the elements of the first array and deleting a random element. 
# Given these two arrays, find which element is missing in the second array.

# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
# Input:
# find_missing_ele([1,2,3,4,5,6,7],[3,7,2,1,4,6])
# Output:
# 5 is the missing number
# Some approaches could be sort the array and compare also we can think about adding all the elemensts
# of both the arrays and then take the diff which is the missing number
# but we'll have to make sure the time complexity doesn't go up also One possible solution 
# is computing the sum of all the numbers in arr1 and arr2, and subtracting arr2’s sum from 
# array1’s sum. The difference is the missing number in arr2. However, this approach could be 
# problematic if the arrays are too long, or the numbers are very large. Then overflow will occur while summing up the numbers.

# The naive solution (brute-force) is go through every element in the second array and check   
# whether it appears in the first array. Note that there may be duplicate elements 
# in the arrays so we should pay special attention to it. The complexity of this 
# approach is O(N^2), since we would need two for loops.
# A more efficient solution is to sort the first array, so while checking whether 
# an element in the first array appears in the second, we can do binary search 
# But we should still be careful about duplicate elements. The complexity is O(NlogN).
#If we don’t want to deal with the special case of duplicate numbers, we can sort 
# both arrays and iterate over them simultaneously. Once two iterators have 
# different values we can stop. The value of the first iterator is the missing element. 
# This solution is also O(NlogN). 

# By performing a very clever trick, we can achieve linear time and constant space 
# complexity without any problems. Here it is: initialize a variable to 0, then XOR 
# every element in the first and second arrays with that variable. In the end, the 
# value of the variable is the result, missing element in array2.
def find_missing_ele(arr1,arr2):
    result=0     
    # Perform an XOR between the numbers in the arrays
    for num in arr1 + arr2: 
        result ^= num 
        #print (result)
        return result 
#  Test
result = find_missing_ele([1,2,3,4,5],[1,2,4,5])
print (result);
