import heapq


class MinStack:

    def __init__ (self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.que = []
        self.get_min = float ('inf')
        self.count = 0
        self.start = 0

    def push (self, x: int) -> None:
        self.que.append (x)
        heapq.heappush (self.min_heap, x)
        self.count += 1

    def pop (self) -> None:
        if self.count != 0:
            t = self.que.pop (self.count - 1)
            self.count -= 1
            self.min_heap.remove (t)

    def top (self) -> int:
        if self.count != 0:
            self.count -= 1
            t = self.que[self.count]
            self.min_heap.remove (t)
            return t
        return -1

    def getMin (self) -> int:
        t = heapq.heappop(self.min_heap)
        heapq.heappush (self.min_heap, t)
        return t

minStack =  MinStack()
minStack.push(-2)
minStack.push(0)
print (minStack.push (-3))
print (minStack.getMin ())
print (minStack.pop ())
print (minStack.top ())
print (minStack.getMin ())