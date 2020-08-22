def maxWater(nums):
    '''
    [0,1,0,2,1,0,1,3,2,1,2,1]
    '''
    l = 0
    r = len(nums) - 1
    count = 0
    l_min = nums[0]
    r_min = nums[-1]
    # [0,1,0,2,1,0,1,3,2,1,2,1]
    while l < r:
        if nums[l] < nums[r]:
            temp = min(l_min, r_min) - nums[l]
            l += 1
            c = nums[l]
            if l_min < c:
                l_min = nums[l]
        else:
            temp = min(l_min, r_min) - nums[r]
            r -= 1
            if r_min < nums[r]:
                r_min = nums[r]
        if temp > 0:
            count += temp
    return count


'''
l = 0, r = 11, count = 1
'''

nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(maxWater(nums))
