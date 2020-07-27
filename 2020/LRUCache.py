class LRU:

    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None



    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.ls = []
        self.counter = 0
        self.obj = self.Node(None)
        self.start = None
        self.end = None


    def set(self, key, value):
        if key in self.dic:

            if self.start == self.dic[key]:
                return self.start.val
            else:
                node = self.dic[key]
                node.val = value
                node.left.right = node.right
                node.right.left = node.left
                self.start.left = node
                node.right  = self.start
                self.start = node

        else:
            node = self.Node (key)
            if self.counter == 0:
                self.start = node
                self.end = node
                self.counter = 1
            else:
                if self.counter == self.capacity:
                    self.end.left.right = None
                    del self.dic[self.end]

                else:
                    self.counter +=1
                node.right = self.start
                self.start.left = node
                node.right = self.start
                self.start = node
            self.dic[key] = node


    def get(self,key ):
        if key in self.dic:
            if self.start== self.dic[key]:
                return self.start.val
            elif self.end == self.dic[key]:
                if self.start == self.end:
                    return self.start.val
                else:
                    temp = self.end
                    self.end.left.right = None
                    self.end = self.end.left
                    self.start.left = temp
                    temp.right = self.start
                    temp.left = None
                    self.start = temp
                    return temp.val
            else:
                node = self.dic[key]
                # consider 3 situation if it is the last element, in the middle or first element
                node.left.right = node.right
                node.right.left = node.left
                self.start.left = node
                node.right = self.start
                self.start = node
                return node.val
        else:
            return -1





obj = LRU(2)
obj.set(1,1)
obj.set(2,2)
print (obj.get (1))
print(obj.start)
print(obj.end)
