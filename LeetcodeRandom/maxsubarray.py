def maxSubArray(nums):
    l = len (nums)
    max_so_far = 0
    final_max = a[0]
    for i in range (l):
        max_so_far += nums[i]
        final_max = max(final_max,max_so_far)
        if max_so_far < 0:
            max_so_far = 0
    return final_max

a= [-1,0]
print (maxSubArray (a))
