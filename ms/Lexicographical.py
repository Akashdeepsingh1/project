def solution(s):
    final_list = []
    l = len(s)
    if l <=1:
        return 1
    FLAG = False
    if s[0]>s[1]:
        return s[1:]
    else:
        i = 0
        while i<l:
            while i+1<l and s[i]<s[i+1]:
                final_list.append(s[i])
                i+=1
            if not FLAG and i+1<l:
                FLAG = True
            i+=1
        if FLAG:
            final_list.append(s[-1])
        return final_list


def solution2(s):
    l = len(s)
    i = 1
    while i<l and s[i]  >= s[i-1]:
        i+=1

    if i == l:
        return s[:-1]
    elif i == 1:
        return s[1:]
    else:
        return s[:i-1] + s[i:]




print (solution2 ('abczd'))