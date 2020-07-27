def rob(nums):
    l = len(nums)
    if l==0:
        return 0
    elif l == 1:
        return l[0]
    else:
        i = 0
        odd_sum = even_sum = 0
        while i < l:
            if i%2==0:
                even_sum += nums[i]
            else:
                odd_sum += nums[i]

            i+=1
        if even_sum > odd_sum:
            return even_sum
        else:
            return odd_sum


print(rob([2,7,9,3,1]))