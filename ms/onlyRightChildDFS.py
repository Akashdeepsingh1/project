class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        else:
            preorder_list = []

            def helper(root):
                if root is None:
                    return
                if root.left:
                    helper(root.left)
                if root is not None:
                    preorder_list.append(root.val)
                if root.right:
                    helper(root.right)
            helper(root)

            head = TreeNode(preorder_list[0])
            current = head

            for i in range(1,len(preorder_list)):

                temp = TreeNode(preorder_list[i])
                current.right = temp
                current = current.right
            return head



a379  = TreeNode(379)
a826 = TreeNode(826)
a379.left = a826

obj = Solution()
obj.increasingBST(a379)