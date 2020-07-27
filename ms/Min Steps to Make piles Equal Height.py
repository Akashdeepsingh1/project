def solution(n):
    l = len(n)
    if l <= 1:
        return 0
    n.sort()
    count = 0
    dnums = 0
    for i in range(1,l):
        if n[i]== n[i-1]:
            count += dnums
        else:
            dnums+=1
            count += dnums
    return count


print (solution ([4,5,5, 4,2]))