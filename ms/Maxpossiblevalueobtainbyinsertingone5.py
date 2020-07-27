def solution(n):
    if n == 0:
        return 50


    elif n < 0:
        n *= -1
        l = list(str(n))
        i = 0
        flag = True
        while i<len(l):
            if int(l[i])>=5:
                l.insert(i,'5')
                flag = False
                break
            i+=1
        if flag:
            l.append('5')
        t = ''.join(l)
        return int(t)*-1
    else:
        l = list(str(n))
        i = 0
        flag = True
        while i<len(l):
            if int(l[i])<=5:
                l.insert(i,'5')
                flag = False
                break
            i+=1
        if flag:
            l.append('5')
        t = ''.join(l)
        return int(t)

print(solution(9))

