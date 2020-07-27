class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class Classy:
    def __init__(self):
        pass

    def reverseLinkList(self,node):
        if node is None:
            return None

        prev = None
        curr = node

        while curr is not None:
            next= curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def print_all(self,node):
        while node is not None:
            print(node.val)
            node = node.next



a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5


obj = Classy()
obj.print_all(a1)

node = obj.reverseLinkList(a1)
obj.print_all(node)