class Classy:
    def __init__(self):
        pass

    def meetingRooms(self, intervals):
        if not intervals:
            return 0

        intervals.sort(key = lambda a: a[0])
        from heapq import heappush, heappop
        h = []
        heappush(h,intervals[0][1])
        for i in intervals[1:]:
            if h[0]<i[0]:
                t = heappop(h)
                heappush(h,i[1])
            else:
                heappush(h,i[1])

        return len(h)



interval1 =  [[0, 30],[5, 10],[15, 20]]
interval2 = [[7,10],[2,4]]
interval3 = [[2,11],[6,16],[11,16]]
interval4 = [[2,15],[36,45],[9,29],[16,23],[4,9]]
interval5 = [[928,5032],[3072,3741],[3960,4588],[482,2269],[2030,4360],[150,772]]

obj = Classy()
print (obj.meetingRooms (interval1))
print(obj.meetingRooms(interval2))
print(obj.meetingRooms(interval3))
print(obj.meetingRooms(interval4))
print (obj.meetingRooms (interval5))

