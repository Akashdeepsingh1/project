'''
Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.

!?',;.
'''

def mostCommonWords(paragraph, banned):
    from collections import defaultdict
    import re
    st = re.sub (r'''[,!|:?.'; ]+''', " ", paragraph).lower()
    para_list = st.split (' ')
    print (para_list)
    temp_dic = defaultdict (int)
    max_val = 0
    max_word = ""

    if len (para_list) == 0:
        return ""
    for each in para_list:
        if each in banned:
            continue
        elif each in temp_dic:
            temp_dic[each] += 1
            if temp_dic[each] > max_val:
                max_val = temp_dic[each]
                max_word = each

        else:
            temp_dic[each] = 1
            if max_val == 0:
                max_val = 1
                max_word = each

    for k, v in temp_dic.items ():
        print ('{}  {}'.format (k, v))
    return max_word

    #print(new_para)


para = "a, a, a, a, b,b,b,c, c"
banned2 = ["a"]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print (mostCommonWords (paragraph, banned))







