class Classy:
    def __init__(self):
        pass

    def subString(self, S):

        from collections import OrderedDict
        self.dic = OrderedDict()
        self.ls = []
        count = 0
        final_str = ""
        index = 0
        le = len(S)
        s = list(S)

        while index<le:
            temp = s[index]
            if temp not in self.ls:
                self.ls.append(temp)
                self.dic[temp] = index
                if count< len(self.ls):
                    count = len(self.ls)
                    final_str = ''.join(self.ls)
            else:
                
                self.dic[temp] = index
                self.ls.append(temp)
            index+=1
        return count,final_str

obj = Classy()
print (obj.subString ('abcabcbb'))
print(obj.subString('bbbbb'))
print(obj.subString('pwwkew'))
