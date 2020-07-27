class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


class Classy:

    def __init__(self):
        self.dic = {}

    def randomPointer(self,s):
        '''

        :param s:
        :return:
        '''
        if s is not None:
            if s in self.dic:
                return self.dic[s]

            self.dic[s] = Node(s.val)
            self.dic[s].next = self.randomPointer(s.next)
            self.dic[s].random = self.randomPointer(s.random)
        return self.dic[s]
