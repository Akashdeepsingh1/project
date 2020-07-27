'''

Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Example 1:

Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]
Example 2:


Input: s = "abacab", k = 3
Output: ["bac", "cab"]
Example 3:

Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
Explanation:
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl"
"wagl" is repeated twice, but is included in the output once.


'''
def solution(s,k):
    len_s =len(s)
    if len_s<k:
        return []
    else:
        final_list = []
        for i in range(len_s-k+1):
            temp_s = s[i:i+k]
            temp_dic = {}
            flag = True
            for j in range(k):
                if temp_s[j] in temp_dic:
                    flag = False
                else:
                    temp_dic[temp_s[j]] = 1
            if flag and temp_s not in final_list:
                final_list.append(temp_s[:])

        return final_list


def solution2(s,k):
    len_s  = len(s)
    if len_s<k:
        return []
    else:
        from collections import deque

        sliding_window = deque()
        count_dict = {}
        for i in range(len_s):
            temp_s = s[i]
            if temp_s in sliding_window:
                count_dict[temp_s] +=1
                sliding_window.append (count_dict[temp_s])
            else:
                sliding_window.append(1)
                count_dict[temp_s] = 1

            #if len()
        #for i in range(k,len_s-k+1):




s = "awaglknagawunagwkwagl"
k = 4

print (solution (s, k))