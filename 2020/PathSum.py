class Node:
    def __init__ (self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__ (self):
        self.ans = float ('-inf')
        self.numList = []

    def _traverse(self,root):
        if root is None:
            return
        self._traverse(root.left)
        self.numList.append(root.val)
        self._traverse(root.right)


    def maxPathSum (self, root):
        if root is None:
            return 0
        self._traverse(root)

        temp_Sum =0

        for each in self.numList:
            temp_Sum = max(temp_Sum+ each, each)
            self.ans = max(temp_Sum,self.ans)


        print(self.numList)




a1 = Node(1)
a2 = Node(2)
a3 = Node(3)

a1.left = a2
a1.right = a3

obj = Tree()
obj.maxPathSum(a1)
print(obj.ans)

#t = [-10, 9, 20, null, null, 15, 7]


a10 = Node(-10)
a9 = Node(9)
a20 = Node(20)
a15 = Node(15)
a7 = Node(7)
obj.numList = []

a10.left = a9
a10.right = a20
a20.left = a15
a20.right = a7
obj.maxPathSum(a10)
print(obj.ans)



d = {1:2, 3:1, 5:-1}
sorted(d,key=lambda i:i)
