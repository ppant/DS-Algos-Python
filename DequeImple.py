# Deque (DECK) class implementation

# Author: Pradeep K. Pant, ppant@cpan.org

# Implement basic operation in Queue
# Stack follows FIFO sequence
# enqueue: adding a element to the queue
# dequeue: Removing an element from queue

# Initialize queue class and set a empty list
class Deque(object):
    def __init__(self):
        self.items=[]
# Check if list is empty
    def isEmpty(self):
        return self.items == []
# Insert a new element at the front  
    def addFront(self,item):
        self.items.append(item)
# Insert a new element at the rear   
    def addRear(self,item):
        self.items.insert(0,item)
# Remove at the front
    def removeFront(self):
        return self.items.pop()
# Remove at the rear
    def removeRear(self):
        return self.items.pop(0)
# Check size of a deque (finally, how may elements are stored)
    def size(self):
        return len(self.items)

# Test
# Create an object and try basic operation
dqObj = Deque()
# Check if list is empty
print (dqObj.isEmpty())
# Add an element at the front
dqObj.addFront(1)
# Add another element at the front
dqObj.addFront(2)
# Add an element at the rear
dqObj.addRear(9)
# Add another element at the rear
dqObj.addRear(10)
# Check again if empty
print (dqObj.isEmpty())
# Check size
print (dqObj.size())
# show items 
print (dqObj.items)
# Remove from front
print (dqObj.removeFront())
# Remove from front
print (dqObj.removeRear())
# Check again items 
print (dqObj.items)