from heapq import heappush, heappop

class Classy:
    def __init__(self):
        pass

    def meetingSchedule(self,slot1,slot2,duration):
        '''
        :param intervals:
        :return:

        Example 1:
        Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
        Output: [60,68]
        Example 2:

        Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
        Output: []

        '''

        slot1.sort(key = lambda x:x[0])
        slot2.sort(key = lambda x:x[0])

        i,j = 0,0

        while i<len(slot1) and j<len(slot2):
            i_start,i_end = slot1[i]
            j_start,j_end = slot2[j]

            if i_start>j_end:
                j+=1
            elif j_start > i_end:
                i+=1
            else:
                t =  min(j_end,i_end) - max(i_start,j_start)
                if t>= duration:
                    return [max(i_start,j_start), min(j_end,i_end)]

                if j_end - j_start >i_end-i_start:
                    i+=1
                else:
                    j+=1


    def meetingSchedule2(self, slot1,slot2,duration):
        if not slot1 or not slot2 or not duration:
            return 0
        count = []
        i = j = 0
        temp1 = []
        temp2 = []
        for i in range(1,len(slots1)):
            temp1.append([slots1[i-1][1],slots1[i][0]])
        for j in range(1,len(slots2)):
            temp2.append([slots2[j-1][1],slots2[j][0]])

        i = j = 0

        while i <len(temp1)and j<len(temp2):
            i_start,i_end = temp1[i]
            j_start,j_end = temp2[j]

            if i_start>j_end:
                j+=1
            elif j_start>i_end:
                i+=1
            else:
                duration1 =min(i_end,j_end) -  max(i_start,j_start)
                if duration1>=duration:
                    count.append([max(i_start,j_start),min(i_end,j_end)])
                if i_end < j_end:
                    i+=1
                else:
                    j+=1
        return count










slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 8

obj = Classy()
#print (obj.meetingSchedule (slots1, slots2, duration))

#print (print (obj.meetingSchedule (slots1, slots2, 12)))
print (obj.meetingSchedule2 (slots1, slots2, 10))

