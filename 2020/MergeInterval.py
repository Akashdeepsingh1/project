class Classy:
    def __init__(self):
        pass

    def mergeIntervals(self, intervals):
        '''

        :param intervals: [[1,3],[2,6],[8,10],[15,18]
        :return: [[1,6],[8,10],[15,18]]
        '''

        intervals.sort(key = lambda x:x[1])
        if not intervals:
            return []
        l = []
        import heapq
        heapq.heappush(l,intervals[-1])

        for each in range(len(intervals)-2,-1,-1):
            temp = heapq.heappop(l)
            # if pop element start is smaller than last element of traverse
            if temp[0]<=intervals[each][1]:
                heapq.heappush(l,[min(temp[0],intervals[each][0]),max(temp[1],intervals[each][1])])
            else:
                heapq.heappush(l,temp)
                heapq.heappush(l,intervals[each])


        return l



l = [[1,3],[2,6],[8,10],[15,18]]
l1 = [[1,4],[5,6]]
l2 = [[1,4],[0,4]]
l3 = [[1,4],[0,0]]
l4 = [[1,4],[2,3]]
l5 = [[2,3],[4,5],[6,7],[8,9],[1,10]]
obj = Classy()


print (obj.mergeIntervals (l))
print (obj.mergeIntervals (l1))
print (obj.mergeIntervals (l2))
print (obj.mergeIntervals (l3))
print (obj.mergeIntervals (l4))
print (obj.mergeIntervals (l5))





