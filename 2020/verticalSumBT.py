class TreeNode:
    def __init__(self, val ):
        self.val  = val
        self.left = None
        self.right = None




class verticalSum:
    def __init__(self):
        self.ans = []

    def _vSum(self, node, ls):
        if node.left is None and node.right is None:
            self.ans.append(sum(ls))

        if node.left:
            ls.append(node.left.val)
            self._vSum(node.left,ls)
        if node.right:
            ls.append(node.right.val)
            self._vSum(node.right,ls)
        if ls:
            ls.pop()



    def vSum(self, node):
        if node is None:
            return 0
        else:
            self._vSum(node,[node.val])
            return self.ans




a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a5 = TreeNode(5)
a6 = TreeNode(6)
a7 = TreeNode(7)

a8 = TreeNode(8)


a2.left = a1
a2.right = a3
a1.left = a5
a5.right = a6
a3.left = a7
a5.left = a8

'''
        2
    1         3
    
 5          7    
8      6   
'''

obj = verticalSum()
print (obj.vSum (a2))

