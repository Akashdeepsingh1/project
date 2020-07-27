class Node:
    def __init__(self,val):
        self.val = val
        self.children = []

class Solution:
    def maxAvg(self,node):
        if node is None:
            return None
        else:
            self.ans = float('-inf')
            def helper(node):
                if node is None:
                    return 0,0
                if len(node.clildren) == 0:
                    self.ans = max(self.ans, node.val)
                    return 1,node.val
                c = 1
                temp_sum = node.valc
                for i in range(len(node.children)):
                    temp_c, temp_sum_1 = helper(node.children[i])
                    c += temp_c
                    temp_sum += temp_sum_1
                self.ans = max(self.ans, temp_sum/c)

                return temp_sum



