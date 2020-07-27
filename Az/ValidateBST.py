from collections import deque

class BST:
    # iterative
    def iterativeValidateBST(self,node):
        l = float('-inf')
        h = float('inf')

        q = deque([[node, l ,h ]])
        while q:
            temp = q.pop()

            print(temp[0].val)
            l = temp[1]
            h = temp[2]
            if temp[0].val <= l:
                return False
            if temp[0].val >= h:
                return False
            if temp[0].right is not None:
                q.append([node.right,node.val,h])

            if temp[0].left is not None:
                q.append([node.left,l,node.val])

        return True

class Tree:
    def __init__(self,val):
        self.val  = val
        self.right = None
        self.left = None


#[5,1,4,null,null,3,6]
#[10,5,15,null,null,6,20]

a10 = Tree(10)
a5 = Tree(5)
a15 = Tree(15)
a6 = Tree(6)
a20 = Tree(20)
a10.left = a5
a10.right = a15
a15.left = a6
a15.right = a20



#
#
#
#
#
# a5 = Tree(5)
# a1 = Tree(1)
# a4 = Tree(4)
# a3 = Tree(3)
# a6 = Tree(6)
#
#
# b1 = Tree(1)
# b2 = Tree(2)
# b3 = Tree(3)
# b2.left = b1
# b2.right = b3
#
# a5.left = a1
# a5.right = a4
# a4.left = a3
# a4.right = a6
#
obj = BST()
# print (obj.iterativeValidateBST (a5))
# print(obj.iterativeValidateBST(b2))

print (obj.iterativeValidateBST (a10))