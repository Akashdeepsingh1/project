# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None

        # preorder = root left right
        # inorder = left root right
        index = {k: inorder.index(k) for k in inorder}

        def createTree(start, end):
            if start > end or not preorder:
                return None

            item = preorder[0]
            node = TreeNode(item)
            loc = index[item]
            del preorder[0]

            node.left = createTree(start, loc-1)
            node.right = createTree(loc+1, end)

            return node

        return createTree(0, len(preorder)-1)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
obj = Solution()
print(obj.buildTree(preorder, inorder))
