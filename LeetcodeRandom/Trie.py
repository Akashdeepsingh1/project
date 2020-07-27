class Trie():
    def __init__(self, ls):
        for each in ls:
            self.each = each
            self.next = None


class Tree:
    def __init__(self):
        self.firstNode = None

    def insert(self, ls):
        node = Trie(ls)
        if self.firstNode is None:
            

