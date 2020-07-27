class Tree:
    def __init__(self, val ):
        self.data = val
        self.left = None
        self.right = None

def maxsum(root):
    if root is None:
        return 0

    l = maxsum(root.left)
    r = maxsum(root.right)

    max_single = max(max(l,r) + root.data, root.data)

    max_top = max(max_single, l+r+ root.data)

    maxsum.res = max(maxsum.res, max_top)

    return max_single


'''
                5
            1        4
                  a3     a6
            
'''

a5 = Tree(5)
a1 = Tree(1)
a4 = Tree(4)
a3 = Tree(3)
a6 = Tree(6)
a5.left = a1
a5.right = a4
a4.left = a3
a4.right = a6

maxsum.res = float('-inf')
print (maxsum (a5))