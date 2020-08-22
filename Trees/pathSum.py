class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root, requiredSum):
    if not root:
        return False

    def _pathSum(root, requiredSum, actualSum):
        if not root:
            return False
        if root.val + actualSum == requiredSum and root.left is None and root.right is None:
            return True
        l = r = 0
        if root.left:
            l = _pathSum(root.left, requiredSum, actualSum +
                         root.val)
        if root.right:
            r = _pathSum(root.right, requiredSum, actualSum +
                         root.val)
        return l or r
    return _pathSum(root, requiredSum, 0)


a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(8)
d = TreeNode(11)
e = TreeNode(13)
f = TreeNode(4)
g = TreeNode(7)
h = TreeNode(2)
i = TreeNode(1)

a.left = b
a.right = c
b.left = d
d.left = g
d.right = h
c.left = e
c.right = f
f.right = i

print(pathSum(a, 22))
