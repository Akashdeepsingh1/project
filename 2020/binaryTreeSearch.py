


class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class BSTSearch:
    def __init__(self):
        pass


    def searchInRange(self, node, lower, high):
        if node is None:
            return 0

        if lower <= node.val <= high:
            print(node.val)
            if node.left is not None:
                self.searchInRange(node.left,lower,high)
            if node.right is not None:
                self.searchInRange(node.right,lower,high)

        elif lower < node.val and node.val > high:
            if node.left is not None:
                self.searchInRange(node.left, lower, high)

            else:
                return 0

        elif node.val < lower and node.val < high:
            if node.right is not None:
                self.searchInRange(node.right,lower,high)
            else:
                self.assertEqual()
                return 0

        else:
            return 0




a500 = Node(500)
a300 = Node(300)
a200 = Node(200)
a100 = Node(100)
a400 = Node(400)

a600 = Node(600)
a700 = Node(700)

a800 = Node(800)
a900 = Node(900)



a500.left = a300
a300.left = a200
a200.left = a100
a300.right  = a400

#a500.left = a600
a500.right = a700
a700.left = a800
a700.right = a900
obj = BSTSearch()
obj.searchInRange(a500,200,701)
