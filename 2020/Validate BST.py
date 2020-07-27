class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def validateBST(root):
    l = float('-inf')
    r = float('inf')
    from collections import deque
    d = deque()
    d.append([root,l,r])

    while d:
        item = d.pop()
        if item[0].val<= item[1] or item[0].val>= item[2]:
            return False
        if item[0].left is not None:
            d.append([item[0].left,item[1],item[0].val])
        if item[0].right is not None:
            d.append([item[0].right,item[0].val,item[2]])
    return True


a2 = Tree(2)
a1 = Tree(1)
a3 = Tree(3)
a2.left  = a1
a2.right = a3

print(validateBST(a2))

'''
#[5,1,4,null,null,3,6]
a5 = Tree(5)
a1 = Tree(1)
a4 = Tree(4)
a3 = Tree(3)
a6 = Tree(6)
a5.left = a1
a5.right = a4
a4.left = a3
a4.right = a6
print (validateBST (a5))

'''
'''
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

print (validateBST (a10))
'''