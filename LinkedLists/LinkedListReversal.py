#  Reverse a linked list implementation

# Author: Pradeep K. Pant, ppant@cpan.org
# Aim is to write a function to reverse a Linked List in place. The function will take in 
# the head of the list as input and return the new head of the list.

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
        # Make sure to copy the current nodes next node to a variable nextnode
        # Before overwriting as the previous node for reversal
         nextnode = current.nextnode

         # Reverse the pointer to the previous node
         current.nextnode = previous

         # Go one forward in the list
         previous = current
         current = nextnode
    return previous
    
# Test
# Create a Linked List 
a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)
d = LinkedListNode(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print (f"a.nextnode: {a.nextnode.value}")
print (f"b.nextnode: {b.nextnode.value}")
print (f"c.nextnode: {c.nextnode.value}")

# Call the reverse()
new_head = reverse(a)
print (f"New head value: {new_head.value}")
print (f"d.nextnode: {d.nextnode.value if d.nextnode else 'None'}")
print (f"c.nextnode: {c.nextnode.value if c.nextnode else 'None'}")
print (f"b.nextnode: {b.nextnode.value if b.nextnode else 'None'}")
