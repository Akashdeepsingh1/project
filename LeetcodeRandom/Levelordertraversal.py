def traverse(stack):
    root = stack.pop
    if root is None:
        return
    if root.left and root.right:
        final_list.append([root.left,root.right])
        stack.append(root.left)
        stack.append(root.right)
    elif root.left and not root.right:
        final_list.append([root.left])
        
