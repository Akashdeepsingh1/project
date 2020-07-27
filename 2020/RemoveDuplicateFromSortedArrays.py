'''

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.


'''

def solution(nums):
    if len(nums)== 0:
        return []
    else:
        index = 1
        for i in range(len(nums)):
            print(nums[i])
            print(nums[i-index])
            if nums[i] == nums[i-index]:
                index +=1
            temp = nums[i]
            nums[i] = nums[i+index]
            nums[i+index] = temp
        return index

num = [0,0,1,1,1,2,2,3,3,4],
print(num.__class__)
print (solution (num))