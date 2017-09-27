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
```python
1+1+1+1+1+1+1+1+1+1
5 + 1+1+1+1+1
5+5
10
With 1 coin being the minimum amount.
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
```python
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
```
 
# Bubble Sort Implementation
The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order. Each pass through the list places the next largest value in its proper place. In essence, each item “bubbles” up to the location where it belongs.
* Regardless of how the items are arranged in the initial list, n−1 passes will be made to sort a list of size n, so 1 pass n-1 comparisons, 2 pass n-2 comparions and n-1 is 1 comparions.
* A bubble sort is often considered the most inefficient sorting method since it must exchange items before the final 
  location is known. These “wasted” exchange operations are very costly. However, because the bubble sort makes passes through the entire unsorted portion of the list, it has the capability to do something most sorting algorithms cannot. In particular, if during a pass there are no exchanges, then we know that the list must be sorted. A bubble sort can be modified to stop early if it finds that the list has become sorted. This means that for lists that require just a few passes, a bubble sort may have an advantage in that it will recognize the sorted list and stop.
* Performance:
        - Worst case: O(n2) n-square
        - Best case: O(n)
        - Average case: O(n2) n-square
```python
arr = [2,7,1,8,5,9,11,35,25]
bubble_sort(arr)
print (arr)
[1, 2, 5, 7, 8, 11, 25, 35]
```

# Selection Sort Implementation
* Selection sort is a in-place algorithm 
* It works well with small files
* It is used for sorting the files with large values and small keys this is due to the fact that selection is based 
  on keys and swaps are made only when required
* The selection sort improves on the bubble sort by making only one exchange for every pass through the list. In order to do this, a selection sort looks for the largest value as it makes a pass and, after completing the pass, places it in the proper location. As with a bubble sort, after the first pass, the largest item is in the correct place. After the second pass, the next largest is in place. This process continues and requires n−1 passes to sort n items, since the final item must be in place after the (n−1) st pass
* Performance:
        - Worst case: O(n2) n-square
        - Best case: O(n)
        - Average case: O(n2) n-square
		- worst case space complexity: O(1)
```python
arr = [2,7,1,8,5,9,11,35,25]
selection_sort(arr)
print (arr)

[1, 2, 5, 7, 8, 11, 25, 35]
```


# Insertion Sort Implementation
Insertion sort always maintains a sorted sub list in the lower portion of the list Each new item is then "inserted" back into the previous sublist such that the sorted sub list is one item larger complexity O(n2) square 
```python
arr = [2,7,1,8,5,9,11,35,25]
insertion_sort(arr)
print (arr)

[1, 2, 5, 7, 8, 11, 25, 35]
```

# Merge Sort Implementation
Merge sort is a recursive algorithm (example of divide and conquer) that continually splits a list in half.
* If the list is empty or has one item, it is sorted by definition (the base case).
* If the list has more than one item, we split the list and recursively invoke a 
* Merge sort on both halves.
* Once the two halves are sorted, the fundamental operation, called a merge, is performed.
* Merging is the process of taking two smaller sorted lists and combining them 
* together into a single, sorted, new list.
* This algorithm is used to sort a linked list
* Performance:
        - Worst case: O(nlog n)
        - Best case: O(nlog n)
        - Average case: O(nlog n)
```python
arr = [11,2,5,4,7,6,8,1,23]
merge_sort(arr)
print (arr)

[1, 2, 4, 5, 6, 7, 8, 11, 23]
```

# Quick Sort Implementation
The quick sort uses divide and conquer to gain the same advantages as the merge sort, while not using additional storage also known as "partition exchange sort".
* As a trade-off, however, it is possible that the list may not be divided in half.
* When this happens, we will see that performance is diminished.
* A quick sort first selects a value, which is called the pivot value.
* The role of the pivot value is to assist with splitting the list.
* The actual position where the pivot value belongs in the final sorted list, commonly called the split point, will  
  be used to divide the list for subsequent calls to the quick sort.
* Performance:
    - Worst case: O(n square)
    - Best case: O(nlog n)
    - Average case: O(nlog n)
```python
arr = [2,7,1,8,5,9,11,35,25]
quick_sort(arr)
print (arr)

[1, 2, 5, 7, 8, 11, 25, 35]
```

# Shell Sort Implementation
This is also called diminishing incremental sort 
* The shell sort improves on insertion sort by breaking the original list into a number of smaller sublists.
* The unique way these sun lists are chosen is the key to the shell sort
* Instead of breaking the list into sublists of contiguous items, the shell sort uses an increment ”i” to create a 
  sublist by choosing all items that are ”i” items apart.
* Shell sort is efficient for medium size lists
* Complexity somewhere between O(n) and O(n2) square
```python
arr = [45,67,23,45,21,24,7,2,6,4,90]
shell_sort(arr)
print (arr)
[2, 4, 6, 7, 21, 23, 24, 45, 45, 67, 90]
```

# Graph Implementation - Adjacency list
* We've used dictionaries to implement the adjacency list in Python which is the easiest way. 
* To implement Graph ADT we'll create two classes, Graph, which holds the master list of vertices, and Vertex, which  
  will represent each vertex in the graph.
* Each Vertex uses a dictionary to keep track of the vertices to which it is connected, and the weight of each edge. 
  This dictionary is called connectedTo. 
```python
# Create six vertices numbered 0 through 5. 
# Display the vertex dictionary
g = Graph()
for i in range(6):
    g.addVertex(i)
print(g.vertList)

# Add the edges that connect the vertices together
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
# Nested loop verifies that each edge in the graph is properly stored. 
for v in g:
   for w in v.getConnections():
       print("( %s , %s )" % (v.getId(), w.getId()))
```

# Graph Implementation - Solving Word Ladder Problem using Breadth First Search (BFS)

let’s consider the following puzzle called a word ladder. Transform the 
word “FOOL” into the word “SAGE”. In a word ladder puzzle you must make 
the change occur gradually by changing one letter at a time. At each step 
you must transform one word into another word, you are not allowed to transform a word into a non-word. 
The following sequence of words shows one possible solution to the problem posed above.
* FOOL
* POOL
* POLL
* POLE
* PALE
* SALE
* SAGE

This is impemented using dictionary

```python

# The Graph class, contains a dictionary that maps vertex names to vertex objects.
# Graph() creates a new, empty graph.
Graph()   

buildGraph()

#BFS begins at the starting vertex s and colors start gray to show that 
#it is currently being explored. Two other values, the distance and the 
#predecessor, are initialized to 0 and None respectively for the starting
#vertex. Finally, start is placed on a Queue. The next step is to begin 
#to systematically explore vertices at the front of the queue. We explore 
#each new node at the front of the queue by iterating over its adjacency 
#list. As each node on the adjacency list is examined its color is 
#checked. If it is white, the vertex is unexplored, and four things happen:
#	* The new, unexplored vertex nbr, is colored gray.
#	* The predecessor of nbr is set to the current node currentVert
#The distance to nbr is set to the distance to currentVert + 1
#nbr is added to the end of a queue. Adding nbr to the end of the queue 
#effectively schedules this node for further exploration, but not until all the 
#other vertices on the adjacency list of currentVert have been explored.

bfs()
```
# Graph Implementation - Solving Knight tour problem using Depth First Search (DFS)
The knight’s tour puzzle is played on a chess board with a single chess 
piece, the knight. The object of the puzzle is to find a sequence of 
moves that allow the knight to visit every square on the board exactly 
once. One such sequence is called a “tour.”     
we will solve the problem using two main steps:
Represent the legal moves of a knight on a chessboard as a graph.
Use a graph algorithm to find a path of length rows×columns−1rows×columns−1 
where every vertex on the graph is visited exactly once.
	To represent the knight’s tour problem as a graph we will use the 
following two ideas: Each square on the chessboard can be represented 
as a node in the graph. Each legal move by the knight can be represented
as an edge in the graph. 
```python

# The Graph class, contains a dictionary that maps vertex names to vertex objects.
# Graph() creates a new, empty graph.
Graph()

# To represent the knight’s tour problem as a graph we will use the 
# following two ideas: Each square on the chessboard can be represented 
# as a node in the graph. Each legal move by the knight can be represented
# as an edge in the graph. 

knightGraph()

# The genLegalMoves function takes the position of the knight on the 
# board and generates each of the eight possible moves. The legalCoord 
# helper function makes sure that a particular move that is generated is 
# still on the board.
genLegalMoves()

# DFS implementation
        
# we will look at two algorithms that implement a depth first search. 
# The first algorithm we will look at directly solves the knight’s tour 
# problem by explicitly forbidding a node to be visited more than once. 
# The second implementation is more general, but allows nodes to be visited 
# more than once as the tree is constructed. The second version is used in 
# subsequent sections to develop additional graph algorithms.

# The depth first exploration of the graph is exactly what we need in 
# order to find a path that has exactly 63 edges. We will see that when 
# the depth first search algorithm finds a dead end (a place in the graph 
# where there are no more moves possible) it backs up the tree to the next
# deepest vertex that allows it to make a legal move.
        
# The knightTour function takes four parameters: n, the current depth in 
# the search tree; path, a list of vertices visited up to this point; u, 
# the vertex in the graph we wish to explore; and limit the number of nodes 
# in the path. The knightTour function is recursive. When the knightTour 
# function is called, it first checks the base case condition. If we have 
# a path that contains 64 vertices, we return from knightTour with a status 
# of True, indicating that we have found a successful tour. If the path is not 
# long enough we continue to explore one level deeper by choosing a new vertex 
# to explore and calling knightTour recursively for that vertex.

# DFS also uses colors to keep track of which vertices in the graph have been visited. 
# Unvisited vertices are colored white, and visited vertices are colored gray. 
# If all neighbors of a particular vertex have been explored and we have not yet reached 
# our goal length of 64 vertices, we have reached a dead end. When we reach a dead end we 
# must backtrack. Backtracking happens when we return from knightTour with a status of False. 
# In the breadth first search we used a queue to keep track of which vertex to visit next. 
# Since depth first search is recursive, we are implicitly using a stack to help us with 
# our backtracking. When we return from a call to knightTour with a status of False, in line 11, 
# we remain inside the while loop and look at the next vertex in nbrList.

knightTour()
```
## Acknowledgments
	
* [Python for data structures algorithms and interviews course on Udemy](https://www.udemy.com)

* [Problem Solving with Algorithms and Data Structures using Python](http://interactivepython.org/runestone/static/pythonds/index.html)
