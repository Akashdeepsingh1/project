def solution(s):
    l = len(s)
    if l ==0 :
        return 0
    elif l == 1:
        return s
    else:
        i = 0
        j = l-1
        Flag = False
        while i<j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                if Flag:
                    return False
                Flag = True

                if s[i+1] == s[j]:
                    i+=1
                else:
                    j-=1
        return True


print (solution ('abbca'))
