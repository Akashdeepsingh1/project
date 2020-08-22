def nSmallest(matrix, k):
    from heapq import heappop, heappush, heapify
    count = k
    data = matrix

    new_list = []
    trackingList = []

    for i in range(len(data)):
        if len(data[i]) > 0:
            heappush(trackingList, (data[i][0], i, 0))

    while len(new_list) < count:
        temp, ls, pos = heappop(trackingList)
        new_list.append(temp)
        if len(data[ls]) > pos+1:
            heappush(trackingList, (data[ls][pos+1], ls, pos+1))

    return new_list


ls = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
#ls = [[4, 9, 13, 25], [1, 3, 19, 36], [2, 5, 12, 45], [0, 1], []]
#K = 6

print(nSmallest(ls, k))
