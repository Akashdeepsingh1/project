class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def levelOrder(self, node):
        final_list = [[node.val]]
        working_list1 = [node]
        working_list2 = []
        data_list = []

        while working_list1:
            curr_node = working_list1.pop()
            if curr_node.left:
                working_list2.append(curr_node.left)
                data_list.append(curr_node.left.val)
            if curr_node.right:
                working_list2.append(curr_node.right)
                data_list.append(curr_node.right.val)

            if not working_list1 and data_list:
                final_list.append(data_list[:])
                working_list1 = working_list2[:]
                working_list2 = []
                data_list = []
        return final_list

    def print_all(self, final_list):
        for each in final_list:
            print(each)


a1 = Node('1')
a2 = Node('2')
a3 = Node('3')
a4 = Node('4')
a5 = Node('5')


b1 = Node('6')
b2 = Node('7')
b3 = Node('8')
b4 = Node('9')
b5 = Node('10')

a1.left = a2
a1.right = a3
a2.left = a4
a3.right = a5
a2.right = b2
a5.left = b3
a5.right = b1
a4.left = b4
a4.right = b5


obj = Solution()
data = obj.levelOrder(a1)
obj.print_all(data)
