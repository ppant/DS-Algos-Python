# Queue class implementation

# Author: Pradeep K. Pant, ppant@cpan.org

# Implement basic operation in Queue
# Stack follows FIFO sequence
# enqueue: adding a element to the queue
# dequeue: Removing an element from queue

# Initialize queue class and set a empty list
class Queue(object):
    def __init__(self):
        self.items=[]
# Check if list is empty
    def isEmpty(self):
        return self.items == []
# Insert new element in the queue  
    def enqueue(self,item):
        self.items.insert(0,item)
# Remove element from queue
    def dequeue(self):
        return self.items.pop()
# Check size of a queue (how may elements are stored)
    def size(self):
        return len(self.items)

# Test
# Create an object and try basic operation
qObj = Queue()
# Check if list is empty
print (qObj.isEmpty())
# Add an element 
qObj.enqueue(1)
# Add another element
qObj.enqueue(2)
# Check again if empty
print (qObj.isEmpty())
# Check size
print (qObj.size())
# show items 
print (qObj.items)
# Remove item (Last-In-First-Out)
print (qObj.dequeue())
# Check again items i
print (qObj.items)