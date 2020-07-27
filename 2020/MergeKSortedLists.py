
class Node:
    def __init__(self, val ):
        self.val = val
        self.next = None

    def __lt__(self, other):
        '''

        :param other:
        :return:
        '''

class Classy:
    def __init__(self):
        pass

    def mergeKList(self, lst):
        import heapq
        h = heapq
        for ls in lst:
            for each in ls:
                temp = Node(each.val)
                heapq.heappush(h,(each.val,temp))

        head = Node(-1)
        curr = head
        while h:
            temp = heapq.heappop(h)
            curr.next = temp
            curr = temp

        return head.next




