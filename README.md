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
```	sum_arr_uniq_pairs([1,2,2,3,4,1,1,3,2,1,3,1,2,2,4,0],5)
	would return 2 pairs:

 	(2,3)
 	(1,4)
 ```
 
## Find a missing element in an array/list ##	
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.
Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
```
Input:
find_missing_ele([1,2,3,4,5,6,7],[3,7,2,1,4,6])
Output:
5 is the missing number
```

## Stack class implementation
Implement basic stack operations (LIFO)
```
push() - Push an element in a stack 
pop()- POP an element from top of the stack
peek() - Just peek into top element of the stack (don't perform any operation)
```

## Queue class implementation
Implement basic Queue operations (FIFO)
```
enqueue - adding a element to the queue 
dequeue - removing an element from the queue
```

## Deque (DECK) class implementation
Implement basic operation in deque (Add and remove elements both at front and rear)
``` 
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
```
print (check_parentheses_match('([])'))
print (check_parentheses_match('[](){([[[]]])'))
```

# Queue with 2 stack implementation

# implement a Queue using two Stacks
This is a classic problem. We need to use the basic charactristics of stack (popping out elements in reverse order) will make a queue

# Singly Linked List class implementation
Implement basic skeleton for a Singly Linked List 

# Doubly Linked List class implementation
Implement basic skeleton for a Doubly Linked List 

## Acknowledgments

* Python for data structures algorithms and interviews course on [Udemy](https://www.udemy.com)
