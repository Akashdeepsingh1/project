from heapq import heappush, heappop, heapify
import heapq

class Classy:
    def __init__(self,n):
        self.count = n
        self.l = []
        self.heap = []
        self.currentCount = 0

    def insert(self,num) -> None:
        if self.currentCount < self.count:
            self.l.append(num)
            heappush(self.heap,-1 * num)
            self.currentCount +=1
        else:
            t=self.l.pop(0)
            self.heap.remove(t*-1)
            heapify(self.heap)
            self.l.append(num)
            heappush(self.heap,-1*num)

    def getMax(self) -> int:

        if self.currentCount == 0:
            return 0
        else:
            t = heappop(self.heap)
            heappush(self.heap, t)
            t *= -1
            return t

