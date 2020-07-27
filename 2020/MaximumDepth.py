class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self,node):
        self.l = 0
        self.r = 0

        def helper(node):
            if node is None:
                return 0
            else:
                if node.left:
                    print(self.l)
                    self.l = helper(node.left)+1
                if node.right:
                    print(self.r)
                    self.r = helper(node.right)+1
                return max(self.l,self.r)

        return helper(node)

    def maxDepthIterative(self,node):
        from collections import deque
        q1 = deque()
        q2 = deque()
        if node is None:
            return 0
        else:
            count = 0
            q1.append(node)

            while len(q1)>0:
                count+=1
                while len(q1)>0:
                    item = q1.pop()
                    if item.left is not None:
                        q2.append(item.left)
                    if item.right is not None:
                        q2.append(item.right)
                q1.extend(q2)
                q2.clear()
            return count



def maxDepth(node):
    if node is None:
        return 0
    else:
        return max(maxDepth(node.left)+1,maxDepth(node.right)+1)


a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a6 = Node(6)

a1.left = a2
a1.right = a3
a3.left = a4
a3.right = a5
a5.left = a6

obj = Solution()
#print (obj.maxDepth (a1))
print(obj.maxDepthIterative(a1))
print(maxDepth(a1))