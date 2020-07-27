'''

Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target. Return the number of pairs.

Example 1:

Input: nums = [1, 1, 2, 45, 46, 46], target = 47
Output: 2
Explanation:
1 + 46 = 47
2 + 45 = 47
Example 2:

Input: nums = [1, 1], target = 2
Output: 1
Explanation:
1 + 1 = 2
Example 3:

Input: nums = [1, 5, 1, 5], target = 6
Output: 1
Explanation:
[1, 5] and [5, 1] are considered the same.

'''


class Solution:
    def __init__(self):
        pass

    def uniqueTwoSum(self, numbers, target):
        dic = {}
        final_list = []
        for each in numbers:
            if each in dic and ((each,target-each) not in final_list and (target-each,each) not in final_list):
                final_list.append((each,target-each))
            else:
                dic[target-each] = each
        print(final_list)
        return len(final_list)

obj = Solution()
nums = [1, 1, 2, 45, 46, 46]
target = 47
print (obj.uniqueTwoSum (nums, target))


nums1 = [1, 1]
target1 = 2
print(obj.uniqueTwoSum(nums1,target1))


nums2 = [1, 5, 1, 5]
target2 = 6
print(obj.uniqueTwoSum(nums2,target2))