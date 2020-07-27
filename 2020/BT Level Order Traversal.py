class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def levelOrder(root):
    if root is None:
        return []
    from collections import deque
    d = deque
    temp = []
    final_list = [[root]]
    d.append(root)
    while d:
        while d:
            item = d.popleft()
            if item.left is not None:
                temp.append(item.left)
            if item.right is not None:
                temp.append(item.right)
        if temp:
            d.extend(temp)
        final_list.append(temp)
    return final_list