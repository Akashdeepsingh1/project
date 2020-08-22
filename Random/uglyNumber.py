def uglyNumber(num):
    if not num:
        return 0
    if num < 4:
        return num
    #num = 1
    nums = [1]
    num2 = 0
    num3 = 0
    num5 = 0
    for i in range(num-1):
        choice = (nums[num2]*2, nums[num3]*3, nums[num5]*5)
        num = min(choice)
        nums.append(num)
        if nums[num2] * 2 == num:
            num2 += 1
        if nums[num3] * 3 == num:
            num3 += 1
        if nums[num5] * 5 == num:
            num5 += 1
    return num


print(uglyNumber(10))
