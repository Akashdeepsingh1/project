def kthSmallestDistance(nums, k):
    if not nums or not k:
        return None

    def checkNumber(middle):
        if not middle:
            return
        count = 0
        for i in range(len(nums)):
            temp = 0
            for j in range(len(nums)):
                if middle < abs(nums[i]-nums[j]):
                    break
                temp = j
        return count >= k

    nums.sort()
    l = nums[0]
    r = nums[-1]

    while l < r:
        mid = l + (r-l)//2
        if checkNumber(mid):
            r = mid
        else:
            l = mid+1
    return l


nums = [1, 3, 1]
k = 1
print(kthSmallestDistance(nums, k))
