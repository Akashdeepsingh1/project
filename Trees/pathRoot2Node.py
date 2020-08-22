
# def temp_fun(count, list_add):
#     if count >= 5:
#         return list_add

#     count += 1
#     list_add.append(count)
#     return temp_fun(count, list_add)


'''
temp_fun(0,[])
    
    None
    temp_fun(1, [1])
        
        None
        temp_fun(2, [1,2])
            
            None
            temp_fun(3, [1,2,3])
                
                None
                temp_fun(4, [1,2,3,4])
                    
                    [1,2,3,4,5]
                    temp_fun(5,[1,2,3,4,5])




print(temp_fun(0, []))
'''

# 1 never append the list inside the function call
# 2 apart from the terminating condition. Always return the data to your parents in bottom up.
# in top down use the variable.

from TreeNode import TreeNode

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a6 = TreeNode(6)
a7 = TreeNode(7)

a1.left = a2
a1.right = a3
a2.left = a4
a3.left = a5
a3.right = a6
a6.left = a7


class Solution:
    def __init__(self):
        self.final_path = []

    def find_path(self, root, node, path):
        if not root:
            return False
        path.append(root)
        if root == node:
            self.final_path = path[:]
            return True
        if self.find_path(root.left, node, path) or self.find_path(root.right, node, path):
            return True
        path.pop()

    def main_fun(self, root, node):
        if self.find_path(root, node, []):
            for each in self.final_path:
                print(each.val)
        else:
            return False


obj = Solution()
print(obj.main_fun(a1, a7))
