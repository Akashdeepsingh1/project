from collections import defaultdict

class CustomMap:
    def __init__(self):
        self.dic = {}
        self.tracker = {}
        self.val = -1

    def set(self, key, val):
        self.dic[key] = val
        self.tracker[key] = val

    def get(self, key):
        if key in self.dic and key not in self.tracker :
            return self.val
        elif key in self.dic and key in self.tracker:
            return self.dic[key]
        else:
            return -1

    def setAll(self,val):
        self.val = val
        self.tracker.clear()


map = CustomMap()





map.set(0, 1)
print (map.get (0))
map.set(1, 2)
print (map.get (1))
map.setAll(5)#
print (map.get (0))
print (map.get (1))
print (map.get (2))
map.set(2, 7)#
print (map.get (0))
print (map.get (1))
print (map.get (2))

