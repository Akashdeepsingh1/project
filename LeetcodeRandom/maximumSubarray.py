def maxSubArray ( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    temp_sum = final_sum = 0
    l = 0
    r = len(nums)

    while l<r:
        temp_sum += nums[l]
        if temp_sum>final_sum:
            final_sum = temp_sum
            print(nums[])
        if temp_sum <0:
            temp_sum = 0
        l+=1


    return final_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))