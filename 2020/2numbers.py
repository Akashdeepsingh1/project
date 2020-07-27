# assumption - numbers are not duplicate and non negative.

def twoSum (nums, target):
    dic = {}
    for i in range (len (nums)):
        if (target - nums[i]) in dic:
            return [dic[target-nums[i]], i]
        else:
            dic[nums[i]] = i
    return None


print(twoSum([2,7,11,15],9))