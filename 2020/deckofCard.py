from heapq import heappush, heappop, nlargest


class MedianFinder:

    def __init__ (self):
        """
        initialize your data structure here.
        """
        self.median = 0
        self.count = 0
        self.maxHeapForLowerNumber = []
        self.minHeapForHigherNumber = []

    def addNum (self, num: int) -> None:
        if self.count == 0:
            self.median = num
            self.count = 1

        elif self.count % 2 == 1:
            self.count += 1
            temp = (self.median + num) / 2
            if self.median > temp:
                heappush (self.minHeapForHigherNumber, self.median)
                heappush (self.maxHeapForLowerNumber, num)

            else:
                heappush (self.maxHeapForLowerNumber, self.median)
                heappush (self.minHeapForHigherNumber, num)
            self.median = temp
        else:
            self.count += 1
            min_temp = nlargest(1,self.maxHeapForLowerNumber)
            max_temp = heappop(self.minHeapForHigherNumber)
            if  num < min_temp:
                self.median = min_temp
                heappush(self.maxHeapForLowerNumber, num)
                heappush(self.minHeapForHigherNumber, max_temp)
            elif num > max_temp:
                self.median = max_temp
                heappush(self.maxHeapForLowerNumber, min_temp)
                heappush(self.maxHeapForLowerNumber,num)
            else:
                self.median = num
                heappush(self.maxHeapForLowerNumber, min_temp)
                heappush(self.minHeapForHigherNumber,max_temp)


    def findMedian (self) -> float:
        return self.median


obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.findMedian()
obj.addNum(3)
obj.findMedian()