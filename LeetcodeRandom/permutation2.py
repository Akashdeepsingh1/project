def permuteUnique ( nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    final_list = []
    def permute(nums, index):
        if index == len(nums)-1:
            if nums not in final_list:
                #print(''.join(nums[:]))
                final_list.append(nums[:])
        for i in range(index,len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            permute(nums, index+1)
            nums[i], nums[index] = nums[index], nums[i]

    permute(nums,0)
    return final_list
nums = [1,1,2]
print (permuteUnique (nums))
