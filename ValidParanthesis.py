class Classy:
    def __init__(self):
        pass

    def validParanthesis(self, s):
        le = len(s)
        if le ==0 :
            return True
        elif le ==1:
            return False
        else:
            dic = {'}':'{',')':'(',']':'['}
            stck = []
            for each in s:
                if str(each) in dic:
                    temp = stck.pop()
                    if dic[each] != temp:
                        return False
                else:
                    stck.append(str(each))
            if len(stck) == 0:
                return True
            else:
                return False



obj = Classy()
print (obj.validParanthesis ('()'))
print(obj.validParanthesis('(){}[]'))
print(obj.validParanthesis('(]'))
print(obj.validParanthesis('([)]'))
print(obj.validParanthesis('{[]}'))
