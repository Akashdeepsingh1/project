class FreqStack:
    class Node:
        def __init__ (self, x):
            self.val = x
            self.next = None
            self.prev = None

    def __init__ (self):
        self.sub_class_obj = self.Node(float('inf'))
        self.start = None
        self.end = None

    def push (self, x: int) -> None:
        obj = self.Node (x)
        if self.start == None:
            self.start = obj
            self.end = obj
        else:
            self.end.next = obj
            obj.prev = self.end
            self.end = obj

    def pop (self) -> int:
        if self.start is not None:
            temp = self.start.val
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
            else:
                self.end.prev = None
            return temp
        return 0

from collections import defaultdict
from heapq import heappush, heappop, _heappop_max
import collections
class FreqStack1 (object):

    def __init__ (self):
        self.freq = collections.Counter ()
        self.group = collections.defaultdict (list)
        self.maxfreq = 0

    def push (self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append (x)

    def pop (self):
        x = self.group[self.maxfreq].pop ()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x




class classy:
    def __init__(self):
        import collections
        self.counter = collections.Counter()
        self.dic = collections.defaultdict(list)
        self.max_freq = 0

    def push(self,x):
        self.counter[x] +=1
        temp = self.counter[x]
        if temp > self.max_freq:
            self.max_freq = temp
        self.dic[temp].append(x)

    def pop(self):
        if self.max_freq!=0:
            t = self.dic[self.max_freq].pop()
            self.counter[t]-=1
            if not self.dic[self.max_freq]:
                self.max_freq-=1
            return t
        return 0










obj = FreqStack1()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(4)
obj.pop()
obj.pop()
obj.pop()

