
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
# p = 5
# q = 1

n3 = TreeNode(3)
n5 = TreeNode(5)
n1 = TreeNode(1)
n6 = TreeNode(6)
n2 = TreeNode(2)
n0 = TreeNode(0)
n8 = TreeNode(8)

n3.left = n5
n3.right = n1
n5.left = n6
n5.right = n2
n2.left = n0
n1.right = n8


class Solution:
    def __init__(self):
        self.final_path = []

    def root2node(self, root, node, path):
        if not root:
            return False
        path.append(root)
        if root == node:
            self.final_path = path[:]
            return True
        if self.root2node(root.left, node, path) or self.root2node(root.right, node, path):
            return True
        path.pop()

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None
        p_path = []
        if self.root2node(root, p, []):
            p_path = self.final_path[:]
        self.final_path = []
        q_path = []
        if self.root2node(root, q, []):
            q_path = self.final_path[:]

        print(p_path)
        print(q_path)

        if p_path and q_path:
            item = None
            while p_path and q_path and p_path[0] == q_path[0]:
                item = p_path[0]
                del p_path[0]
                del q_path[0]

            print((item, item.val))
        else:
            return None

    def lca2(self, root, p, q):
        if not root or not p or not q:
            return None


obj = Solution()
obj.lowestCommonAncestor(n3, n5, n2)
