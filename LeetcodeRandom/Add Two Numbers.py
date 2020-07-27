class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self,l1:ListNode, l2:ListNode)->ListNode:
        currentNode =headNode =  None
        carry = 0
        FLAG = True
        while l1 is not None and l2 is not None:
            sum_s = l1.val + l2.val + carry
            carry = sum_s//10
            item = sum_s%10
            new_node = ListNode(item)

            if FLAG:
                currentNode = new_node
                headNode = currentNode
                FLAG = False
            else:
                currentNode.next = new_node
                currentNode = new_node

            l1 = l1.next
            l2 = l2.next

        while l1 is not None and l2 is None:
            item = l1.val + carry
            carry = item//10
            item = item%10
            new_node = ListNode(item)
            if FLAG:
                currentNode = new_node
                headNode = currentNode
                FLAG = False
            else:
                currentNode.next = new_node
                currentNode = new_node
            l1 =l1.next

        while l2 is not None and l1 is None:
            item = l2.val + carry
            carry = item//10
            item = item%10
            new_node = ListNode(item)

            if FLAG:
                currentNode = new_node
                headNode = currentNode
                FLAG = False
            else:
                currentNode.next = new_node
                currentNode = new_node
            l2 = l2.next

        if carry!=0:
            new_node = ListNode(carry)
            currentNode.next = new_node

        return headNode

# x = ListNode(2)
# y = ListNode(4)
# z = ListNode(3)
# x.next = y
# y.next = z
#
#
#
# a = ListNode(5)
# b = ListNode(6)
# c = ListNode(4)
#
# a.next = b
# b.next = c

x= ListNode(1)
#y = ListNode(8)
#x.next = y

a = ListNode(9)
b = ListNode(9)
a.next = b

obj = Solution()
t = obj.addTwoNumbers(x,a)


