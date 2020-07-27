def findJudge ( N, trust) -> int:
    if N == 1:
        return 1
    elif N > 1:
        temp = [i for i in range (1, N + 1)]
        while len (temp) > 1:
            temp0 = temp.pop ()
            temp1 = temp.pop ()
            if [temp0, temp1] in trust:
                temp.append (temp1)
            elif [temp1, temp0]:
                temp.append (temp0)
        if len (temp) == 1:
            FLAG = True
            for i in range (1, N+1):
                if ([i, temp[0]] in trust and [temp[0],i]) or i == temp[0]:
                    continue
                else:
                    FLAG = False
                #if [temp[0], i] in trust and i != temp[0]:
                #   return -1
            if FLAG:
                return temp[0]
            return -1


N = 3
trust = [[1,2],[2,3]]
print(findJudge(N,trust))

