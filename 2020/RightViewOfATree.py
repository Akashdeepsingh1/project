class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class classy:
    def __init__(self):
        pass

    def rightView(self, root):
        from collections import deque
        d = deque()

        d.append((root, 0))
        count = []

        while d:
            item,level=d.popleft()
            if level not in count:
                print(item.val)
                count.append(level)
            if item.right:
                d.append((item.right,level+1))
            if item.left:
                d.append((item.left,level+1))



a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a6 = Node(6)
a7 = Node(7)
a8 = Node(8)
a9 = Node(9)

a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5

a3.left = a6

a4.right = a7
a5.left = a8

a7.left = a9

obj = classy()

obj.rightView(a1)
