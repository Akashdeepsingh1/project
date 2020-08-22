class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def __init__(self):
        self.head = Node(None)

    def insertBeginning(self, val):
        # base condition

        insertElement = Node(val)
        insertElement.next = self.head.next
        self.head.next = insertElement

    def getDecimalVal(self):
        head = self.head.next
        if not head:
            return 0
        num = 0
        while head:
            num = num*10 + head.val
            head = head.next

        decimalNum = 0
        count = 0
        while num:
            mod = num % 10
            if mod:
                decimalNum += (2**count)
            count += 1
            num //= 10
        return decimalNum


obj = Solution()
# obj.insertBeginning(1)
obj.insertBeginning(1)
# obj.insertBeginning(1)
print(obj.getDecimalVal())
