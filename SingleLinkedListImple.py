#  Singly Linked List class implementation

# Author: Pradeep K. Pant, ppant@cpan.org

# Implement basic skeleton for a singly Linked List 

# Initialize singly linked list class
class LinkedListNode(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None

# Test
# Adde node
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