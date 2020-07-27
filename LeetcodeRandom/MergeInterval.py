def merge(intervals) :
    l=len(intervals)
    if len(intervals) <= 1:
        return intervals

    intervals = sorted(intervals,key = lambda i:i[0])

    i = 1
    temp = [intervals[0]]
    index = 0
    while i < l:
        check_temp = intervals[i]
        if temp[index][1] >= check_temp[0]:
            if temp[index][1] < check_temp[1]:
                temp[index][1] = check_temp[1]
            if temp[index][0] > check_temp[0]:
                temp[index][0] = check_temp[0]
        elif temp[index][1] > check_temp[1]:
            if temp[index][0] > check_temp[0]:
                temp[index][0] = check_temp[0]

        else:
            index += 1
            temp.append (check_temp)
        i += 1
    return temp


intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals1 = [[1,4],[4,5]]
intervals2 = [[1,4],[0,1]]
intervals3 = [[1,4],[2,3]]
print (merge (intervals))
