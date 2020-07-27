class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None




class Classy:
    def __init__(self):
        self.ans = 0

    def _helper(self, node):
        if node is None:
            return 0

        left_val = self._helper(node.left)
        right_val = self._helper(node.right)
        left_sum  = right_sum = 0
        if node.left and node.left.val == node.val:
            left_sum = left_val+ 1

        if node.right and node.right.val == node.val:
            right_sum = right_val + 1

        self.ans = max(self.ans, left_sum+right_sum)
        return max(left_sum,right_sum)


    def similarNodeLength(self, node):
        if not Node:
            return 0
        return self._helper(node)



a51 = Node(5)
a52 = Node(5)
a53 = Node(5)
a11 = Node(1)
a41 = Node(4)
a42 = Node(4)
a51.left = a11
a11.left = a41
a11.right = a42
a51.right = a52
a52.right = a53

obj = Classy()
print (obj.similarNodeLength (a51))
