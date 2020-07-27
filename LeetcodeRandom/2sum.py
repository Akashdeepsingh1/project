def sumtwo(nums, target):
    dic = {}

    for i in range(0, len(nums)):
        temp = target - nums[i]
        if temp in dic:
            return [dic[temp],i]
        else:
            dic[temp] = i

    return None
