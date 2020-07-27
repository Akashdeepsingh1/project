def getPermutation (n: int, k: int) -> str:

    a = [str (i) for i in range (1, n+1)]
    l = 0
    r = n


    def permute (a, l, r):
        if l == r:
            temp = a
            f1.append(temp)
            #fl.append (int (''.join (a)))
            print(''.join(a))
        else:
            for i in range (l, r + 1):
                a[l], a[i] = a[i], a[l]
                permute (a, l + 1, r)
                a[l], a[i] = a[i], a[l]
    f1 = []
    permute(a,l,r-1)
    return (fl[k])


print(getPermutation(3,5))
