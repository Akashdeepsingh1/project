def findDuplicate ( nums) -> int:
    '''
    @param nums list
    @return int which is duplicate
    exception: if the element is empty


    '''


    if not nums:
        return 0
    temp_sum = 0
    running_sum = 0
    for i in range (len (nums)):
        running_sum += (i+1)
        temp_sum += nums[i]
    return running_sum - temp_sum

num1 = [2,2,2,2,2]
num2 = [1,3,4,2,2]
num3 = [3,1,3,4,2]
print (findDuplicate (num1))
print (findDuplicate (num2))
print (findDuplicate (num3))


def findDuplicate1 ( nums) -> int:
    t, h = nums[0], nums[nums[0]]
    while t != h: t, h = nums[t], nums[nums[h]]
    t = -1
    while t != h: t, h = nums[t], nums[h]
    return t


print (findDuplicate1 (num1))
print (findDuplicate1 (num2))
print (findDuplicate1 (num3))

