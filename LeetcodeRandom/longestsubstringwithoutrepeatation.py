def lengthOfLongestSubstring (s):
    """
    :type s: str
    :rtype: int
    """
    i = 0
    dic = {}
    st = list(s)
    sum_s = 0
    l = len (st)
    final_sum = 0
    if l <= 1:
        return l
    initial_temp = final_temp = 0

    while i < l:
        char_temp = st[i]

        if char_temp in dic.keys () :
            initial_temp = dic[char_temp]
            final_temp = i
            temp = final_temp- initial_temp
            for each, val in enumerate(dic):
                if each < initial_temp:
                    del dic[val]

            if final_sum < temp:
                final_sum = temp

            dic[st[i]] = i

        else:
            dic[st[i]] = i
            final_temp = i

        i += 1


    if final_sum <= temp:
        final_sum = final_temp - initial_temp

    return final_sum

print(lengthOfLongestSubstring('abba'))