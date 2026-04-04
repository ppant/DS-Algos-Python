# Binary Search Tree Check - Validate BST
# Author: Pradeep K. Pant, ppant@cpan.org

# Given a binary tree, check whether it’s a binary search tree or not.
# Strategy: If a tree is a BST, then an in-order traversal should return
# values in sorted order.

class Node:
    def __init__(self, k, val):
        self.key = k
        self.payload = val
        self.leftChild = None
        self.rightChild = None

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getRootVal(self):
        return self.key

def inorder(tree, tree_vals):
    if tree != None:
        inorder(tree.getLeftChild(), tree_vals)
        tree_vals.append(tree.getRootVal())
        inorder(tree.getRightChild(), tree_vals)
        
def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)

# Test
root = Node(3, "red")
root.leftChild = Node(2, "at")
root.rightChild = Node(4, "blue")
root.rightChild.rightChild = Node(6, "yellow")

vals = []
inorder(root, vals)
print(f"In-order traversal: {vals}")
print(f"Is BST? {sort_check(vals)}")

# Negative test
root.leftChild.key = 5 # Break BST property
vals = []
inorder(root, vals)
print(f"In-order traversal (broken): {vals}")
print(f"Is BST? {sort_check(vals)}")
