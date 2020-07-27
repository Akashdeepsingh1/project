def minWindows(s,t):
    t_dic = {}
    s_list = list(s)
    l = 0
    r = 0
    min_val = len(s)

    for each in t:
        if each in t_dic:
            t_dic[each] +=1
        else:
            t_dic[each] = 1
    temp = {}

    while (l+len(t))<=len(s_list)and r<len(s_list):
        FLAG_R = True
        show_val = s_list[r]
        FLAG= True
        if s_list[r] in t_dic:
            if s_list[r] in temp:
                temp[s_list[r]] += 1
            else:
                temp[s_list[r]] = 1

        while r-l+1>= len(t) and FLAG:
            FLAG = True
            for each in t_dic:
                if each in temp and temp[each]>=t_dic[each]:
                   continue
                else:
                    FLAG = False
                    break
            if FLAG:
                if r-l <= min_val:
                    if s_list[l] in temp:
                        temp[s_list[l]] -= 1
                    r_final = r
                    l_final = l
                    min_val = r-l
                l+=1
            else:
                r+=1
                FLAG_R = False
        if FLAG_R:
            r+=1

    return s[l_final:r_final+1]
s = "ab"
t = "b"

print (minWindows (s, t))