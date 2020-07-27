def longestpalindromicsubsequence(s):
    l = len(s)
    if l == 0:
        return 0
    elif l == 1:
        return 1
    else:
        temp_list= [[0 for i in range(l)] for j in range(l)]
        for i in range(l):
            temp_list[i][i] = 1
        k = 2
        while k <= l:
            for i in range(l-k+1):
                j = i+k -1
                if k == 2 and s[i] == s[j]:
                    temp_list[i][j] = 2
                elif k == 2 and s[i] != s[j]:
                    temp_list[i][j] = 1
                else:
                    if s[i] == s[j]:
                        temp_list[i][j] = temp_list[i+1][j-1] + 2
                    else:
                        temp_list[i][j] = max(temp_list[i+1][j],temp_list[i][j-1])


            k+=1
        return temp_list[0][l-1]


print (longestpalindromicsubsequence ('GEEKS FOR GEEKS'))

