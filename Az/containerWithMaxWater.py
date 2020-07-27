def ContainerWithMostWater(arr):
    r = len(arr)-1
    l = 0
    final_sum = 0
    if r == 0 and r == 1:
        return 0
    else:
        while l<r:
            temp = (r-l) * min(arr[l],arr[r])
            if arr[l]<arr[r]:
                l+=1
            else:
                r-=1
            if final_sum< temp :
                final_sum = temp
        return final_sum


s = [1,8,6,2,5,4,8,3,7]

print (ContainerWithMostWater (s))