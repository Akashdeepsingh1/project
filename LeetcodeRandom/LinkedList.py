class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class Linkedlist:

    def __int__(self):
        self.firstNode =  None


    def insert(self,data):
        head = Node(data)
        if self.firstNode is None:
            self.firstNode = head
        head = head.next

    def print_all(self):
        first = self.firstNode
        while first.next is not None:
            print(first.data)
            first = first.next

obj = Linkedlist()
obj.insert(10)
obj.insert(20)
obj.insert(30)

obj.print_all()



