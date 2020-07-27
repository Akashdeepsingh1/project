def longestpalindromic(s):
    l = len(s)
    if l==0:
        return 0
    elif l ==1 :
        return 1
    else:
        list_temp = [[0 for i in range(l)] for j in range(l)]
        for i in range(l):
            list_temp[i][i] =1
            count = 1
            start = i

        # k = 2
        for i in range(l-1):
            if s[i] == s[i+1]:
                count = 2
                start = i
                list_temp[i][i+1] = 1

        k = 3
        while k<l:
            for i in range(l-k+1):
                j = i+k-1
                if s[i] == s[j] and list_temp[i+1][j-1] == 1:
                    list_temp[i][j] = 1
                    if count < k:
                        count = k
                        start = i

            k+=1

    return count, s[start:start+count]


print (longestpalindromic ('forgeeksskeegfor'))