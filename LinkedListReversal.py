#  Reverse a linked list implementation

# Author: Pradeep K. Pant, ppant@cpan.org
# Aim is to write a function to reverse a Linked List in place. The function will take in 
# the head of the list as input and return the new head of the list.

# Initialize singly linked list class
class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        
    def reverse(head):
        # Set variables current, previous and nextnode
        current = head
        previous = None
        nextnode = None 
        
         # until we have gone through to the end of the list
        while current:        
            # Make sure to copy the current nodes next node to a variable next_node
            # Before overwriting as the previous node for reversal
             nextnode = current.nextnode

             # Reverse the pointer ot the next_node
             current.nextnode = previous

             # Go one forward in the list
             previous = current
             current = nextnode
    
# Test
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

