class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class MergeTree:
    def merge(self, a, b):
        if not a and not b:
            return None
        elif not a and b:
            return b
        elif not b and a:
            return a
        else:
            a.data += b.data
            a.left = self.merge(a.left, b.left)
            a.right = self.merge(a.right, b.right)
            return a

    def printAll(self, node):
        if not node:
            return
        self.printAll(node.left)
        print(node.data)
        self.printAll(node.right)


a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)


b1 = Node(6)
b2 = Node(7)
b3 = Node(8)
b4 = Node(9)
b5 = Node(10)

a1.left = a2
a1.right = a3
a2.left = a4
a3.right = a5

b1.left = b2
b1.right = b3
b2.right = b4
b3.left = b5


obj = MergeTree()
obj.printAll(obj.merge(a1, b1))
