def lengthOfLongestSubstring (s):
    """
    :type s: str
    :rtype: int
    """
    st = 0
    le = 0
    st_final = 0
    len_final = 0
    dic = {}
    FLAG = True
    temp_len = 0
    if len (s) == 1:
        len_final = 1
    for i in range (0, len (s)):
        temp_len += 1
        if s[i] in dic.keys ():
            le = i - dic[s[i]]
            temp = st
            st = dic[s[i]] + 1
            FLAG = False
            temp_len = 1

        if len_final < le:
            len_final = le
            st_final = temp

        dic[s[i]] = i
    if FLAG:
        len_final = len (s)
    elif len_final < le:
        len_final = le
    elif len_final < temp_len:
        len_final = temp_len

    return len_final, st_final

print(lengthOfLongestSubstring('GEEKSFORGEEKS'))