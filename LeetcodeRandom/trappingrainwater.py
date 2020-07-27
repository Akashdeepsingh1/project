def trap(height):
    l , r, res = 0, len(height)-1, 0
    while(l<r):
        mn = min(height[l],height[r])
        if mn == height[l]:
            l+=1
            while l< r and mn > height[l]:
                res += mn - height[l]
                l += 1

        else:
            r -= 1
            while l<r and mn > height[r]:
                res += mn - height[r]
                r -= 1
    return res


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))