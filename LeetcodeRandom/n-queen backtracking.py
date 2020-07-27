def getPermutation ( n: int, k: int) -> str:
    fl = []
    a = [str(i) for i in range (1,n+1)]
    permute (a, 0, n - 1, fl)
    print((fl[k-1]))


def permute (a, l, r, fl):
    if l == r:
        fl.append (int(''.join (a)))
    else:
        for i in range (l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute (a, l + 1, r,fl)
            a[l], a[i] = a[i], a[l]



getPermutation(3,3)