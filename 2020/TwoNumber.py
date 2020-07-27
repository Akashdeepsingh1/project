def solution(nums, target):
    target -=30 
    dic = {}
    final_item = []
    for i in range(len(nums)):
        if target - nums[i] in dic:
            if dic[target-nums[i]] != nums[i]:
                if final_item:
                    if (final_item[0]< nums[i] and final_item[1]<nums[i]) or (final_item[0]) < target-nums[i] and final_item[1]< (target-nums[i]):
                        final_item = [nums[i],target-nums[i]]
                else:
                    final_item = [nums[i], target-nums[i]]
                dic[nums[i]] = i
        else:
            dic[nums[i]] = i
    return [dic[final_item[0]],dic[final_item[1]]]


nums = [20, 50, 40, 25, 30, 10]
print (solution (nums, 90))

