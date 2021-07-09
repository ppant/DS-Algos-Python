# Stack class implementation

# Author: Pradeep K. Pant, https://pradeeppant.com

# Implement basic operation in stack
# Stack follows LIFO sequence

# Initialize Stack class and set a empty list
class Stack(object):
    def __init__(self):
        self.items=[]
# Check if list is empty
    def isEmpty(self):
        return self.items == []
# Push an element in a stack 
    def push(self,item):
        self.items.append(item)
# POP an element from top of the stack
    def pop(self):
        return self.items.pop()
# Just peek into top element of the stack (don't perform any operation)
    def peek(self):
        return self.items[len(self.items)-1]
# Check size of a stack (how may elements are stored)
    def size(self):
        return len(self.items)
    
# Test
# Create an object and try basic operation
sObj = Stack()
# Check if list is empty
print (sObj.isEmpty())
# Add an element 
sObj.push(1)
# Add another element
sObj.push(2)
# Peek into stack and check top element
print (sObj.peek())
# Check again if empty
print (sObj.isEmpty())
# Check size
print (sObj.size())
# show items 
print (sObj.items)
# Remove item (First-In-First-Out)
print (sObj.pop())
# Check again items 
print (sObj.items)