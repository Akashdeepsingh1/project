'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


'''


class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        pass

    def validateBST(self,node):
        l = float('-inf')
        r = float('inf')
        from collections import deque
        d = deque((node,l,r))
        while d:
            item,left, right =d.pop()
            if left<item.val<right:
                if item.left is not None:
                    d.append((item.left,left,item.val))
                if item.right is not None:
                    d.append((item.right,item.val,right))
            else:
                return False
        return True