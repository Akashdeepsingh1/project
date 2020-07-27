class Classy:
    def __init__(self):
        pass

    def maxSubarry(self, nums, k):
        if not nums:
            return 0

        count = 0
        for st in range(len(nums)):
            current_sum = 0
            for end in range(st,len(nums)):
                current_sum +=nums[end]
                if current_sum == k:
                    count+=1
        return count

nums = [1,1,1]
nums1 = [-1,-1,1]
target1 = 0
target = -1
nums2 = [28,54,7,-70,22,65,-6]
target2 = 100



obj = Classy()
print (obj.maxSubarry (nums2, target2))