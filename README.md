# Data Structures and Algorithms using Python
This is a collection of various common programming problems solved using Data structures implemented in Python. I have mostly done this before in C/C++/Perl. This is a attempt to solve using Python. Please feel free to collaborate.

## Anagram algorithm ##	
Algorithm will take two strings and check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters in other words rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once	
```	Some examples of anagram:
	"dormitory" is an anagram of "dirty room"
	"a perfectionist" is an anagram of "I often practice."
	"action man" is an anagram of "cannot aim" 
```	
Our anagram check algorithm with take two strings and will give a boolean TRUE/FALSE depends on anagram found or not?

## Array Pair Sum ##	
Given an integer array, output all the unique pairs that sum up to a specific value k.
So the input:
```python	
sum_arr_uniq_pairs([1,2,2,3,4,1,1,3,2,1,3,1,2,2,4,0],5)
would return 2 pairs:

 	(2,3)
 	(1,4)
 ```
 
## Find a missing element in an array/list ##	
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.
Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
```python
Input:
find_missing_ele([1,2,3,4,5,6,7],[3,7,2,1,4,6])
Output:
5 is the missing number
```

## Stack class implementation
Implement basic stack operations (LIFO)
```python
push() - Push an element in a stack 
pop()- POP an element from top of the stack
peek() - Just peek into top element of the stack (don't perform any operation)
```

## Queue class implementation
Implement basic Queue operations (FIFO)
```python
enqueue - adding a element to the queue 
dequeue - removing an element from the queue
```

## Deque (DECK) class implementation
Implement basic operation in deque (Add and remove elements both at front and rear)
```python
addFront() - Add an element at the front
addRear() - Add an element at the rear
removeFront() - Remove from front
removeRear() - Remove from rear
```

# Balance parenthelss using stack/list
Given a string of opening and closing parentheses, check whether it’s balanced. 
We have 3 types of parentheses: 
round brackets: ()
square brackets: []
curly brackets: {}. 
Assume that the string doesn’t contain any other character than these, no spaces words or numbers. 
As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not. 
Algo will take string as inut string and will return boolean (TRUE/FALSE)
Examples:
```python
print (check_parentheses_match('([])'))
print (check_parentheses_match('[](){([[[]]])'))
```

# Queue with 2 stack implementation
This is a classic problem. We need to use the basic charactristics of stack (popping out elements in reverse order) will make a queue.
Example:
```python
# Create a object of the class
qObj = QueueWith2Stack()
# Add an element 
qObj.enqueue(1)
# Add another element
qObj.enqueue(2)
# Add more element
qObj.enqueue(4)
# Add more element
qObj.enqueue(8)
# Remove item
print (qObj.dequeue())
# Remove item 
print (qObj.dequeue())
# Remove item
print (qObj.dequeue())
# Remove item 
print (qObj.dequeue())
```

# Singly Linked List class implementation
Implement basic skeleton for a Singly Linked List 
Example:
```python
# Added node
a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)        
# Set the pointers
a.nextnode = b
b.nextnode = c

print (a.value)
print (b.value)
print (c.value)

# Print using class 
print (a.nextnode.value)
```
# Doubly Linked List class implementation
Implement basic skeleton for a Doubly Linked List 
Example:
```python
# Added node
a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)        
# Set the pointers
# setting b after a (a before b)
b.prev_node = a
a.next_node = b

# Setting c after a
b.next_node = c
c.prev_node = b

print (a.value)
print (b.value)
print (c.value)

# Print using class 
print (a.next_node.value)
print (b.next_node.value)
print (b.prev_node.value)
print (c.prev_node.value)
```
#  Reverse a linked list implementation
Aim is to write a function to reverse a Linked List in place. The function will take in 
the head of the list as input and return the new head of the list.
Example:
```python
# Create a Linked List 
a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)
d = LinkedListNode(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print (a.nextnode.value)
print (b.nextnode.value)
print (c.nextnode.value)

# Call the reverse()
LinkedListNode().reverse(a)
print (d.nextnode.value)
print (c.nextnode.value)
print (b.nextnode.value)
```

#  Linked list Nth to last node
Aim is a function that takes a head node and an integer value n and then returns the nth to last node in the linked list. Example:
```python
# Create a Linked List 
a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)
d = LinkedListNode(4)
e = LinkedListNode(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

print (a.nextnode.value)
print (b.nextnode.value)
print (c.nextnode.value)
print (d.nextnode.value)

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = LinkedListNode().nth_to_last_node(2, a) 
print (target_node.value)
# Ans: d=4
```

# Computes the cumulative sum - Recursion 
Aim is to write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer. For example, if n=4 , return 4+3+2+1+0, which is 10. We always should take care of the base case. In this case, we have a base case of n =0 (Note, you could have also designed the cut off to be 1). In this case, we have: n + (n-1) + (n-2) + .... + 0.
Example:
```python
print (recursion_cululative_sum(5))
```

# Sum of digits - Recursion
Given an integer, create a function which returns the sum of all the individual 
digits in that integer. For example: if n = 4321, return 4+3+2+1
Example:
```python
print (recursion_sum_digits(12))
```

# Word split - Recursion
Create a function called word_split() which takes in a string phrase and a set list_of_words. The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. You can assume the phrase will only contain words found in the dictionary if it is completely splittable.
Example:
```python
 print (word_split('themanran',['the','ran','man']))
```

# Reverse a string - Recursion
Implement a recursive reverse. 
Example:
```python
 print(reverse_str('hello world'))
```
 
# List all the permutation of a string - Recursion
Given a string, write a function that uses recursion to output a list of all the possible permutations of that string. For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
This way of doing permutaion is for learning in real scenerios better to use excellant Python library "ltertools" with current approach there are n! permutations, so the it looks that algorithm will take O(n*n!)time
Example:
```python
 print(permute('abc'))
``` 

# Implement fibonacci sequence with simple iteration
```python
# We'll try to find the 9th no in the fibonacci sequence which is 34
print (fibonacci_itertaive(9))
# 34
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# The recursive solution is exponential time Big-O , with O(n).
```

# Implement fibonacci sequence - Recursion
Our function will accept a number n and return the nth number of the fibonacci
sequence Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts off with a base case checking to see if
n = 0 or 1, then it returns 1. Else it returns fib(n-1)+fib(n+2).
```python
# We'll try to find the 9th no in the fibnacci sequence which is 34
print (fibonacci_recursion(9))
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# The recursive solution is exponential time Big-O , with O(2^n). However, 
# its a very simple and basic implementation to consider
```

# Implement fibonacci sequence - Dynamic programming
Implement the function using dynamic programming by using a cache to store results (memoization).
memoization + recursion = dynamic programming
```python
# We'll try to find the 9th no in the fibnacci sequence which is 34
print (fibonacci_dynamic(9))
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# The recursive-memoization solution is exponential time Big-O , with O(n)
```

# Implement coin change problem - Recursion
Given a target amount n and a list (array) of distinct coin values, what's the fewest coins needed to make the
change amount.
1+1+1+1+1+1+1+1+1+1
5 + 1+1+1+1+1
5+5
10
With 1 coin being the minimum amount.
```python
print (coin_change_recursion(8,[1,5]))
# 4
# Note:
# The problem with this approach is that it is very inefficient! It can take many, 
# many recursive calls to finish this problem and its also inaccurate for non 
# standard coin values (coin values that are not 1,5,10, etc.)
```

# Implement coin change problem - Dynamic programming
Given a target amount n and a list (array) of distinct coin values, what's the fewest coins needed to make the
change amount.
1+1+1+1+1+1+1+1+1+1
5 + 1+1+1+1+1
5+5
10
With 1 coin being the minimum amount.
```python
# Caching
target = 74
coins = [1,5,10,25]
known_results = [0]*(target+1)

print (coin_change_dynamic(target,coins,known_results))
```

# Build a tree and fetch nodes and insert using list of lists

```python
ttree = buildTree('a')
insertLeft(ttree,'b')
insertRight(getLeftChild(ttree),'d')
insertRight(ttree,'c')
insertLeft(getRightChild(ttree),'e')
insertRight(getRightChild(ttree),'f')
#print(getLeftChild(ttree))
print(getLeftChild(ttree))
print(getRightChild(ttree))
```

# Binary Search Tree Implementation

```python
# list must already be sorted!
arr = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(arr,4))
# True
#print(binary_search(arr,2.2))
# False
```

# Binary Heap Implementation Recursive approach
```python 

# Creates a new, empty, binary heap.
BinaryHeap()

# Adds a new item to the heap.
insert(k) 

# Returns the item with the minimum key value, leaving item in the heap.
findMin() 

# Returns the item with the minimum key value, removing the item from the heap.
delMin() 

# Returns true if the heap is empty, false otherwise.
isEmpty() 

# Returns the number of items in the heap.
size() 

# Builds a new heap from a list of keys.
buildHeap(list) 
```

# Binary Search Implementation Recursive approach
```python
# list must already be sorted!
# list must already be sorted!
arr = [1,2,3,4,5,6,7,8,9,10]
rec_bin_search(arr,3)
# True
rec_bin_search(arr,15)
# False
```

# Binary Search Tree Implementation
```python
mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])
```

# Binary Search Tree Check - Validate BST Sol 1
Given a binary tree, check whether it’s a binary search tree or not?
```python
inorder(tree)
sort_check(tree_vals)
```

# Binary Search Tree Check - Validate BST Sol 2
Given a binary tree, check whether it’s a binary search tree or not?
```python
root= Node(10, "Hello")
root.left = Node(5, "Five")
root.right= Node(30, "Thirty")

print(verify(root)) # prints True, since this tree is valid

root = Node(10, "Ten")
root.right = Node(20, "Twenty")
root.left = Node(5, "Five")
root.left.right = Node(15, "Fifteen")

print(verify(root)) # prints False, since 15 is to the left of 10

sort_check(tree_vals)
```

# Trim a Binary Search Tree
Given the root of a binary search tree and 2 numbers min and max, trim the 
tree such that all the numbers in the new tree are between min and max (inclusive). The resulting tree should still be a valid binary search tree. so we should remove all the nodes whose value is not between min and max. 
The complexity of this algorithm is O(N), where N is the number of nodes in the tree. Because we basically perform a post-order traversal of the tree, visiting each and every node one. This is optimal because we should visit every 
node at least once. This is a very elegant question that demonstrates the effectiveness of recursion in trees. 

# Nodes and References Implementation of a Tree
Implementing the representation of a Tree as a class with nodes and references.
```python
r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())

#  Output
#a
#None
#<__main__.BinaryTree object at 0x104779c10>
#b
#<__main__.BinaryTree object at 0x103b42c50>
#c
#hello
```

# Tree Level Order Print
Given a binary tree of integers, print it in level order. The output will contain 
space between the numbers in the same level, and new line between different levels. 
For example, if the tree is: 
#   1
#  2  3
# 4 5 6
# though not needed but paths are 1->2->4, 1->3->5 and 1->3->6

# The output should be: 
# 
#     1 
#     2 3 
#     4 5 6
# The time complexity of this solution is O(N), which is the number of nodes in 
# the tree, so it’s optimal. Because we should visit each node at least once. 
# The space complexity depends on maximum size of the queue at any point, which is 
# the most number of nodes at one level. The worst case occurs when the tree is a 
# complete binary tree, which means each level is completely filled with maximum 
# number of nodes possible. In this case, the most number of nodes appear at the 
# last level, which is (N+1)/2 where N is the total number of nodes. So the space 
# vcomplexity is also O(N). Which is also optimal while using a queue. 
## Acknowledgments

* Python for data structures algorithms and interviews course on [Udemy](https://www.udemy.com)

* [Problem Solving with Algorithms and Data Structures using Python](http://interactivepython.org/runestone/static/pythonds/index.html)
