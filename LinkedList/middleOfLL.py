# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def middleNode(self, head: ListNode) -> ListNode:
        '''
            input: head. Type ListNode 
            return: middle Node. Type ListNode
        '''
        # base condition
        if not head or not head.next:
            return head

        # initializing variable slow and fast
        slow = head
        fast = head.next

        while slow and fast:
            slow = slow.next
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                break
        print(slow.val)
        return slow


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


obj = Solution()

obj.middleNode(n2)
