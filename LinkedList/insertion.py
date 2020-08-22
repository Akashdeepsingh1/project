
# defining the Node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Insertion at the end
# Insertion at the beginning
# Insertion after a particular element
# Insertion at a particular position

class LinkedList:
    def __init__(self):
        self.head = Node(None)

    def insertBeginning(self, val):
        # base condition
        if not val:
            return 0

        insertElement = Node(val)
        insertElement.next = self.head.next
        self.head.next = insertElement
        # return self.head.next

    def insertEnd(self, val):
        if not val:
            return 0
        insertElement = Node(val)
        prev = self.head
        curr = self.head
        while curr:
            prev = curr
            curr = curr.next
        prev.next = insertElement
        # return self.head.next

    def insertAtNthPosition(self, val, n):
        if not val:
            return 0
        insertNode = Node(val)
        curr = self.head
        prev = self.head

        while n > 0 and curr:
            prev = curr
            curr = curr.next
            n -= 1
        insertNode.next = prev.next
        prev.next = insertNode

    def insertBeforeElement(self, val, element):
        if not val:
            return 0
        insertNode = Node(val)
        curr = self.head
        prev = self.head

        while curr and curr.val != element:
            prev = curr
            curr = curr.next
        if curr and curr.val == element:
            insertNode.next = curr
            prev.next = insertNode

    def insertAfterElement(self, val, element):
        if not val:
            return 0
        insertValue = Node(val)
        curr = self.head
        while curr and curr.val != element:
            curr = curr.next
        if curr and curr.val == element:
            if curr.next != None:
                insertValue.next = curr.next
            curr.next = insertValue

    def insertInaSortedLinkedList(self, val):
        if not val:
            return 0
        insertElement = Node(val)
        if self.head.next is None:
            self.head.next = insertElement
            return
        curr = self.head.next
        FLAG = True

        while curr and curr.next:
            if curr.val <= val and curr.next.val >= val:
                insertElement.next = curr.next
                curr.next = insertElement
                FLAG = False
                break
            curr = curr.next

        if FLAG:
            if val > curr.val:
                curr.next = insertElement
            else:
                insertElement.next = self.head.next
                self.head.next = insertElement

    def display(self):
        curr = self.head.next
        while curr:
            print(
                f'The current Node is {curr.val} and the next node is {curr.next}')
            curr = curr.next


'''
# testcase to check the insert begin followed by insert end
obj = LinkedList()
obj.insertBeginning(1)
obj.display()
obj.insertEnd(2)
obj.display()
'''


'''
# testcase to check the insert end followed by insert start
obj1 = LinkedList()
obj1.insertEnd(1)
obj1.display()
obj1.insertBeginning(2)
obj1.display()
'''


obj2 = LinkedList()
#obj2.insertAtNthPosition(1, 5)
#obj2.insertAtNthPosition(1, 0)

# obj2.insertAtNthPosition(5, 5)
# obj2.insertAtNthPosition(1, 1)


# obj2.insertAtNthPosition(5, 5)
# obj2.insertAtNthPosition(1, 2)

'''
obj2.insertAtNthPosition(5, 5)
obj2.insertAtNthPosition(1, 1)
obj2.display()
obj2.insertAtNthPosition(2, 2)
obj2.display()
obj2.insertAtNthPosition(7, 1)
obj2.display()
obj2.insertAtNthPosition(10, 9)
obj2.display()
obj2.insertAtNthPosition(11, 3)
obj2.display()
obj2.display()
'''


# obj2.insertBeginning(1)
# obj2.insertEnd(3)
#obj2.insertAtNthPosition(2, 2)
#obj2.insertBeforeElement(4, 3)
#obj2.insertBeforeElement(9, 5)
#obj2.insertAfterElement(5, 4)
# obj2.insertEnd(5)
# obj2.insertInaSortedLinkedList(3)
obj2.insertInaSortedLinkedList(2)
obj2.insertInaSortedLinkedList(10)
obj2.insertInaSortedLinkedList(5)
obj2.insertInaSortedLinkedList(1)
obj2.insertInaSortedLinkedList(0)
obj2.insertInaSortedLinkedList(5)
obj2.display()
