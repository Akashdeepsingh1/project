def maxSubarray(arr):
    '''

    :param arr:
    :return:
    [-2,1,-3,4,-1,2,1,-5,4],

    '''

    if not arr:
        return 0
    temp_sum = arr[0]
    final_sum = arr[0]
    #[-2, 1, -3, 4, -1, 2, 1, -5, 4]

    for i in range (1, len (arr)):
        temp_sum = max (arr[i], temp_sum + arr[i])
        final_sum = max (final_sum, temp_sum)

    return final_sum



arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print (maxSubarray (arr))