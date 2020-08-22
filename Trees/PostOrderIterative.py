class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


a = TreeNode('a')
b = TreeNode('b')
c = TreeNode('c')
d = TreeNode('d')
e = TreeNode('e')
f = TreeNode('f')
g = TreeNode('g')
h = TreeNode('h')

a.left = b
b.left = d
b.right = e
e.left = f
e.right = g
a.right = c
c.right = h


class Solution:
    def postorderTraversal(self, root: TreeNode):
        stack, output = [], []
        while root or stack:
            # push nodes: right -> node -> left
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            root = stack.pop()

            # if the right subtree is not yet processed
            if stack and root.right == stack[-1]:
                stack[-1] = root
                root = root.right
            # if we're on the leftmost leaf
            else:
                output.append(root.val)
                root = None

        return output


obj = Solution()
print(obj.postorderTraversal(a))
