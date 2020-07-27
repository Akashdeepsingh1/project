class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LL:
    def __init__(self):
        self.firstLink = None
        self.head = None

    def insert(self,val):
        node = Node(val)
        if self.head == None:
            self.firstLink = node
            self.head = node

        else:
            self.head.next = node
            self.head = self.head.next

    def print_all(self):
        temp = self.firstLink
        while temp is not None:
            print(temp.val)
            temp = temp.next

    def reserve(self):
        temp = self.firstLink
        while self.firstLink is not None:




obj = LL()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.print_all()


