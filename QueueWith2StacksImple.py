# Queue with 2 stack implementation

# Author: Pradeep K. Pant, ppant@cpan.org

# Problem Statement: Given the Stack class below, implement a Queue class using two stacks!

# create a class 
class QueueWith2Stack(object):
    # Initialize class
    def __init__(self):
        # initialize two empty stack using python list which we have to use to implement queue
        self.stack1 = []
        self.stack2 = []
    # Append a  element
    def enqueue(self,element):
        # add a element in the queue
        print ("Appending",+element)
        self.stack1.append(element)
        return True
    # take the element out
    def dequeue(self):
        # remove a element from the queue
        # Check for empty 
        if not self.stack2:
            while self.stack1:
                # Append in second stack the valu of pop from first list
                # reverse order continuous popping of the element 
                self.stack2.append(self.stack1.pop())
        print ("Poping element")
        return self.stack2.pop()

# Test set 1
# Create a object of the class
qObj = QueueWith2Stack()
# Add an element 
qObj.enqueue(1)
# Add another element
qObj.enqueue(2)
# Add more element
qObj.enqueue(4)
# Add more element
qObj.enqueue(8)
# Remove item
print (qObj.dequeue())
# Remove item 
print (qObj.dequeue())
# Remove item
print (qObj.dequeue())
# Remove item 
print (qObj.dequeue())

# Test set 2
for i in range(5):
    qObj.enqueue(i)
    
for i in range(5):
    print (qObj.dequeue())
