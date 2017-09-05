#  Doubly Linked List class implementation

# Author: Pradeep K. Pant, ppant@cpan.org

# Implement basic skeleton for a doubly Linked List 

# Initialize linked list class
class DoublyLinkedListNode(object):
    def __init__(self,value):
        self.value = value
        self.prev_node = None
        self.next_node = None

# Test
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