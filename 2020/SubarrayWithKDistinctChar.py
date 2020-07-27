def maxSubarray(nums, k):
    '''

    :param nums: [1,2,1,2,3]
    :param k: 2
    :return: 7
    Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
    '''
    from collections import defaultdict
    count = 0
    final_list = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)+1):
            temp = nums[i:j]
            dict = set()
            for each in temp:
                dict.add(each)
            if len(dict) == k:
                count+=1
                final_list.append(temp)
    return count,final_list

nums = [1,2,1,2,3]
k= 2

print (maxSubarray (nums, k))