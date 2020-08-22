# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairsRecursive(self, head: ListNode) -> ListNode:
        if not head:
            return None
        first = head
        second = head.next
        if first and not second:
            return first

        if second:
            first.next = self.swapPairsRecursive(second.next)
            second.next = first
        return second

    def swapPairsIterative(self, head):
        if not head:
            return None

        prev = None
        curr = head

    def print_all(self, head):
        while head:
            print(head.val)
            head = head.next


a = ListNode('a')
b = ListNode('b')
c = ListNode('c')
d = ListNode('d')
e = ListNode('e')
f = ListNode('f')
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

obj = Solution()
head = obj.swapPairsRecursive(e)
obj.print_all(head)
