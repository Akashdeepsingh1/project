
def _helper2(sortedList, num, position):
    count = 1
    while ((position-count) > 0 and sortedList[position-count] == num) or ((position+count) < len(sortedList)-1 and sortedList[position+count] == num):
        if ((position-count) > 0 and sortedList[position-count] == num) and ((position+count) < len(sortedList)-1 and sortedList[position+count] == num):
            count += 2
        elif ((position-count) > 0 and sortedList[position-count] == num) or ((position+count) < len(sortedList)-1 and sortedList[position+count] == num):
            count += 1
        else:
            return count
    return count


def _helper(sortedList, num, start, end):
    if sortedList[start] == num:
        return _helper2(sortedList, num, start)
    elif sortedList[end] == num:
        return _helper2(sortedList, num, end)
    else:
        mid = (start+end)//2
        if sortedList[mid] >= num:
            return _helper(sortedList, num, start, mid-1)
        else:
            return _helper(sortedList, num, mid+1, end)


def countOccurence(sortedList, num):
    if not sortedList or not num:
        return 0
    return _helper(sortedList, num, 0, len(sortedList)-1)


arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42]
target = 8

print(countOccurence(arr, target))
