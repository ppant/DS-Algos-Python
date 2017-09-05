# Build a tree and fetch nodes and insert using list of lists
# Author: Pradeep K. Pant, ppant@cpan.org
#from test import testEqual
# Test code

def buildTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]
# Test data
ttree = buildTree('a')
insertLeft(ttree,'b')
insertRight(getLeftChild(ttree),'d')
insertRight(ttree,'c')
insertLeft(getRightChild(ttree),'e')
insertRight(getRightChild(ttree),'f')
#print(getLeftChild(ttree))
print(getLeftChild(ttree))
print(getRightChild(ttree))
#insertLeft(ttree,'b')
#insertRight(ttree,'d')
#insertRight(ttree,'c')
#insertLeft(ttree,'e')
#insertRight(ttree,'f')
#l = getLeftChild(ttree)
#print(l)
#testEqual(getRootVal(getRightChild(ttree)),'c')
#testEqual(getRootVal(getRightChild(getLeftChild(ttree))),'d')
#testEqual(getRootVal(getRightChild(getRightChild(ttree))),'f')
#x = BinaryTree('a')
#insertLeft(x,'b')
#insertRight(x,'c')
#insertRight(getRightChild(x),'d')
#insertLeft(getRightChild(getRightChild(x)),'e')
