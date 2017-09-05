#  Linked list Nth to last node

# Author: Pradeep K. Pant, ppant@cpan.org
# Aim is a function that takes a head node and an integer value n and then 
# returns the nth to last node in the linked list.
# Solution strategy 
# One approach to this problem is this:
# Imagine you have a bunch of nodes and a "block" which is n-nodes wide. We 
# could walk this "block" all the way down the list, and once the front of the 
# block reached the end, then the other end of the block would be a the Nth node!
# So to implement this "block" we would just have two pointers a left and right 
# pair of pointers. Let's mark out the steps we will need to take:
#Walk one pointer n nodes from the head, this will be the right_point
#Put the other pointer at the head, this will be the left_point
#Walk/traverse the block (both pointers) towards the tail, one node at a time, 
# keeping a distance n between them. Once the right_point has hit the tail, 
# we know that the left point is at the target.

# First initialize singly linked list class
class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        
    def nth_to_last_node(n,head):
        # Set variables 
        # Left pointer at head and right pointer at place nth distance from 
        # left pointer
        # so we have blocks between left and right pointers we keep them moving
        # till right pointer hits the tail
        left_pointer = head
        right_pointer = head
        # setting up right pointer based on the val of n
        for i in range(n-1):
            # Check edge cases
            if not right_pointer.nextnode:
                raise LookupError('Error: n is larger than linked list')
            right_pointer = right_pointer.nextnode
        # finally check if right pointer is hitting the tail if so return left pointer
        while right_pointer.nextcode:
            left_pointer = left_pointer.nextnode
            right_pointer = right_pointer.nextnode
        return left_pointer
# Test
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
