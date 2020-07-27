# def longestpalindrome(s):
#     s_new = s
#     s_new = '$'.join(s_new[i:i+1] for i in range(0,len(s),1))
#
#     i = j = 0
#     ls = []
#     s_new_temp = []
#     k = 0
#     max_new = 0
#     max_count = 0
#     while k < len(s_new):
#         t = 1
#
#         count = 1
#         while k-t >= 0 and k+t < len(s_new):
#             if s_new[k-t] == s_new[k+t]:
#                 count+=2
#             t+=1
#
#
#         s_new_temp.append(count)
#         if count>max_count:
#             max_count = count
#             max_new = k
#             ls = s_new[k-max_count:k+max_new+1]
#
#
#         k+=1
#     # tf = max_count//2
#     # return s_new[max_new-tf:max_new+tf]
#     return ls
#
#
#
#
# print(longestpalindrome('cbbd'))



def longestpalindromic(str1):
    l = len(str1)

    if l ==0:
        return 0
    elif l == 1:
        return 1
    else:
        temp_list = [[0 for i in range(l)] for j in range(l)]

        start = 0
        count = 0
        for i in range(l):
            temp_list[i][i] = 1

        for i in range(l-1):
            if str1[i] == str1[i+1]:
                temp_list[i][i+1] = 1
                count = 2
                start = i

        k = 3
        while k<l:
            for j in range(l-k+1):
                end = j+k-1
                if str1[j] == str1[end] and temp_list[j+1][end-1] == 1:
                    temp_list[j][end] = 1
                    if k > count:
                        count = k
                        start = j
            k+=1





        return count, start

print(longestpalindromic('forgeeksskeegfor'))


















