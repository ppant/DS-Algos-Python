# Stack implementation

# Author: Pradeep K. Pant, ppant@cpan.org

# Implement basic operation in stack
# Stack follows LIFO sequence

# Initialize Stack class and set a empty list
class Stack(object):
    def __init__(self):
        self.items=[]
# Checi if list is empty
    def isEmpty(self):
        return self.items == []
# Push an element in a stack 
    def Push(self,item):
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
    