class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Classy:
    def addTwoNumbers(self,l1,l2):
        head = -1
        carry = 0
        while l1 is not None and l2 is not None:
            temp = l1.val + l2.val + carry
            if temp>9:
                carry = 1
                temp = temp%10
            else:
                carry = 0
            curr = ListNode(temp)
            if head != -1:
                curr.next = head
            head = curr

            l1 = l1.next
            l2 = l2.next

        while l1 is not None and l2 is None:
            temp = l1.val + carry
            if temp>9:
                carry = 1
                temp = temp%10
            else:
                carry = 0
            curr = ListNode(temp)
            if head != -1:
                curr.next = head
            head = curr
            l1 = l1.next

        while l1 is None and l2 is not None:
            temp = l2.val + carry
            if temp>9:
                carry = 1
                temp = temp%10
            else:
                carry = 0
            curr = ListNode(temp)
            if head != -1:
                curr.next = head
            head = curr
            l2 = l2.next

        return head


    def print_all(self, node):
        while node is not None:
            print(node.val)
            node = node.next


a2 = ListNode(2)
a4 = ListNode(4)
a3 = ListNode(3)

a2.next = a4
a4.next = a3


b5 = ListNode(5)
b6 = ListNode(6)
b4 = ListNode(4)

b5.next = b6
b6.next = b4

obj = Classy()
t= obj.addTwoNumbers (a2, b5)
obj.print_all(t)
