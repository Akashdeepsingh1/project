class Node:
    def __init__ (self, val):
        self.val = val
        self.next = None


class JoinLL:
    def __init__ (self):
        pass

    def joinLL (self, l1, l2):
        '''
        @param l1: Node
        @param l2: Node
        @return : Node
        @exception - wrong input
        This functions joins the 2 list and return a single list

        '''

        if l1 is None and l2 is None:
            return None

        head = first = None

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                if head is None and first is None:
                    first = l1
                    head = l1
                else:
                    head.next = l1
                    head = head.next
                l1 = l1.next
            else:
                if head is None and first is None:
                    first = l2
                    head = l2
                else:
                    head.next = l2
                    head = head.next
                l2 = l2.next

        if l1 is not None:
            head.next = l1

        if l2 is not None:
            head.next = l2

        return first

    def print_all(self, node):
        while node is not None:
            print(node.val)
            node = node.next




a1 = Node(4)
a2 = Node(6)
a3 = Node(10)
a1.next = a2
a2.next = a3

b1 = Node(1)
b2 = Node(10)
b3 = Node(11)
b4 = Node(15)
b5 = Node(16)
b6 = Node(20)

b1.next = b2
b2.next = b3
b3.next = b4
b4.next = b5
b5.next = b6



obj = JoinLL()
t = obj.joinLL (a1, b1)
obj.print_all(t)
