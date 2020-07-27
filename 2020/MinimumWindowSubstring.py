class Classy:
    def __init__(self):
        pass


    def checkCount(self, item):
        for each in self.smallS:
            if each not in item:
                return float('inf')
        return len(item)


    def minimumWindom(self, S, T):
        self.smallS = list(T)
        count = float('inf')
        self.dic = []
        final_string= ""



        for i in range(len(S)):
            for j in range(i, len(S)):
                item1 = S[i:j]
                item2 = S[j:]

                if item1 not in self.dic:
                    temp = self.checkCount(item1)
                    if temp< count:
                        count = temp
                        final_string = ''.join(item1)
                    self.dic.append(item1)

                if item2 not in self.dic:
                    temp1 = self.checkCount(item2)
                    if temp1<count:
                        count = temp1
                        final_string = "".join(item2)
                    self.dic.append(item2)

        return final_string


obj = Classy()
S = "ADOBECODEBANC"

T = "ABC"
s1 = "a"
t = "a"

s2 = "ab"
t2 = "b"

s3 = "abc"
t3 = "ac"

print (obj.minimumWindom (S, T))
print(obj.minimumWindom(s1,t))
print(obj.minimumWindom(s2,t2))
print(obj.minimumWindom(s3,t3))


