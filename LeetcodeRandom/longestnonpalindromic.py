def longestnonpalindromicsubsequence(s):
    l = len(s)
    if l == 0:
        return 0
    elif l == 1:
        return 0
    else:
        temp_list = [[0 for i in range(l)]for j in range(l)]
        k = 2
        while k <= l:
            for i in range(l-k+1):
                j = i + k-1
                if k ==2:
                    if s[i] != s[j]:
                        temp_list[i][j] = 1
                elif s[i]!=s[j]:
                    temp_list[i][j] = max(temp_list[i+1][j], temp_list[i][j-1])+2
                else:
                    temp_list[i][j] = max(temp_list[i+1][j], temp_list[i][j-1])
            k+=1


        return temp_list


print (longestnonpalindromicsubsequence ('acbbca'))
