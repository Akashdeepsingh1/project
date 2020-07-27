'''

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


'''

def solution(nums):

    if len(nums) == 0:
        return 0
    else:
        target = nums[0]
        final_temp = nums[0]
        index = 1
        while index <len(nums):
            temp = nums[index]
            if (temp>=0 and target>0) or (temp < 0  and temp+target >0):
                target += temp
            elif target <= 0 and temp >=0:
                target = temp
            else:
                target = 0
            if final_temp< target:
                final_temp = target
            index+=1


        return final_temp


print (solution ([-2, 1, -3, 4, -1, 2, 1, -5, 4]))