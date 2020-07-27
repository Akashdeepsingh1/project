class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def zigzag(root):
    if root is None:
        return []
    if root and root.left is None and root.right is None:
        return [root]
    else:
        from collections import deque
        d = deque()
        temp = []
        temp_val = []
        final_list = [[root.val]]
        d.append(root)
        flip = True
        while d:
            while d:
                item = d.popleft()
                if item.left is not None:
                    temp.append(item.left)
                    temp_val.append(item.left.val)
                if item.right is not None:
                    temp.append(item.right)
                    temp_val.append(item.right.val)
            if temp_val:
                if flip:
                    flip = False
                    temp_val.reverse()
                    final_list.append(temp_val)
                else:
                    flip = True
                    final_list.append(temp_val)
                d.extend(temp)
                temp = []
                temp_val = []

