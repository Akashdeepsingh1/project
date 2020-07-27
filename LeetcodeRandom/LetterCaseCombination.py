def letterCasePermutation(s):
    if len(s)==0:
        return []
    res = []
    dfs(s,0,"",res)
    return res

def dfs(s,index,path,res):
    if len(s) == len(path):
        res.append(path)
        return
    for j in s[index]:
        temp = ord(j)
        if 48<=temp<=57:
            dfs(s,index+1,path+j,res)
        elif 65<=temp<=90:
            dfs(s,index+1,path+str(chr(temp+32)),res)
            dfs(s,index+1,path+j,res)
        elif 97<=temp<=122:
            dfs(s,index+1,path+str(chr(temp-32)),res)
            dfs(s,index+1,path+j,res)


print (letterCasePermutation ('3z4'))