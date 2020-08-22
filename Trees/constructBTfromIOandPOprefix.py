from TreeNode import TreeNode


class Solution:
    def __init__(self):
        pass

    def constructTree(self, inOrder, postOrder):
        if not inOrder or not postOrder:
            return None

            # inorder = lt Root right
            # postorder = lrt right root

        index = {k: inOrder.index(k) for k in inOrder}

        def _constructTree(start, end):
            if start > end or not inOrder:
                return None

            item = postOrder.pop()
            node = TreeNode(item)

            pos = index[item]

            node.right = _constructTree(pos+1, end)
            node.left = _constructTree(start, pos-1)

            return node
        return _constructTree(0, len(postOrder)-1)

    def print_all(self, node):
        if not node:
            return

        print(node.val)
        obj.print_all(node.left)
        obj.print_all(node.right)


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

obj = Solution()
obj.print_all(obj.constructTree(inorder, postorder))
