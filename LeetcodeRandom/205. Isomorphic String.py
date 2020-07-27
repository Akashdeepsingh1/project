def isIsomorphic(s,t):
    s_len = len(s)
    t_len = len(t)

    if s_len != t_len:
        return False
    dic = {}

    for i in range(s_len):
        if s[i] in dic:
            if dic[s[i]] != t[i]:
                return False
        else:
            dic[s[i]] = t[i]

    return True


print (isIsomorphic ('foo', 'bar'))
