# Binary Search Tree Check - Validate BST
# Author: Pradeep K. Pant, ppant@cpan.org
# Problem Statement
# Given a binary tree, check whether it’s a binary search tree or not.
# Solution strategy
# 
# Here is a simple solution- If a tree is a binary search tree, then traversing 
# the tree inorder should lead to sorted order of the values in the tree. So, we 
# can perform an inorder traversal and check whether the node values are sorted or not. 

tree_vals = []

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        tree_vals.append(tree.getRootVal())
        inorder(tree.getRightChild())
        
def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)
# Test
inorder(tree)
sort_check(tree_vals)


