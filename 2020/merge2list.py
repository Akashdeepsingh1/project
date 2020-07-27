class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



def mergeTwoLists (l1, l2):
    if l1 is None and l2 is None:
        return None
    elif l1 is None and l2 is not None:
        return l1
    elif l1 is not None and l2 is None:
        return l2
    else:
        head = ListNode (-1)
        curr = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                newnode = ListNode (l1.val)
                curr.next = newnode
                l1 = l1.next
            else:
                newnode = ListNode (l2.val)
                curr.next = newnode
                l2 = l2.next
            curr = curr.next
        if l1 is None and l2 is not None:
            curr.next = l2
        elif l1 is not None and l2 is None:
            curr.next = l1
        return head.next


l11 = ListNode(1)
l12 = ListNode(2)
l14 = ListNode(4)
l11.next = l12
l12.next = l14

l21 = ListNode(1)
l23 = ListNode(3)
l24 = ListNode(4)
l21.next = l23
l23.next = l24

print (mergeTwoLists (l11, l21))


