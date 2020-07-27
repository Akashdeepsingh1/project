class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

'''
        a1
    a2         a3
a7         a8      a5
     a4

'''


class Solution:
    def maxAvgSubTree(self,node):
        if node is None:
            return 0
        else:
            self.ans = float('-inf')

            def helper(node):
                if node is None:
                    return 0,0

                if node.left is None and node.right is None:
                    self.ans = max(node.val, self.ans)
                    return 1,node.val

                lc, lmean = helper(node.left)
                rc, rmean = helper(node.right)
                c = lc+rc+1
                temp_avg= ((lc*lmean) + (rc*rmean) + node.val)/c
                self.ans = max(self.ans, temp_avg)
                return c,temp_avg
            helper(node)

            return self.ans



a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a6 = Node(6)
a7 = Node(7)
a8 = Node(3.6)


a1.left = a2
a1.right = a3
a2.left = a7
a7.right = a4
a3.left = a8
a3.right = a5

'''
        a1
    a2         a3
a7         a8      a5
     a4

'''



obj = Solution()
print (obj.maxAvgSubTree (a1))

