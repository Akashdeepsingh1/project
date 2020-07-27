class Classy:
    def __init__(self):
        pass

    def meetingRoom(self, intervals):
        '''
        :param intervals:
        :return:

        Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

        Example 1:

        Input: [[0, 30],[5, 10],[15, 20]]
        Output: 2
        Example 2:

        Input: [[7,10],[2,4]]
        Output: 1

        '''

        if not intervals:
            return 0

        import heapq

        intervals.sort(key = lambda x:x[0])
        rooms = []
        heapq.heappush(rooms,intervals[0][1])

        for i in range(1,len(intervals)):
            st, end = intervals[i]
            temp = heapq.heappop(rooms)
            if temp <= st:
                heapq.heappush(rooms,end)
            else:
                heapq.heappush(rooms,end)
                heapq.heappush(rooms,temp)

        return rooms

obj = Classy()
Input = [[0, 30],[5, 10],[15, 20]]
print (obj.meetingRoom (Input))

input1 = [[7,10],[2,4]]
print(obj.meetingRoom(input1))


input2 = [[2,11],[6,16],[11,16]]
print(obj.meetingRoom(input2))


input3 = [[2,15],[36,45],[9,29],[16,23],[4,9]]
print(obj.meetingRoom(input3))


input4 = [[928,5032],[3072,3741],[3960,4588],[482,2269],[2030,4360],[150,772]]
print(obj.meetingRoom(input4))