class Node:
    def __init__ (self, val):
        self.val = val
        self.next = None


class LL:
    def __init__ (self):
        self.head = None
        self.currentNode = None

    def reverseKGroup (self, node, k):
        '''
        @param node: link node - this is the head of the node
        @param k : in group it needs to be reversed
        @return node: after the linked list has been reverse in group of k
        @exception: node not found or trying to access nullpinter

        '''
        matcher = None
        while node:
            i = 1
            self.currentNode = Node (node.val)
            node = node.next
            start = self.currentNode
            while i < k and node is not None:
                temp = Node (node.val)
                temp.next = self.currentNode
                self.currentNode = temp
                i += 1
                node = node.next
        
            if self.head is None:
                self.head = self.currentNode
            else:
                matcher.next = self.currentNode

            matcher = start



    def printAll(self, node):
        while node is not None:
            print(node.val)
            node = node.next






a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a6 = Node(6)
a1.next= a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a6

obj = LL()
obj.reverseKGroup (a1, 1)
obj.printAll(obj.head)