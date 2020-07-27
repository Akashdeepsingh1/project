class LinkedList:
    def __init__(self, node):
        self.val = node
        self.next = None

a = LinkedList('a')
b = LinkedList('b')
c = LinkedList('c')
d = LinkedList('d')
e = LinkedList('e')
f = LinkedList('f')
a.next = b
b.next = c
c.next = d
d.next = e
#e.next = f

def reverse(head, k):

    current = head
    FLAG = True
    while current is not None:
        temp = k
        start = current
        prev = None
        while temp>0 and current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
            temp-=1

        if FLAG:
            FLAG = False
            head = prev
            linker = start
        else:
            if (start is not None)  and  (temp  in [0,1] and k != 2):
                linker.next = prev
            else:
                linker.next = start
                #linker.next = prev
            linker = start
    return head

def print_all(head):
    while head is not None:
        print(head.val)
        head = head.next





t = reverse(a, 2)
print_all(t)
