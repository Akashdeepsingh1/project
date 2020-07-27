# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def _isValidBST (self, left, root, right):
        if root is None:
            return True
        if left >= root.val or root.val >= right:
            return False
        if not self._isValidBST (left, root.left, root.val):
            return False

        if not self._isValidBST (root.val, root.right, right):
            return False
        return True

    def isValidBST (self, root: TreeNode) -> bool:
        if not root:
            return True
        return self._isValidBST (float ('-inf'), root, float ('inf'))



a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)

a2.left = a1
a2.right = a3

obj = Solution()
print (obj.isValidBST (a2))