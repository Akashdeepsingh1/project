def sum3(nums):



    nums = nums.sort()

    r = len(nums)-1
    l = 0
    ls = []
    while l<r:
        temp_num = nums[l] + nums[r]
        tl = (l+r)//2
        while l < tl < r:
            if nums[tl] == -temp_num:
                ls.append([nums[l],nums[r],nums[tl]])
                break
            elif nums[tl] + temp_num < 0:
                tl+=1
            else:
                tl-=1


        while nums[l] == nums[l+1] and l<r:
            l+=1
        while nums[r] == nums[r-1] and l<r:
            r-=1

        if abs(nums[l]) > abs(nums[r]):
            l+=1
        else:
            r-=1
    return ls


print (sum3 ([-4, -1, -1, 0, 1, 2]))
