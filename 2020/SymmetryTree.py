class Tree:
    def __init__(self, val):
        self.val  = val
        self.left = None
        self.right = None


from collections import deque

#iterative
def symmetryTree(node):
    if node is None:
        return True
    if node and node.left is None and node.right is None:
        return True
    d = deque()
    d.append([node.left,node.right])

    while d:
        left_temp, right_temp = d.pop()
        if left_temp.val != right_temp.val:
            return False
        if left_temp.left is not None or right_temp.right is not None:
            d.append([left_temp.left,right_temp.right])
        if left_temp.right is not None or right_temp.left is not None:
            d.append([left_temp.right,right_temp.left])

    return True


#recursive

def symmetryTreeRecur(node):

