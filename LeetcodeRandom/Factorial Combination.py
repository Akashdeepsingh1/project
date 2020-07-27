def getFactors(n):
    ret = []
    def DFS(cur,i):
        num = cur.pop()
        while i*i <= num:
            div = num//i
            if num%i == 0 and div!=1:
                ret.append(cur+[i,div])
                DFS(cur+[i,div],i)
            i+=1

    DFS([n],2)
    return ret


print (getFactors (12))