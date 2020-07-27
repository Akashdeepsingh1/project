class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

    def __int__(self):
        pass


#Loop
def postorderTraversal(root):
    ans = []
    if not root: return ans
    stack = [(root, False)]
    while stack:
        node, ready = stack.pop()
        print(node.val)
        if ready:
            ans.append(node.val)
        else:
            # preorder
            # if node.right: stack.append((node.right, False))
            # if node.left: stack.append((node.left, False))
            # stack.append((node, True))

            # in-order
            # if node.right: stack.append((node.right, False))
            # stack.append((node, True))
            # if node.left: stack.append((node.left, False))

            # post-order
            stack.append((node, True))
            if node.right: stack.append((node.right, False))
            if node.left: stack.append((node.left, False))
    return ans




head = TreeNode(1)
head.right = TreeNode(2)
head.right.left = TreeNode(3)


print(postorderTraversal(head))

