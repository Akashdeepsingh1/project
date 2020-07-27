def sqrt(num, l, r):
    if l>r:
        return r
    if l*l == num:
        return l
    if r*r == num:
        return r
    mid = (l+r)//2
    temp = mid * mid
    if temp == num:
        return mid
    if temp>num:
        return sqrt(num,l,mid-1)
    else:
        return sqrt(num,mid+1,r)

num = 49
print (sqrt (num, 2, num // 2))