'''
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
'''


def solution(s):
    if len(s) == 0:
        return []
    else:
        i = 0
        final_list = [0] * len(s)
        temp_dic = {}
        for i in range(len(s)):
            temp_dic[s[i]] = i
        count = 0
        for i in range(len(s)):
            final_list[i] = temp_dic[s[i]]
        i = 0
        temp_list = []
        flag = True
        while i < len(s):
            j = final_list[i]
            count +=1
            k = i
            while k<j:
                if final_list[k]>j:
                    j = final_list[k]
                k+=1

            temp_list.append(k+1 - i)
            i = k + 1
        print(count)
        print(temp_list)

S = "ababcbacadefegdehijhklij"

print (solution (S))