class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class MergeTree:
    def __init__(self):
        self.finalPaths = []

    def allPath(self, node, path):
        if node is None:
            return
        path.append(node.data)
        if node is not None and (node.left is None and node.right is None):
            self.finalPaths.append(path[:])

        self.allPath(node.left, path)
        self.allPath(node.right, path)
        path.pop()

    def printAll(self, node):
        if not node:
            return
        self.printAll(node.left)
        print(node.data)
        self.printAll(node.right)


a1 = Node('1')
a2 = Node('2')
a3 = Node('3')
a4 = Node('4')
a5 = Node('5')


b1 = Node('6')
b2 = Node('7')
b3 = Node('8')
b4 = Node('9')
b5 = Node('10')

a1.left = a2
a1.right = a3
a2.left = a4
a3.right = a5
a2.right = b2
a5.left = b3
a5.right = b1
a4.left = b4
a4.right = b5

obj = MergeTree()
obj.allPath(node=a1, path=[])
print(obj.printAll(a1))
print(obj.finalPaths)
