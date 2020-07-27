from collections import defaultdict,Counter
class Classy:
    def __init__(self):
        self.freq = Counter()
        self.dic = defaultdict(list)
        self.max_freq = 0

    def push(self,x):
        self.freq[x]+=1
        t = self.freq[x]
        self.dic[t].append(x)
        if self.max_freq < t:
            self.max_freq = t


    def pop(self):
        if self.max_freq == 0:
            return None
        t = self.dic[self.max_freq].pop()
        self.freq[t]-=1
        if not self.dic[self.max_freq]:
            self.max_freq -=1
        return t



obj = Classy()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(4)
print (obj.pop ())
print (obj.pop ())
print (obj.pop ())
print (obj.pop ())
print (obj.pop ())
print (obj.pop ())
print(obj.pop())