#  Singly Linked List cycle check implementation

# Author: Pradeep K. Pant, ppant@cpan.org
# Given a singly linked list, write a function which takes in the first node in 
# a singly linked list and returns a boolean indicating if the linked list contains 
# a "cycle". A cycle is when a node's next point actually points back to a previous 
# node in the list. This is also sometimes known as a circularly linked list.

# Solution strategy is to use analogy of two runners, one is fater than other, 
# if there is no cycle faster runner will newver meet slower runner and if there is a cycle 
# faster runner will eventually cross slower runner, with the analogy we can set two markers
# first is on nextnode and otherone on next to next node

# There could be other ways to solve this like using a set where we put the visted 
# node and then check
# Initialize singly linked list class
class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        
    def cycle_check(node):
        # Set two pointers initialize to passed node
        pt1 = node
        pt2 = node
        # loop through end of the list
        while pt2 != None and pt2.nextnode != None:
            pt1 = pt1.nextnode
            pt2 = pt2.nextnode.nextnode;
            # If pt2 meet pt1 then there is a cycle
            if pt2 == pt1:
                return True
            return False
# Test
# Create a Linked List 
a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)
# Create a cycle
a.nextnode = b
b.nextnode = c
# This is a cycle -- to test non-cycle scnerio comment this line
c.nextnode = a

print (a.value)
print (b.value)
print (c.value)

obj = LinkedListNode()
obj.cycle_check(a)


