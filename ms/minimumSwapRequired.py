def palindrome (s):
    dic = {}
    l = list(s)
    for each in l:
        if each in dic:
            dic[each] += 1
        else:
            dic[each] = 1

    FLAG = False
    for each in dic:
        if dic[each] % 2 == 0:
            continue
        else:
            if FLAG:
                return False
            FLAG = True
    return True


#minimum swap
def minimumSwap(s):
    if len(s) == 0 or not palindrome(s):
        return -1
    else:
        l = len(s)
        ls = list(s)
        swap = 0
        for i in range(l//2):
            for j in range(l-i-1,i,-1):
                FLAG = True
                if ls[i]!=ls[j]:
                    for k in range(i+1, j):
                        if ls[i] == ls[k]:
                            FLAG = False
                            temp = ls[j]
                            ls[j] = ls[k]
                            ls[k] = temp
                            swap+=1
                    if FLAG and l%2!=0:
                        temp = ls[i+1]
                        ls[i+1] = ls[l//2]
                        ls[l//2] = temp
                        i-=1
                    break

        print(''.join(ls))
        return swap


#adjacent swap

def adjacentSwap(s):
    l = len(s)
    if l == 0 or not palindrome(s):
        return -1
    elif l ==1:
        return 1
    else:
        ls = list(s)
        swaps =0
        i = 0
        while i < l//2:
            FLAG = False
            for j in range(l-i-1, i, -1):
                if ls[j] == ls[i]:
                    FLAG = True
                    for k in range(j, l-i-1):
                        temp = ls[k]
                        ls[k] = ls[k+1]
                        ls[k+1] = temp
                        swaps+=1
                    break
            if not FLAG and l%2!=0:
                for k in range(i,l//2):
                    temp = ls[k]
                    ls[k] = ls[k + 1]
                    ls[k + 1] = temp
                    swaps += 1
                i-=1
            i+=1
        return swaps


print(adjacentSwap('mmada'))
print(minimumSwap('aabb'))
print(minimumSwap('mamad'))
