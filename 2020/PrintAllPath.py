"""
Python program to print all path from root to
leaf in a binary tree
"""


# binary tree node contains data field ,
# left and right pointer
class Node:
    # constructor to create tree node
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None


# function to print all path from root
# to leaf in binary tree
def printPaths (root):
    # list to store path
    path = []
    printPathsRec (root, path, 0)


def printPathsRec (root, path, pathLen):

    if root is None:
        return

    if (len (path) > pathLen):
        path[pathLen] = root.data
    else:
        path.append (root.data)
    pathLen = pathLen + 1

    if root.left is None and root.right is None:
        printArray (path, pathLen)
    else:
        printPathsRec (root.left, path, pathLen)
        printPathsRec (root.right, path, pathLen)

def printArray (ints, len):
    for i in ints[0: len]:
        print (i, " ", end="")
    print ()

""" 
Constructed binary tree is 
		10 
		/ \ 
	8	 2 
	/ \ / 
	3 5 2 
"""
root = Node (10)
root.left = Node (8)
root.right = Node (2)
#root.left.left = Node (3)
root.left.right = Node (5)
root.right.left = Node (2)
#printPaths (root)










class Path:
    def __init__(self):
        self.stack = []
        self.ans = []

    def _getPath(self, node):
        if node.left is None and node.right is None:
            self.ans.append(self.stack[:])
        if node.left is not None:
            self.stack.append(node.left.data)
            self._getPath(node.left)
        if node.right is not None:
            self.stack.append(node.right.data)
            self._getPath(node.right)
        if self.stack:
            self.stack.pop()

    def getPath(self,node):
        if not node:
            return []
        else:
            self.stack.append(node.data)
            self._getPath(node)


    def print_all(self):
        print(self.ans)







obj = Path()
obj.getPath(root)
obj.print_all()

