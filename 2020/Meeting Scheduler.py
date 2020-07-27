
class Classy:
    def __init__(self):
        pass

    def minAvailableDuration(self,slots1,slots2,duration):
        '''

        :param self:
        :param slots1:
        :param slots2:
        :param duration:
        :return:


        Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
        Output: [60,68]


        Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
        Output: []

        It is guaranteed that no two availability slots of the same person intersect with each other.
        That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.
        '''



        '''
        [[10,50],[60,120],[140,210]]
        [[0,15],[60,70]]
        duration = 8
        
        first check the end time of both the elements and 
        which ever end time is less - use that to substract with which ever start time is greater
        if the desired duration is not found then move to the next element whichever has a smaller end time 
        '''

        slots1.sort (key=lambda a: a[1])
        slots2.sort (key=lambda a: a[1])

        l1 = len(slots1)
        l2 = len(slots2)

        index1 = 0
        index2 = 0
        while index1<l1 and index2<l2:
            item11,iteml2 = slots1[index1]
            item21,item22 = slots2[index2]
            if iteml2>= item22:
                tempStartTime = max(item11,item21)
                if  duration<=(item22 - tempStartTime):
                    return [tempStartTime,tempStartTime+duration]
                else:
                    index2+=1
            else:
                tempStartTime = max(item11,item21)
                if duration <=(iteml2 - tempStartTime):
                    return [tempStartTime,tempStartTime+duration]
                else:
                    index1+=1
        return []


slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 12



obj = Classy()
print (obj.minAvailableDuration (slots1, slots2, duration))
